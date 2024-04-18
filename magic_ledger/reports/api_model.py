from flask_restx import fields
from magic_ledger.extensions import api

sales_journal_entry = api.model(
    "SalesJournalEntry",
    {
        "date": fields.String,
        "client_name": fields.String,
        "client_vat_code": fields.String,
        "total": fields.Float,
        "amount": fields.Float,
        "vat_amount": fields.Float,
        "regular_amount": fields.Float,
        "regular_vat_amount": fields.Float,
        "reduced_amount": fields.Float,
        "reduced_vat_amount": fields.Float,
        "no_vat_amount": fields.Float,
        "payed": fields.Boolean,
    },
)

purchase_journal_entry = api.model(
    "PurchaseJournalEntry",
    {
        "date": fields.String,
        "supplier_name": fields.String,
        "supplier_vat_code": fields.String,
        "total": fields.Float,
        "amount": fields.Float,
        "vat_amount": fields.Float,
        "regular_amount": fields.Float,
        "regular_vat_amount": fields.Float,
        "reduced_amount": fields.Float,
        "reduced_vat_amount": fields.Float,
        "no_vat_amount": fields.Float,
        "payed": fields.Boolean,
    },
)
