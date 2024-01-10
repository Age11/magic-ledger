from magic_ledger.third_parties.models.addressbook import Addressbook


def get_addressbook_by_id(address_id):
    return Addressbook.query.filter_by(id=address_id).first()
