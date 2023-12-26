import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.invoices.invoice import Invoice

bp = Blueprint("invoices", __name__, url_prefix="/<project_id>/invoices")


@bp.route("/", methods=("GET", "POST"))
def invoices(project_id):
    if request.method == "POST":
        logging.info("""Creating invoice with the following data:""")
        logging.info(request.json)

        # The type will determin weather we add something to the inventory or not
        inv_type = request.json["inv_type"]
        number = request.json["number"]
        serial = request.json["serial"]
        receive_date = request.json["receive_date"]
        due_date = request.json["due_date"]
        issue_date = request.json["issue_date"]
        payment_status = request.json["payment_status"]
        supplier_id = request.json["supplier_id"]
        client_id = request.json["client_id"]
        amount = request.json["amount"]
        currency = request.json["currency"]
        issuer_name = request.json["issuer_name"]
        error = None

        if not number:
            error = "Number is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            new_invoice = Invoice(
                inv_type=inv_type,
                number=number,
                serial=serial,
                receive_date=receive_date,
                issue_date=issue_date,
                due_date=due_date,
                payment_status=payment_status,
                owner_id=project_id,
                supplier_id=supplier_id,
                client_id=client_id,
                amount=amount,
                currency=currency,
                issuer_name=issuer_name,
            )
            db.session.add(new_invoice)
            db.session.commit()
            response = jsonify()
            response.status_code = 201
            response.headers["location"] = "/" + project_id + "/invoices/" + str(new_invoice.id)
            return response
    elif request.method == "GET":
        invs = Invoice.query.filter_by(owner_id=project_id).all()

        return jsonify([row.__getstate__() for row in invs])


@bp.route("/<int:invoice_id>", methods=("GET", "PUT", "DELETE"))
def invoice(project_id, invoice_id):
    invoice = Invoice.query.filter_by(owner_id=project_id, id=invoice_id).first()
    if request.method == "GET":
        return jsonify(invoice.__getstate__())
