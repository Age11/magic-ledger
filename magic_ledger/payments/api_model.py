from flask_restx import fields
from magic_ledger.extensions import api
from magic_ledger.payments import payment_status, payment_type


payment_model_output = api.model(
    "payment_output",
    {
        "id": fields.Integer(required=True, description="The payment id"),
        "owner_id": fields.Integer(required=True, description="The payment owner id"),
        "payment_date": fields.Date(required=True, description="The payment due date"),
        "due_date": fields.Date(required=True, description="The payment due date"),
        "payment_status": fields.String(
            required=True, description="The payment status"
        ),
        "payment_type": fields.String(required=True, description="The payment type"),
        "details": fields.String(required=True, description="The payment details"),
        "currency": fields.String(required=True, description="The payment currency"),
        "amount_paid": fields.Float(required=True, description="The paid amount"),
        "amount_due": fields.Float(required=True, description="The due amount"),
        "pending_amount": fields.Float(required=True, description="The current debt"),
        "invoice_id": fields.Integer(
            required=True, description="The payment invoice id"
        ),
        "transaction_id": fields.Integer(
            required=True, description="The payment transaction id"
        ),
    },
)


payment_model_input = api.model(
    "payment_input",
    {
        "id": fields.Integer(required=True, description="The payment id"),
        "owner_id": fields.Integer(required=True, description="The payment owner id"),
        "payment_date": fields.Date(required=True, description="The payment due date"),
        "due_date": fields.Date(required=True, description="The payment due date"),
        "payment_status": fields.String(
            enum=[payment_status.DUE, payment_status.PAID],
            required=True,
            description="The payment status",
        ),
        "payment_type": fields.String(
            required=True,
            enum=[payment_type.PAYABLE, payment_type.RECEIVABLE],
            description="The payment type",
        ),
        "currency": fields.String(required=True, description="The paid currency"),
        "amount_due": fields.Float(required=True, description="The due amount"),
        "amount_paid": fields.Float(required=True, description="The payment amount"),
        "invoice_id": fields.Integer(
            required=True, description="The payment invoice id"
        ),
        "transaction_id": fields.Integer(
            required=True, description="The payment transaction id"
        ),
    },
)
