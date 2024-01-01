from datetime import datetime

from magic_ledger.account_balance.account_balance import AccountBalance


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
            account.current_debit += current_debit
            account.current_debit += current_credit
            return account
        else:
            account = AccountBalance(
                analytical_account=analytical_account,
                owner_id=project_id,
                balance_date=balance_date
            )
            account.initial_debit = initial_debit
            account.initial_credit = initial_credit
            account.current_debit = current_debit
            account.current_credit = current_credit
            return account
