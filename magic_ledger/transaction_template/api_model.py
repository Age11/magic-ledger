from flask_restx import Namespace, fields, Model
from magic_ledger.extensions import api

TGT_main_transaction_model = api.model(
    "Transaction",
    {
        "debit_account": fields.String(
            required=True, description="Debit account number"
        ),
        "credit_account": fields.String(
            required=True, description="Credit account number"
        ),
        "currency": fields.String(required=False, description="Transaction currency"),
        "details": fields.String(required=True, description="Transaction details"),
        "tx_type": fields.String(required=True, description="Transaction type"),
    },
)

TGT_followup_transaction_model = api.model(
    "FollowupTransaction",
    {
        "debit_account": fields.String(
            required=True, description="Debit account number"
        ),
        "credit_account": fields.String(
            required=True, description="Credit account number"
        ),
        "operation": fields.String(
            required=False,
            description="Operation performed in the transaction",
            pattern="""^[*/%+\-]\-?\d*\.?\d+([*/%+\-]\-?\d*\.?\d+)*$""",
        ),
        "details": fields.String(required=True, description="Transaction details"),
        "tx_type": fields.String(required=True, description="Transaction type"),
    },
)


transaction_group_template_model = api.model(
    "TransactionGroupTemplate",
    {
        "id": fields.Integer(required=True, description="Template ID"),
        "name": fields.String(required=True, description="Template name"),
        "description": fields.String(required=True, description="Template description"),
        "main_transaction": fields.Nested(
            TGT_main_transaction_model, description="Main transaction details"
        ),
        "followup_transactions": fields.List(
            fields.Nested(TGT_followup_transaction_model),
            description="Follow-up transactions details",
        ),
    },
)


transaction_processor_model = api.model(
    "TransactionProcessor",
    {
        "transaction_group_template_id": fields.Integer(
            required=True, description="Transaction Group Template ID"
        ),
        "transaction_date": fields.String(
            required=True, description="Transaction date"
        ),
        "amount": fields.Float(required=True, description="Transaction amount"),
    },
)
