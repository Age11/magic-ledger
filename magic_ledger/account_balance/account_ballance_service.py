from datetime import datetime

from dateutil.relativedelta import relativedelta
from flask_sqlalchemy import session
from sqlalchemy import and_
from sqlalchemy.sql import extract

from magic_ledger.account_balance.account_balance import AccountBalance
from magic_ledger import db


def create_account_balance(project_id, analytical_account, balance_date):
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
    acct_balance_month,
    acct_balance_year,
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
        new_account = AccountBalance(
            analytical_account=account.analytical_account,
            owner_id=account.owner_id,
            balance_date_string=open_date_string,
        )
        new_account.initial_debit = account.initial_debit
        new_account.initial_credit = account.initial_credit
        new_account.cumulated_debit = account.cumulated_debit
        new_account.cumulated_credit = account.cumulated_credit
        account.processed = True
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
