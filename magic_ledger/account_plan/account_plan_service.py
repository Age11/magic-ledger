from magic_ledger.account_plan.model import AccountPlan


def get_account_type(account):
    acc_type = AccountPlan.query.filter_by(account=account).first().acc_type
    if acc_type == "A":
        return "debit"
    elif acc_type == "P":
        return "credit"
    else:
        return "bifunctional"
