import logging

from flask import request


import magic_ledger.payments.payment_status as payment_status


from flask_restx import Namespace, Resource

from magic_ledger.payments import payment_service
from magic_ledger.payments.api_model import payment_model_input, payment_model_output

ns = Namespace(
    "payments",
    path="/<project_id>/payments/",
    description="An api that allows the user to manage a project's payments",
)


@ns.route("/")
class Payments(Resource):
    @ns.expect(payment_model_input)
    @ns.response(201, "Payment created successfully")
    def post(self, project_id):
        logging.info("""Creating a payment with the following data:""")
        request.json["owner_id"] = project_id
        request.json["payment_status"] = payment_status.DUE
        logging.info(request.json)
        inventory = payment_service.create_payment(request.json)
        return (
            {},
            201,
            {"location": "/" + project_id + "/invoices/" + str(inventory.id)},
        )

    @ns.marshal_list_with(payment_model_output, code=200)
    def get(self, project_id):
        return payment_service.get_all_payments(owner_id=project_id), 200


@ns.route("/<payment_id>/")
class Payment(Resource):
    @ns.marshal_with(payment_model_output)
    def get(self, payment_id, project_id):
        return payment_service.get_payment_by_id(payment_id, owner_id=project_id)


@ns.route("/<payment_id>/pay/")
class SolvePayment(Resource):
    def put(self, payment_id, project_id):
        payment_service.deposit_payment(
            payment_id, owner_id=project_id, request_body=request.json
        )
        return {}, 204


@ns.route("/<payment_date>/receivable/")
class Receivable(Resource):
    @ns.marshal_list_with(payment_model_output, code=200)
    def get(self, project_id, payment_date):
        return (
            payment_service.get_all_receivable_payments_by_date(
                payment_date=payment_date, owner_id=project_id
            ),
            200,
        )


@ns.route("/<payment_date>/payable/")
class Payable(Resource):
    @ns.marshal_list_with(payment_model_output, code=200)
    def get(self, project_id, payment_date):
        return (
            payment_service.get_all_payable_payments_by_date(
                payment_date=payment_date, owner_id=project_id
            ),
            200,
        )


@ns.route("/available-dates/")
class AvailablePaymentDates(Resource):
    def get(self, project_id):
        return payment_service.get_available_payment_dates(owner_id=project_id)
