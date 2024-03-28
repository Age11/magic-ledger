import logging

from flask import jsonify, request


from magic_ledger.inventory.api_model import inventory_model_output
from magic_ledger.invoices import invoice_service
from magic_ledger.invoices.api_model import invoice_model_input, invoice_model_output
import magic_ledger.invoices.document_type as document_type
import magic_ledger.invoices.payment_status as payment_status


from flask_restx import Namespace, Resource

ns = Namespace(
    "invoice",
    path="/<project_id>/invoices/",
    description="An api that allows the user to manage a project's invoices",
)


@ns.route("/")
class Invoices(Resource):
    @ns.expect(invoice_model_input)
    @ns.response(201, "Invoice created successfully")
    def post(self, project_id):
        logging.info("""Creating an invoice with the following data:""")
        request.json["owner_id"] = project_id
        request.json["payment_status"] = payment_status.DUE
        logging.info(request.json)
        inventory = invoice_service.create_invoice(request.json)
        return (
            {},
            201,
            {"location": "/" + project_id + "/invoices/" + str(inventory.id)},
        )

    @ns.marshal_list_with(invoice_model_output, code=200)
    def get(self, project_id):
        return invoice_service.get_all_invoices(owner_id=project_id), 200


@ns.route("/<invoice_id>/", endpoint="invoice_items")
class InvoiceById(Resource):
    @ns.marshal_list_with(inventory_model_output, code=200)
    def get(self, project_id, invoice_id):
        return (
            invoice_service.get_invoice_by_id(
                invoice_id=invoice_id, owner_id=project_id
            ),
            200,
        )
