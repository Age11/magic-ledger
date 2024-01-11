from flask_restx import fields
from magic_ledger.extensions import api
from magic_ledger.invoices import payment_status, document_type

invoice_model_input = api.model(
    "invoice_input",
    {
        "name": fields.String(required=True, description="The invoice name"),
        "description": fields.String(
            required=True, description="The invoice description"
        ),
        "payment_status": fields.String(
            required=True,
            description="The invoice payment status",
            enum=[payment_status.PAID, payment_status.DUE],
        ),
        "document_type": fields.String(
            required=True,
            description="The invoice document type",
            enum=[document_type.INVOICE],
        ),
        "owner_id": fields.Integer(required=True, description="The invoice owner id"),
    },
)

invoice_model_output = api.model(
    "invoice_output",
    {
        "id": fields.Integer(required=True, description="The invoice id"),
        "name": fields.String(required=True, description="The invoice name"),
        "description": fields.String(
            required=True, description="The invoice description"
        ),
        "payment_status": fields.String(
            required=True,
            description="The invoice payment status",
            enum=[payment_status.PAID, payment_status.DUE],
        ),
        "document_type": fields.String(
            required=True,
            description="The invoice document type",
            enum=[document_type.INVOICE],
        ),
        "owner_id": fields.Integer(required=True, description="The invoice owner id"),
    },
)
