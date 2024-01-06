from magic_ledger import db
from magic_ledger.invoices.invoice import Invoice


def create_invoice(request_body):
    invoice_data = {k: request_body[k] for k in (
        "document_type", "serial_number", "receive_date", "issue_date", "due_date", "payment_status", "owner_id",
        "supplier_id", "client_id", "currency", "issuer_name")}
    new_invoice = Invoice(**invoice_data)
    db.session.add(new_invoice)
    db.session.commit()
    return new_invoice

def get_all_invoices(owner_id):
    return Invoice.query.filter_by(owner_id=owner_id).all()

def get_invoice_by_id(invoice_id, owner_id):
    return Invoice.query.filter_by(id=invoice_id, owner_id=owner_id).first()
