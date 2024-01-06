from datetime import datetime

from dateutil.relativedelta import relativedelta

from magic_ledger.account_balance.account_balance import AccountBalance
from magic_ledger import db



def create_account_balance(project_id, analytical_account, balance_date):
    account = AccountBalance(
        analytical_account=analytical_account,
        owner_id=project_id,
        balance_date=balance_date
    )
    db.session.add(account)
    db.session.commit()
    return account

def account_balance_exists(owner_id, analytical_account, balance_date):
    account = AccountBalance.query.filter_by(owner_id=owner_id, analytical_account=analytical_account,
                                             balance_date=balance_date).first()
    if account:
        return True
    else:
        return False
def update_account_balance(owner_id, analytical_account, balance_date, initial_debit=0, debit=0, initial_credit=0,
                           credit=0):
    if account_balance_exists(owner_id, analytical_account, balance_date):
        account = AccountBalance.query.filter_by(
            owner_id=owner_id,
            analytical_account=analytical_account,
            balance_date=balance_date
        ).first()
        account.initial_debit += initial_debit
        account.initial_credit += initial_credit
        account.debit += debit
        account.credit += debit
        db.session.add(account)
    else:
        account = AccountBalance(
            analytical_account=analytical_account,
            owner_id=owner_id,
            balance_date=balance_date
        )
        account.initial_debit = initial_debit
        account.initial_credit = initial_credit
        account.debit = credit
        account.credit = credit
        db.session.add(account)
    db.session.commit()
    return account
def close_balance_accounts(project_id, balance_date):
    balance_date = datetime.strptime(balance_date, "%Y-%m")
    accounts = AccountBalance.query.filter_by(balance_date=balance_date, owner_id=project_id).all()
    open_date = balance_date + relativedelta(months=1)
    for account in accounts:
        account.calculate_totals()
        new_account = AccountBalance(
            analytical_account=account.analytical_account,
            owner_id=account.owner_id,
            balance_date= open_date
        )
        new_account.initial_debit = account.final_debit_balance
        new_account.initial_credit = account.final_credit_balance
        account.completed = True
        db.session.add(new_account)
    db.session.commit()

