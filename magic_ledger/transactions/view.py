import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.account_balance.account_balance import AccountBalance
from magic_ledger.account_balance.view import account_exists
from magic_ledger.account_plan.model import AccountPlan
from magic_ledger.transactions.transaction import Transaction

bp = Blueprint("transactions", __name__, url_prefix="/<project_id>/transactions/")


@bp.route("/", methods=("GET", "POST"))
def invoices(project_id):
    if request.method == "POST":
        logging.info("""Creating transaction with the following data:""")
        logging.info(request.json)

        # The type will determin weather we add something to the inventory or not
        debit_account = request.json["debit_account"]
        credit_account = request.json["credit_account"]
        debit_amount = request.json["debit_amount"]
        credit_amount = request.json["credit_amount"]
        currency = request.json["currency"]
        transaction_date = request.json["transaction_date"]
        details = request.json["details"]

        error = None

        if not debit_account:
            error = "debit_account_id is required."
        if not credit_account:
            error = "credit_account_id id is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            if account_exists(debit_account):
                account = AccountBalance.query.filter_by(
                    analytical_account=debit_account
                ).first()
                account.initial_debit += debit_amount
                db.session.commit()
            else:
                account = AccountBalance(analytical_account=debit_account, owner_id=project_id)
                account.update_current_debit(debit_amount)
                db.session.add(account)

            if account_exists(credit_account):
                account = AccountBalance.query.filter_by(
                    analytical_account=credit_account
                ).first()
                account.initial_credit += credit_amount
                db.session.commit()
            else:
                account = AccountBalance(analytical_account=credit_account, owner_id=project_id)
                account.update_current_credit(credit_amount)
                db.session.add(account)

            new_transaction = Transaction(
                debit_account_id=debit_account,
                credit_account_id=credit_account,
                debit_amount=debit_amount,
                credit_amount=credit_amount,
                currency=currency,
                transaction_date=transaction_date,
                owner_id=project_id,
                details=details,
            )
            db.session.add(new_transaction)
            db.session.commit()
            response = jsonify()
            response.status_code = 201
            response.headers["location"] = "/" + project_id + "/transactions/" + str(new_transaction.id)
            return response
    elif request.method == "GET":
        txs = Transaction.query.all()
        return jsonify([row.__getstate__() for row in txs])


@bp.route("/<int:transaction_id>")
def get_transaction(project_id, transaction_id):
    if request.method == "GET":
        inv = Transaction.query.filter_by(id=transaction_id, owner_id=project_id).first().__getstate__()
        inv["debit_account_name"] = (
            AccountPlan.query.filter_by(account=inv["debit_account_id"]).first().acc_name
        )
        inv["credit_account_name"] = (
            AccountPlan.query.filter_by(account=inv["credit_account_id"]).first().acc_name
        )
        return jsonify(inv)
