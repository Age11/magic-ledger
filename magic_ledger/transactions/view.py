import json

from flask import Blueprint
from flask import request
from flask import flash
from flask import jsonify
from magic_ledger import db
from magic_ledger.transactions.model import Transaction
from magic_ledger.account_plan.model import AccountPlan
import logging

bp = Blueprint("transactions", __name__, url_prefix="/transactions/")


@bp.route("/", methods=("GET", "POST"))
def invoices():
    if request.method == "POST":
        logging.info('''Creating transaction with the following data:''')
        logging.info(request.json)

        # The type will determin weather we add something to the inventory or not
        debit_account_id = request.json["debit_account_id"]
        credit_account_id = request.json["credit_account_id"]
        amount = request.json["amount"]
        currency = request.json["currency"]
        transaction_date = request.json["transaction_date"]
        organization_id = request.json["organization_id"]
        details = request.json["details"]

        error = None

        if not debit_account_id:
            error = "debit_account_id is required."
        if not credit_account_id:
            error = "credit_account_id id is required."
        if not amount:
            error = "amount is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            new_transaction = Transaction(debit_account_id=debit_account_id, credit_account_id=credit_account_id, amount=amount, currency=currency, transaction_date=transaction_date, organization_id=organization_id, details=details)
            db.session.add(new_transaction)
            db.session.commit()
            response = jsonify()
            response.status_code = 201
            response.headers['location'] = '/invoices/' + str(new_transaction.id)
            return response
    elif request.method == "GET":
        txs = Transaction.query.all()
        json_data = json.dumps([row.__getstate__() for row in txs], default=str)
        return json_data

@bp.route("/<int:transaction_id>")
def get_transaction(transaction_id):
    if request.method == "GET":
        inv = Transaction.query.filter_by(id=transaction_id).first().__getstate__()
        inv['debit_account_name'] = AccountPlan.query.filter_by(account=inv['debit_account_id']).first().name
        inv['credit_account_name'] = AccountPlan.query.filter_by(account=inv['credit_account_id']).first().name
        json_data = json.dumps(inv, default=str)
        return json_data