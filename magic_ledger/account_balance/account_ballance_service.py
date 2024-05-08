from datetime import datetime

from dateutil.relativedelta import relativedelta

from sqlalchemy import and_, not_, or_, func
from sqlalchemy.sql import extract

from magic_ledger.account_balance.account_balance import AccountBalance
from magic_ledger import db
from magic_ledger.account_plan import account_plan_service


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


def get_income_accounts(owner_id, balance_date):
    return (
        db.session.query(AccountBalance)
        .filter(
            or_(
                AccountBalance.analytical_account.like("7%"),
                AccountBalance.analytical_account == "609",
            ),
            not_(AccountBalance.analytical_account == "709"),
            AccountBalance.owner_id == owner_id,
            AccountBalance.processed == False,
            func.strftime("%Y-%m", AccountBalance.balance_date) == balance_date,
        )
        .all()
    )


def get_expenses_accounts(owner_id, balance_date):
    return (
        db.session.query(AccountBalance)
        .filter(
            or_(
                AccountBalance.analytical_account.like("6%"),
                AccountBalance.analytical_account == "709",
            ),
            not_(AccountBalance.analytical_account == "609"),
            AccountBalance.owner_id == owner_id,
            AccountBalance.processed == False,
            func.strftime("%Y-%m", AccountBalance.balance_date) == balance_date,
        )
        .all()
    )


def get_current_profit_or_loss(owner_id, balance_date):
    if not account_balance_exists(owner_id, "121")[0]:
        create_account_balance(owner_id, "121")
    profit_or_loss = AccountBalance.query.filter_by(
        owner_id=owner_id, analytical_account="121"
    ).first()
    if profit_or_loss.processed == True:
        return profit_or_loss.get_final_balance()[0]
    else:
        income_accounts = get_income_accounts(owner_id, balance_date)
        expense_accounts = get_expenses_accounts(owner_id, balance_date)
        total_income = 0
        total_expenses = 0
        current_profit_or_loss, balance_type = profit_or_loss.get_final_balance()

        for acc in income_accounts:
            total_income += acc.get_final_balance()[0]

        for acc in expense_accounts:
            total_expenses += acc.get_final_balance()[0]

        return current_profit_or_loss + total_income - total_expenses


def get_account_final_balance(owner_id, analytical_account, balance_date):
    bd = datetime.strptime(balance_date, "%Y-%m")
    ab = AccountBalance.query.filter(
        and_(
            AccountBalance.owner_id == owner_id,
            extract("month", AccountBalance.balance_date) == bd.month,
            extract("year", AccountBalance.balance_date) == bd.year,
            AccountBalance.analytical_account == analytical_account,
            AccountBalance.processed == False,
        )
    ).first()
    if ab:
        return ab.get_final_balance()
    else:
        0, account_plan_service.get_account_type(analytical_account)
