from magic_ledger import db
from magic_ledger.transactions.transaction import Transaction




def create_transaction(request_body):
    transactions_data = {k: request_body[k] for k in (
        'debit_account_id', 'credit_account_id', 'debit_amount', 'credit_amount', 'currency', 'transaction_date', 'details', 'owner_id')}
    transaction = Transaction(
        **transactions_data
    )
    db.session.add(transaction)
    db.session.commit()
    return transaction
