from magic_ledger import db
from magic_ledger.invoices import invoice_type, payment_status
from magic_ledger.invoices.invoice import Invoice


def create_invoice(request_body):
    invoice_data = {
        k: request_body[k]
        for k in (
            "serial_number",
            "invoice_date",
            "due_date",
            "invoice_type",
            "payment_status",
            "owner_id",
            "supplier_id",
            "client_id",
            "currency",
            "amount",
            "vat_amount",
            "issuer_name",
        )
    }
    new_invoice = Invoice(**invoice_data)
    db.session.add(new_invoice)
    db.session.commit()
    return new_invoice


def get_all_invoices(owner_id):
    return Invoice.query.filter_by(owner_id=owner_id).all()


def get_all_payable_invoices(owner_id):
    return Invoice.query.filter_by(
        owner_id=owner_id,
        invoice_type=invoice_type.PAYABLE,
        payment_status=payment_status.DUE,
    ).all()


def get_all_receivable_invoices(owner_id):
    return Invoice.query.filter_by(
        owner_id=owner_id,
        invoice_type=invoice_type.RECEIVABLE,
        payment_status=payment_status.DUE,
    ).all()


def get_invoice_by_id(invoice_id, owner_id):
    return Invoice.query.filter_by(id=invoice_id, owner_id=owner_id).first()


def solve_payment(invoice_id, owner_id):
    invoice = Invoice.query.filter_by(
        id=invoice_id,
        owner_id=owner_id,
        payment_status=payment_status.DUE,
    ).first()
    invoice.payment_status = payment_status.PAID
    db.session.commit()
    return invoice
