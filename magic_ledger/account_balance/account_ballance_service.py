from datetime import datetime

from dateutil.relativedelta import relativedelta
from flask_sqlalchemy import session
from sqlalchemy import and_, not_, or_
from sqlalchemy.sql import extract

from magic_ledger.account_balance.account_balance import AccountBalance
from magic_ledger import db


def create_account_balance(
    project_id, analytical_account, balance_date=datetime.now().strftime("%Y-%m-%d")
):
    account = AccountBalance(
        analytical_account=analytical_account,
        owner_id=project_id,
        balance_date_string=balance_date,
    )
    db.session.add(account)
    db.session.commit()
    return account


def account_balance_exists(
    owner_id,
    analytical_account,
    acct_balance_month=datetime.now().month,
    acct_balance_year=datetime.now().year,
):
    account = (
        db.session.query(AccountBalance)
        .filter(
            and_(
                AccountBalance.owner_id == owner_id,
                AccountBalance.analytical_account == analytical_account,
                extract("month", AccountBalance.balance_date) == acct_balance_month,
                extract("year", AccountBalance.balance_date) == acct_balance_year,
            )
        )
        .first()
    )

    if account:
        return True, account
    return False, None


def update_account_balance(
    owner_id,
    analytical_account,
    balance_date,
    initial_debit=0,
    initial_credit=0,
    cumulated_debit=0,
    cumulated_credit=0,
    current_rollover_debit=0,
    current_rollover_credit=0,
):
    bd = datetime.strptime(balance_date, "%Y-%m-%d")
    exists, account = account_balance_exists(
        owner_id, analytical_account, bd.month, bd.year
    )
    if exists:
        account.update_balance(
            initial_debit,
            initial_credit,
            cumulated_debit,
            cumulated_credit,
            current_rollover_debit,
            current_rollover_credit,
        )
        db.session.add(account)
    else:
        account = create_account_balance(
            owner_id, analytical_account, bd.strftime("%Y-%m-%d")
        )
        account.update_balance(
            initial_debit,
            initial_credit,
            cumulated_debit,
            cumulated_credit,
            current_rollover_debit,
            current_rollover_credit,
        )
        db.session.add(account)
    db.session.commit()
    return account


def close_monthly_balance_accounts(project_id, balance_date_string):
    balance_date = datetime.strptime(balance_date_string, "%Y-%m")
    accounts = (
        db.session.query(AccountBalance)
        .filter(
            and_(
                AccountBalance.owner_id == project_id,
                extract("month", AccountBalance.balance_date) == balance_date.month,
                extract("year", AccountBalance.balance_date) == balance_date.year,
            )
        )
        .all()
    )
    open_date_string = (balance_date + relativedelta(months=1)).strftime("%Y-%m-%d")

    if balance_date.month == 12:
        for account in accounts:
            account.cumulate_amounts()
            account.calculate_total_amounts()

    for account in accounts:
        account.cumulate_amounts()
        account.calculate_total_amounts()
        account.calculate_final_amounts()
        account.processed = True
        new_account = AccountBalance(
            analytical_account=account.analytical_account,
            owner_id=account.owner_id,
            balance_date_string=open_date_string,
        )
        new_account.initial_debit = account.initial_debit
        new_account.initial_credit = account.initial_credit
        new_account.cumulated_debit = account.cumulated_debit
        new_account.cumulated_credit = account.cumulated_credit
        db.session.add(new_account)
    db.session.commit()


def get_account_balances(owner_id):
    accounts = AccountBalance.query.filter_by(owner_id=owner_id).all()
    return accounts


def get_balance_for_date(owner_id, balance_date):
    bd = datetime.strptime(balance_date, "%Y-%m")
    accounts = AccountBalance.query.filter(
        and_(
            AccountBalance.owner_id == owner_id,
            extract("month", AccountBalance.balance_date) == bd.month,
            extract("year", AccountBalance.balance_date) == bd.year,
        )
    ).all()
    return accounts


def get_available_dates(owner_id):
    dates = AccountBalance.query.filter_by(owner_id=owner_id).all()
    res = []
    for date in dates:
        res.append(date.balance_date.strftime("%Y-%m"))
    return list(set(res))


def get_account_totals(owner_id, analytical_account):
    account = AccountBalance.query.filter_by(
        owner_id=owner_id, analytical_account=analytical_account, processed=False
    ).first()

    total_debit = account.get_total_debit_balance()
    total_credit = account.get_total_credit_balance()
    final_balance = total_debit - total_credit
    return total_debit, total_credit, final_balance


def get_current_profit_or_loss(owner_id):
    income_accounts = (
        db.session.query(AccountBalance)
        .filter(
            or_(
                AccountBalance.analytical_account.like("7%"),
                AccountBalance.analytical_account == "609",
            ),
            not_(AccountBalance.analytical_account == "709"),
            AccountBalance.owner_id == owner_id,
        )
        .all()
    )
    expense_accounts = (
        db.session.query(AccountBalance)
        .filter(
            or_(
                AccountBalance.analytical_account.like("6%"),
                AccountBalance.analytical_account == "709",
            ),
            not_(AccountBalance.analytical_account == "609"),
            AccountBalance.owner_id == owner_id,
        )
        .all()
    )
    total_income = 0
    total_expenses = 0
    if not account_balance_exists(owner_id, "121")[0]:
        create_account_balance(owner_id, "121")
    profit_or_loss = AccountBalance.query.filter_by(
        owner_id=owner_id, analytical_account="121"
    ).first()
    current_profit_or_loss = (
        profit_or_loss.get_total_debit_balance()
        - profit_or_loss.get_total_credit_balance()
    )

    for acc in income_accounts:
        debit = acc.get_total_debit_balance()
        credit = acc.get_total_credit_balance()
        total_income += debit - credit

    for acc in expense_accounts:
        debit = acc.get_total_debit_balance()
        credit = acc.get_total_credit_balance()
        total_expenses += debit - credit

    return current_profit_or_loss - total_income - total_expenses
