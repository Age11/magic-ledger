from magic_ledger.transactions import transaction_service
from magic_ledger.transactions.api_model import (
    transaction_model_input,
    transaction_model_output,
)

import logging
from flask import request
from flask_restx import Namespace, Resource

ns = Namespace(
    "transaction",
    path="/<project_id>/transactions/",
    description="An api that allows the user to manage a project's transactions",
)


@ns.route("/")
class Transactions(Resource):
    @ns.expect(transaction_model_input)
    @ns.response(201, "Transaction created successfully")
    def post(self, project_id):
        logging.info("""Creating an transaction with the following data:""")
        request.json["owner_id"] = project_id
        logging.info(request.json)
        transaction = transaction_service.create_transaction_and_update_balance(
            request.json
        )
        return (
            {},
            201,
            {"location": "/" + project_id + "/transactions/" + str(transaction.id)},
        )

    @ns.marshal_list_with(transaction_model_output, code=200)
    def get(self, project_id):
        return transaction_service.get_all_transactions(owner_id=project_id), 200


@ns.route("/<transaction_id>/", endpoint="transaction")
class TransactionById(Resource):
    @ns.marshal_with(transaction_model_output, code=200)
    def get(self, project_id, transaction_id):
        return (
            transaction_service.get_transaction_by_id(
                transaction_id=transaction_id, owner_id=project_id
            ),
            200,
        )
