from magic_ledger import db
from magic_ledger.transactions.transaction import Transaction


def create_transaction(request_body):
    transactions_data = {
        k: request_body[k]
        for k in (
            "debit_account",
            "credit_account",
            "debit_amount",
            "credit_amount",
            "currency",
            "transaction_date",
            "details",
            "owner_id",
        )
    }
    transaction = Transaction(**transactions_data)
    db.session.add(transaction)
    db.session.commit()
    return transaction


def get_all_transactions(owner_id):
    transactions = Transaction.query.filter_by(owner_id=owner_id).all()
    return transactions


def get_transaction_by_id(transaction_id, owner_id):
    transaction = Transaction.query.filter_by(
        id=transaction_id, owner_id=owner_id
    ).first()
    return transaction
