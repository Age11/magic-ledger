from flask_restx import fields
from magic_ledger.extensions import api


transaction_model_input = api.model(
    "transaction_input",
    {
        "debit_account": fields.String(
            required=True, description="The transaction debit account"
        ),
        "credit_account": fields.String(
            required=True, description="The transaction credit account"
        ),
        "debit_amount": fields.Float(
            required=True, description="The transaction debit amount"
        ),
        "credit_amount": fields.Float(
            required=True, description="The transaction credit amount"
        ),
        "currency": fields.String(
            required=True, description="The transaction currency"
        ),
        "transaction_date": fields.Date(
            required=True, description="The transaction date"
        ),
        "details": fields.String(required=True, description="The transaction details"),
        "owner_id": fields.Integer(
            required=True, description="The transaction owner id"
        ),
        "tx_type": fields.String(required=True, description="The transaction type"),
        "invoice_id": fields.Integer(
            required=False, description="The transaction invoice id"
        ),
    },
)

transaction_model_output = api.model(
    "transaction_output",
    {
        "id": fields.Integer(required=True, description="The transaction id"),
        "debit_account": fields.String(
            required=True, description="The transaction debit account"
        ),
        "credit_account": fields.String(
            required=True, description="The transaction credit account"
        ),
        "debit_amount": fields.Float(
            required=True, description="The transaction debit amount"
        ),
        "credit_amount": fields.Float(
            required=True, description="The transaction credit amount"
        ),
        "currency": fields.String(
            required=True, description="The transaction currency"
        ),
        "transaction_date": fields.Date(
            required=True, description="The transaction date"
        ),
        "details": fields.String(required=True, description="The transaction details"),
        "owner_id": fields.Integer(
            required=True, description="The transaction owner id"
        ),
        "tx_type": fields.String(required=True, description="The transaction type"),
        "invoice_id": fields.Raw(
            required=False, description="The transaction invoice id or None"
        ),
    },
)
