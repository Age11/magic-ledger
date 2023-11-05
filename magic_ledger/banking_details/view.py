import json

from flask import Blueprint
from flask import request
from flask import flash
from flask import jsonify
from magic_ledger import db
from magic_ledger.banking_details.model import BankingDetails
import logging

bp = Blueprint("bank_details", __name__, url_prefix="/bank_details")

@bp.route("/", methods=("GET", "POST"))
def invoices():
    if request.method == "POST":
        logging.info('''Creating banking details with the following data:''')
        logging.info(request.json)

        organization_id = request.json["organization_id"]
        account = request.json["account"]
        details = request.json["details"]


        error = None

        if not organization_id:
            error = "organization id is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            address = BankingDetails(account=account, organization_id=organization_id, details=details)
            db.session.add(address)
            db.session.commit()
            return jsonify(address)
    elif request.method == "GET":
        addresses = BankingDetails.query.all()
        json_data = json.dumps([row.__getstate__() for row in addresses], default=str)
        return json_data
