import json

from flask import Blueprint
from flask import request
from flask import flash
from flask import jsonify
from magic_ledger import db
from magic_ledger.invoices.model import Invoice
import logging

bp = Blueprint("invoices", __name__, url_prefix="/invoices")


@bp.route("/", methods=("GET", "POST"))
def invoices():
    if request.method == "POST":
        logging.info('''Creating invoice with the following data:''')
        logging.info(request.json)

        # The type will determin weather we add something to the inventory or not
        inv_type = request.json["inv_type"]
        number = request.json["number"]
        serial = request.json["serial"]
        receive_date = request.json["receive_date"]
        due_date = request.json["due_date"]
        issue_date = request.json["issue_date"]
        payment_status = request.json["payment_status"]
        org_id = request.json["organization_id"]
        supplier_id = request.json["supplier_id"]
        client_id = request.json["client_id"]
        amount = request.json["amount"]
        currency = request.json["currency"]
        issuer_name = request.json["issuer_name"]
        error = None

        if not number:
            error = "Number is required."
        if not org_id:
            error = "Company id is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            new_invoice = Invoice(inv_type=inv_type, number=number, serial=serial, receive_date=receive_date,
                                  issue_date=issue_date, due_date=due_date, payment_status=payment_status,
                                  organization_id=org_id, supplier_id=supplier_id, client_id=client_id, amount=amount,
                                  currency=currency, issuer_name=issuer_name)
            db.session.add(new_invoice)
            db.session.commit()
            return jsonify(new_invoice)
    elif request.method == "GET":
        invoices = Invoice.query.all()
        json_data = json.dumps([row.__getstate__() for row in invoices], default=str)
        return json_data
