import logging


from flask import request


from magic_ledger.account_balance.account_balance import AccountBalance
import magic_ledger.account_balance.account_ballance_service as account_balance_service
from magic_ledger.account_balance.api_model import (
    account_balance_entry_model_input,
    account_balance_entry_model_output,
)


from flask_restx import Namespace, Resource

ns = Namespace(
    "account-balance",
    path="/<project_id>/account-balance/",
    description="An api that allows the user to manage the account balance",
)


@ns.route("/")
class AccountBalance(Resource):
    @ns.marshal_list_with(account_balance_entry_model_output, code=200)
    @ns.response(201, "Get account balance")
    def get(self, project_id):
        return account_balance_service.get_account_balances(owner_id=project_id), 200

    @ns.expect(account_balance_entry_model_input)
    @ns.response(201, "Account balance created")
    def post(self, project_id):
        """Create a new account balance entry"""
        logging.info("""adding initial account balance with the following data:""")
        logging.info(request.json)
        for account_balance in request.json:
            account_balance["owner_id"] = project_id
            account_balance_service.update_account_balance(**account_balance)
        return {}, 201


@ns.route("/close/<balance_date>")
class CloseBalance(Resource):
    @ns.response(201, "Accounts closed")
    def post(self, project_id, balance_date):
        """Closing account"""
        logging.info("""closing balance for the following month:""" + balance_date)
        account_balance_service.close_monthly_balance_accounts(
            project_id=project_id, balance_date_string=balance_date
        )
        return {}, 201
