from magic_ledger.account_plan.api_model import account_plan_entry_model
from magic_ledger.account_plan.model import AccountPlan


from flask_restx import Namespace, Resource

ns = Namespace(
    "account-plan",
    path="/account-plan/",
    description="An api that allows the user to manage the account plan",
)


@ns.route("/")
class Transactions(Resource):
    @ns.marshal_list_with(account_plan_entry_model)
    @ns.response(201, "Get account plan")
    def get(self):
        return AccountPlan.query.all()
