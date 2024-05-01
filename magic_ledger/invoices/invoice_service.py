from datetime import datetime

from magic_ledger import db
from magic_ledger.invoices import invoice_type
from magic_ledger.payments import payment_type, payment_status
from magic_ledger.invoices.invoice import Invoice
from sqlalchemy.sql import extract
from sqlalchemy import and_

from magic_ledger.payments.payment_service import create_payment


def create_invoice(request_body):
    invoice_data = {
        k: request_body[k]
        for k in (
            "serial_number",
            "invoice_date",
            "owner_id",
            "supplier_id",
            "client_id",
            "amount",
            "vat_amount",
            "currency",
            "issuer_name",
            "invoice_type",
        )
    }
    new_invoice = Invoice(**invoice_data)
    db.session.add(new_invoice)
    db.session.commit()
    payment_data = {
        k: request_body[k]
        for k in (
            "owner_id",
            "due_date",
            "payment_status",
            "payment_type",
            "currency",
            "amount_due",
        )
    }
    payment_data["invoice_id"] = new_invoice.id
    payment_data["payment_date"] = new_invoice.invoice_date.strftime("%Y-%m-%d")
    create_payment(payment_data)
    return new_invoice


def get_all_invoices(owner_id):
    return Invoice.query.filter_by(owner_id=owner_id).all()


def get_invoice_by_id(invoice_id, owner_id):
    return Invoice.query.filter_by(id=invoice_id, owner_id=owner_id).first()


def get_all_receivable_invoices_by_date(owner_id, invoice_date):
    inv_date = datetime.strptime(invoice_date, "%Y-%m")
    return (
        db.session.query(Invoice)
        .filter(
            and_(
                Invoice.owner_id == owner_id,
                Invoice.invoice_type == invoice_type.OUTGOING,
                extract("month", Invoice.invoice_date) == inv_date.month,
                extract("year", Invoice.invoice_date) == inv_date.year,
            )
        )
        .order_by(Invoice.invoice_date)
        .all()
    )


def get_all_payable_invoices_by_date(owner_id, invoice_date):
    inv_date = datetime.strptime(invoice_date, "%Y-%m")
    return (
        db.session.query(Invoice)
        .filter(
            and_(
                Invoice.owner_id == owner_id,
                Invoice.invoice_type == invoice_type.INCOMING,
                extract("month", Invoice.invoice_date) == inv_date.month,
                extract("year", Invoice.invoice_date) == inv_date.year,
            )
        )
        .order_by(Invoice.invoice_date)
        .all()
    )
