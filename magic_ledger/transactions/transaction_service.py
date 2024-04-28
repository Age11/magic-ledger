from magic_ledger import db
from magic_ledger.transactions.transaction import Transaction
import magic_ledger.account_balance.account_ballance_service as balance_service


def create_transaction(request_body):
    transaction = Transaction(**request_body)
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


def create_transaction_and_update_balance(request_body):
    transaction = create_transaction(request_body)

    # update account balance
    balance_service.update_account_balance(
        owner_id=request_body["owner_id"],
        analytical_account=request_body["debit_account"],
        current_rollover_debit=request_body["debit_amount"],
        balance_date=request_body["transaction_date"],
    )

    balance_service.update_account_balance(
        owner_id=request_body["owner_id"],
        analytical_account=request_body["credit_account"],
        current_rollover_credit=request_body["credit_amount"],
        balance_date=request_body["transaction_date"],
    )

    return transaction


def get_transactions_by_type(owner_id, tx_type, tx_date):
    resp = []
    transactions = Transaction.query.filter_by(owner_id=owner_id).all()
    for transaction in transactions:
        if (
            transaction.tx_type in tx_type
            and transaction.transaction_date.strftime("%Y-%m") == tx_date
        ):
            resp.append(transaction)
    return resp


def get_available_dates(owner_id):
    transactions = Transaction.query.filter_by(owner_id=owner_id).all()
    dates = []
    for transaction in transactions:
        dates.append(transaction.transaction_date.strftime("%Y-%m"))
    return list(set(dates))


def get_all_transactions_for_month(owner_id, tx_date):
    transactions = Transaction.query.filter_by(owner_id=owner_id).all()
    resp = []
    for transaction in transactions:
        if transaction.transaction_date.strftime("%Y-%m") == tx_date:
            resp.append(transaction)
    return resp
