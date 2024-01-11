from flask_restx import fields
from magic_ledger.extensions import api

account_plan_entry_model = api.model(
    "account_plan_entry_model",
    {
        "id": fields.Integer(required=True, description="The account id"),
        "account": fields.String(required=True, description="The account name"),
        "acc_name": fields.String(required=True, description="The account name"),
        "acc_type": fields.String(required=True, description="The account type"),
    },
)
