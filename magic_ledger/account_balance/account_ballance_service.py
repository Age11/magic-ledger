from datetime import datetime

from dateutil.relativedelta import relativedelta

from magic_ledger.account_balance.account_balance import AccountBalance
from magic_ledger import db

class AccountBalanceService:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AccountBalanceService, cls).__new__(cls)
        return cls._instance


    def account_balance_exists(self, owner_id, analytical_account, balance_date):
        account = AccountBalance.query.filter_by(owner_id=owner_id, analytical_account=analytical_account,
                                                 balance_date=balance_date).first()
        if account:
            return True
        else:
            return False


    def update_account_balance(self, project_id, analytical_account, balance_date, initial_debit=0, current_debit=0, initial_credit=0,
                               current_credit=0):
        if self.account_balance_exists(project_id, analytical_account, balance_date):
            account = AccountBalance.query.filter_by(
                owner_id=project_id,
                analytical_account=analytical_account,
                balance_date=balance_date
            ).first()
            account.initial_debit += initial_debit
            account.initial_credit += initial_credit
            account.debit += current_debit
            account.debit += current_credit
            return account
        else:
            account = AccountBalance(
                analytical_account=analytical_account,
                owner_id=project_id,
                balance_date=balance_date
            )
            account.initial_debit = initial_debit
            account.initial_credit = initial_credit
            account.credit = current_debit
            account.credit = current_credit
            return account

    def close_balance_accounts(self,project_id, balance_date):
        accounts = AccountBalance.query.filter_by(balance_date=balance_date, owner_id=project_id).all()
        open_date = (datetime.strptime(balance_date, "%Y-%m") + relativedelta(months=1)).strftime("%Y-%m")
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




