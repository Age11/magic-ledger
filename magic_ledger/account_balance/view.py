import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.account_balance.account_balance import AccountBalance

bp = Blueprint("account_balance", __name__, url_prefix="/<project_id>/account-balance")


def account_exists(analytical_account):
    account = AccountBalance.query.filter_by(
        analytical_account=analytical_account
    ).first()
    if account:
        return True
    else:
        return False


@bp.route("/set-initial", methods=("GET", "POST"))
def account_balance(project_id):
    if request.method == "POST":
        logging.info("""adding account balance with the following data:""")
        logging.info(request.json)

        analytical_account = request.json["analytical_account"]
        initial_debit = request.json["initial_debit"]
        initial_credit = request.json["initial_credit"]

        error = None

        if not analytical_account:
            error = "account is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        if account_exists(analytical_account):
            account = AccountBalance.query.filter_by(
                analytical_account=analytical_account
            ).first()
            account.initial_debit = initial_debit
            account.initial_credit = initial_credit
            db.session.commit()
        else:
            account = AccountBalance(
                analytical_account=analytical_account,
                owner_id=project_id,
            )
            account.initial_debit = initial_debit
            account.initial_credit = initial_credit
            db.session.add(account)
            db.session.commit()
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/invoices/" + str(account.id)
        return response
    elif request.method == "GET":
        balance = AccountBalance.query.all()
        return jsonify([row.__getstate__() for row in balance])
