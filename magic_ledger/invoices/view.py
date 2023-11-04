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
        logging.info(request.form)
        logging.info(request.data)
        #The type will determin weather we add something to the inventory or not
        inv_type = request.json["inv_type"]
        number = request.json["number"]
        serial = request.json["serial"]
        receive_date = request.json["receive_date"]
        due_date = request.json["due_date"]
        state = request.json["state"]
        org_id = request.json["organization_id"]

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
                                  due_date=due_date, state=state, organization_id=org_id)
            db.session.add(new_invoice)
            db.session.commit()
            return jsonify(new_invoice)
    elif request.method == "GET":
        invoices = Invoice.query.all()
        json_data = json.dumps([row.__getstate__() for row in invoices], default=str)
        return json_data
