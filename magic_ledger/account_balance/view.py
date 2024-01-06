import logging
from datetime import datetime

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.account_balance.account_balance import AccountBalance
import magic_ledger.account_balance.account_ballance_service as abs
from magic_ledger.misc.clock import CLOCK

bp = Blueprint("account_balance", __name__, url_prefix="/<project_id>/account-balance")


@bp.route("/", methods=("GET", "POST"))
def account_balance(project_id):
    if request.method == "POST":
        logging.info("""adding initial account balance with the following data:""")
        logging.info(request.json)

        error = None

        if not len(request.json) > 0:
            error = "provide some balance entries"
        # TODO: add more validation

        for balance in request.json:
            balance["owner_id"] = project_id
            # TODO this is the only date I pass as date instead of string. Fix it. You need to add a way to get date as String easily
            balance["balance_date"] = datetime.strptime(balance["balance_date"], "%Y-%m")
            account = abs.update_account_balance(
                **balance
            )

        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/account-balance/set-initial/"
        response.autocorrect_location_header = False
        return response
    elif request.method == "GET":
        balance = AccountBalance.query.filter_by(owner_id=project_id).all()
        return jsonify([row.__getstate__() for row in balance])


@bp.route("/close/<balance_date>", methods=("GET", "POST"))
def close_month(project_id, balance_date):
    if request.method == "POST":
        logging.info("""closing balance for the following month:""" + balance_date)
        abs.close_balance_accounts(project_id=project_id, balance_date=balance_date)
        response = jsonify()
        response.status_code = 201
        return response
