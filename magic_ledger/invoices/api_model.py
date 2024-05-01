from flask_restx import fields
from magic_ledger.extensions import api
from magic_ledger.invoices import invoice_type
from magic_ledger.payments import payment_status, payment_type

invoice_model_output = api.model(
    "invoice_input",
    {
        "id": fields.Integer(required=True, description="The invoice id"),
        "serial_number": fields.String(required=True, description="The invoice name"),
        "invoice_date": fields.Date(required=True, description="The invoice date"),
        "invoice_type": fields.String(
            required=True,
            description="The invoice type",
            enum=[invoice_type.OUTGOING, invoice_type.INCOMING],
        ),
        "supplier_id": fields.Integer(
            required=True, description="The invoice supplier id"
        ),
        "client_id": fields.Integer(required=True, description="The invoice client id"),
        "amount": fields.Float(required=True, description="The invoice amount"),
        "vat_amount": fields.Float(required=True, description="The invoice vat amount"),
        "total_amount": fields.Float(
            required=True, description="The invoice total amount"
        ),
        "currency": fields.String(required=True, description="The invoice currency"),
        "issuer_name": fields.String(
            required=True, description="The invoice issuer name"
        ),
        "owner_id": fields.Integer(required=True, description="The invoice owner id"),
    },
)

invoice_model_input = api.model(
    "invoice_input",
    {
        "serial_number": fields.String(required=True, description="The invoice name"),
        "invoice_date": fields.Date(required=True, description="The invoice date"),
        "due_date": fields.Date(required=True, description="The invoice due date"),
        "payment_status": fields.String(
            required=True,
            description="The invoice payment status",
            enum=[payment_status.PAID, payment_status.DUE],
        ),
        "invoice_type": fields.String(
            required=True,
            description="The invoice type",
            enum=[invoice_type.INCOMING, invoice_type.OUTGOING],
        ),
        "supplier_id": fields.Integer(
            required=True, description="The invoice supplier id"
        ),
        "client_id": fields.Integer(required=True, description="The invoice client id"),
        "amount": fields.Float(required=True, description="The invoice amount"),
        "vat_amount": fields.Float(required=True, description="The invoice vat amount"),
        "currency": fields.String(required=True, description="The invoice currency"),
        "issuer_name": fields.String(
            required=True, description="The invoice issuer name"
        ),
        "owner_id": fields.Integer(required=True, description="The invoice owner id"),
    },
)
