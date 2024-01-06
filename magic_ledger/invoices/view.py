import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.invoices import invoice_service, payment_status, document_type
from magic_ledger.invoices.invoice import Invoice

bp = Blueprint("invoices", __name__, url_prefix="/<project_id>/invoices")


@bp.route("/", methods=("GET", "POST"))
def invoices(project_id):
    if request.method == "POST":
        logging.info("""Creating invoice with the following data:""")
        request.json["owner_id"] = project_id
        request.json["payment_status"] = payment_status.DUE
        request.json["document_type"] = document_type.INVOICE
        logging.info(request.json)

        new_invoice = invoice_service.create_invoice(request_body=request.json)

        db.session.add(new_invoice)
        db.session.commit()
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/invoices/" + str(new_invoice.id)
        return response
    elif request.method == "GET":
        invs = invoice_service.get_all_invoices(owner_id=project_id)
        return jsonify([row.__getstate__() for row in invs])


@bp.route("/<int:invoice_id>", methods=("GET", "PUT", "DELETE"))
def invoice(project_id, invoice_id):
    invoice = invoice_service.get_invoice_by_id(invoice_id=invoice_id, owner_id=project_id)
    if request.method == "GET":
        return jsonify(invoice.__getstate__())
