from magic_ledger.third_parties.models.banking_details import BankingDetails


def get_banking_details_by_id(banking_details_id):
    return BankingDetails.query.filter_by(id=banking_details_id).first()
