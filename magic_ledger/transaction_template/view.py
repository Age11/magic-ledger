from magic_ledger.transaction_template.api_model import (
    transaction_group_template_model,
    transaction_processor_model,
)
from magic_ledger.transaction_template.transaction_group_template_service import (
    create_transaction_group_template,
    retrieve_all_transaction_group_templates,
    generate_transactions_from_template,
    retrieve_all_transaction_group_templates_by_type,
    transaction_group_templates_by_type,
)

import logging
from flask import request
from flask_restx import Namespace, Resource

from magic_ledger.transactions.api_model import transaction_model_output

ns = Namespace(
    "transaction-group-templates",
    path="/<project_id>/transaction-group-templates/",
    description="An api that allows the user to manage transaction templates",
)


@ns.route("/")
class GroupTransactionTemplate(Resource):
    @ns.expect(transaction_group_template_model)
    @ns.response(201, "Transaction created successfully")
    def post(self, project_id):
        logging.info("""Creating an transaction with the following data:""")
        create_transaction_group_template(request.json, project_id)
        return (
            {},
            201,
        )

    @ns.response(200, "Transaction templates retrieved successfully")
    @ns.marshal_list_with(transaction_group_template_model, code=200)
    def get(self, project_id):
        return (retrieve_all_transaction_group_templates(project_id), 200)


@ns.route("/<tx_type>")
class GroupTransactionTemplateByType(Resource):
    @ns.response(200, "Transaction templates retrieved successfully by type")
    @ns.marshal_list_with(transaction_group_template_model, code=200)
    def get(self, project_id, tx_type):
        return (
            retrieve_all_transaction_group_templates_by_type(project_id, tx_type),
            200,
        )


@ns.route("/by-type")
class GroupTransactionTemplateByType(Resource):
    @ns.response(200, "Transaction templates retrieved successfully by type")
    @ns.marshal_list_with(transaction_group_template_model, code=200)
    def get(self, project_id):
        return (
            transaction_group_templates_by_type(project_id, request.json["tx_type"]),
            200,
        )


@ns.route(
    "/<transaction_group_template_id>/use-template",
    endpoint="transaction-group-templates",
)
class TransactionProcessor(Resource):
    @ns.expect(transaction_processor_model)
    @ns.marshal_list_with(transaction_model_output, code=200)
    @ns.response(201, "Transactions created successfully")
    def post(self, project_id, transaction_group_template_id):
        logging.info("""Creating a transaction with the following data:""")
        return (
            generate_transactions_from_template(
                transaction_group_template_id, project_id, request.json
            ),
            201,
        )
