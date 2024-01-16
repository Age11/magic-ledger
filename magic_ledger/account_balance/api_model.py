from flask_restx import fields
from magic_ledger.extensions import api

account_balance_entry_model_input = api.model(
    "account_balance_entry_model_input",
    {
        "analytical_account": fields.String(
            required=True, description="The account name"
        ),
        "owner_id": fields.Integer(required=True, description="The account owner id"),
        "balance_date": fields.String(
            required=True, description="The account balance date"
        ),
    },
)

account_balance_entry_model_output = api.model(
    "account_balance_entry_model_output",
    {
        "id": fields.Integer(required=True, description="The account id"),
        "analytical_account": fields.String(
            required=True, description="The account name"
        ),
        "initial_debit": fields.Float(
            required=True, description="The account initial debit"
        ),
        "initial_credit": fields.Float(
            required=True, description="The account initial credit"
        ),
        "cumulated_debit": fields.Float(
            required=True, description="The account cumulated debit"
        ),
        "cumulated_credit": fields.Float(
            required=True, description="The account cumulated credit"
        ),
        "current_turnover_debit": fields.Float(
            required=True, description="The account current turnover debit"
        ),
        "current_turnover_credit": fields.Float(
            required=True, description="The account current turnover credit"
        ),
        "total_debit_balance": fields.Float(
            required=True, description="The account total debit balance"
        ),
        "total_credit_balance": fields.Float(
            required=True, description="The account total credit balance"
        ),
        "final_debit_balance": fields.Float(
            required=True, description="The account final debit balance"
        ),
        "final_credit_balance": fields.Float(
            required=True, description="The account final credit balance"
        ),
        "owner_id": fields.Integer(required=True, description="The account owner id"),
        "balance_date": fields.String(
            required=True, description="The account balance date"
        ),
        "processed": fields.Boolean(
            required=True, description="The current entry processed status"
        ),
    },
)
