from datetime import datetime, timedelta

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
    transactions = (
        Transaction.query.filter_by(owner_id=owner_id).order_by(Transaction.id).all()
    )
    resp = []
    for transaction in transactions:
        if transaction.transaction_date.strftime("%Y-%m") == tx_date:
            resp.append(transaction)
    return resp


def last_day_of_month(year, month):
    first_of_next_month = datetime(year, month, 1) + timedelta(days=32)
    last_day = first_of_next_month - timedelta(days=first_of_next_month.day)
    return last_day.date()


def generate_close_vat_transactions(owner_id, balance_date):
    bd = datetime.strptime(balance_date, "%Y-%m")
    collected_vat = balance_service.get_account_final_balance(
        owner_id, "4427", balance_date
    )[0]
    deductible_vat = balance_service.get_account_final_balance(
        owner_id, "4426", balance_date
    )[0]

    if collected_vat > deductible_vat:
        if deductible_vat == 0:
            create_transaction_and_update_balance(
                {
                    "debit_account": "4427",
                    "credit_account": "4423",
                    "debit_amount": collected_vat,
                    "credit_amount": collected_vat,
                    "currency": "RON",
                    "transaction_date": last_day_of_month(bd.year, bd.month).strftime(
                        "%Y-%m-%d"
                    ),
                    "details": "Regularizare TVA",
                    "tx_type": "închideri",
                    "owner_id": owner_id,
                }
            )
        else:
            create_transaction_and_update_balance(
                {
                    "debit_account": "4427",
                    "credit_account": "4426",
                    "debit_amount": deductible_vat,
                    "credit_amount": deductible_vat,
                    "currency": "RON",
                    "transaction_date": last_day_of_month(bd.year, bd.month).strftime(
                        "%Y-%m-%d"
                    ),
                    "details": "Regularizare TVA",
                    "tx_type": "închideri",
                    "owner_id": owner_id,
                }
            )

        create_transaction_and_update_balance(
            {
                "debit_account": "4427",
                "credit_account": "4423",
                "debit_amount": collected_vat - deductible_vat,
                "credit_amount": collected_vat - deductible_vat,
                "currency": "RON",
                "transaction_date": last_day_of_month(bd.year, bd.month).strftime(
                    "%Y-%m-%d"
                ),
                "details": "Regularizare TVA",
                "tx_type": "închideri",
                "owner_id": owner_id,
            }
        )
    elif deductible_vat > collected_vat:
        if collected_vat == 0:
            create_transaction_and_update_balance(
                {
                    "debit_account": "4424",
                    "credit_account": "4426",
                    "debit_amount": deductible_vat,
                    "credit_amount": deductible_vat,
                    "currency": "RON",
                    "transaction_date": last_day_of_month(bd.year, bd.month).strftime(
                        "%Y-%m-%d"
                    ),
                    "details": "Regularizare TVA",
                    "tx_type": "închideri",
                    "owner_id": owner_id,
                }
            )
        else:
            create_transaction_and_update_balance(
                {
                    "debit_account": "4427",
                    "credit_account": "4426",
                    "debit_amount": collected_vat,
                    "credit_amount": collected_vat,
                    "currency": "RON",
                    "transaction_date": last_day_of_month(bd.year, bd.month).strftime(
                        "%Y-%m-%d"
                    ),
                    "details": "Regularizare TVA",
                    "tx_type": "închideri",
                    "owner_id": owner_id,
                }
            )

        create_transaction_and_update_balance(
            {
                "debit_account": "4424",
                "credit_account": "4426",
                "debit_amount": deductible_vat - collected_vat,
                "credit_amount": deductible_vat - collected_vat,
                "currency": "RON",
                "transaction_date": last_day_of_month(bd.year, bd.month).strftime(
                    "%Y-%m-%d"
                ),
                "details": "Regularizare TVA",
                "tx_type": "închideri",
                "owner_id": owner_id,
            }
        )

    elif deductible_vat == collected_vat != 0:
        create_transaction_and_update_balance(
            {
                "debit_account": "4427",
                "credit_account": "4426",
                "debit_amount": deductible_vat,
                "credit_amount": deductible_vat,
                "currency": "RON",
                "transaction_date": last_day_of_month(bd.year, bd.month).strftime(
                    "%Y-%m-%d"
                ),
                "details": "Regularizare TVA",
                "tx_type": "închideri",
                "owner_id": owner_id,
            }
        )


def generate_close_income_and_expenses_account_transactions(owner_id, balance_date):
    bd = datetime.strptime(balance_date, "%Y-%m")
    expenses = balance_service.get_expenses_accounts(owner_id, balance_date)
    income = balance_service.get_income_accounts(owner_id, balance_date)
    for acc in expenses:
        if acc.get_final_balance()[0] > 0:
            create_transaction_and_update_balance(
                {
                    "debit_account": "121",
                    "credit_account": acc.analytical_account,
                    "debit_amount": acc.get_final_balance()[0],
                    "credit_amount": acc.get_final_balance()[0],
                    "currency": "RON",
                    "transaction_date": last_day_of_month(bd.year, bd.month).strftime(
                        "%Y-%m-%d"
                    ),
                    "details": "Închiderea conturilor de cheltuieli",
                    "tx_type": "închideri",
                    "owner_id": owner_id,
                }
            )

    for acc in income:
        if acc.get_final_balance()[0] > 0:
            create_transaction_and_update_balance(
                {
                    "debit_account": acc.analytical_account,
                    "credit_account": "121",
                    "debit_amount": acc.get_final_balance()[0],
                    "credit_amount": acc.get_final_balance()[0],
                    "currency": "RON",
                    "transaction_date": last_day_of_month(bd.year, bd.month).strftime(
                        "%Y-%m-%d"
                    ),
                    "details": "Închiderea conturilor de venituri",
                    "tx_type": "închideri",
                    "owner_id": owner_id,
                }
            )
