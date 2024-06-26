from datetime import datetime

from magic_ledger import db
from magic_ledger.invoices import invoice_type, client_types
from magic_ledger.invoices.invoice import Invoice
from sqlalchemy.sql import extract
from sqlalchemy import and_

from magic_ledger.payments.payment_service import create_payment
from magic_ledger.third_parties.service import organization_service, agent_service


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
    if "client_type" in request_body:
        invoice_data["client_type"] = request_body["client_type"]
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
    invs = Invoice.query.filter_by(owner_id=owner_id).all()
    for inv in invs:
        if inv.client_type == client_types.ORGANIZATION:
            cli = organization_service.get_organization_by_id(inv.client_id, owner_id)
            inv.client_name = cli.organization_name
            inv.cli_nrc = cli.nrc
        elif inv.client_type == client_types.PERSON:
            cli = agent_service.get_agent_by_id(inv.client_id, owner_id)
            inv.client_name = cli.agent_name + " " + cli.last_name
            inv.cli_nrc = cli.cnp

        sup = organization_service.get_organization_by_id(inv.supplier_id, owner_id)
        inv.supplier_name = sup.organization_name
        inv.sup_nrc = sup.nrc
    return invs


def get_invoice_by_id(invoice_id, owner_id):
    return Invoice.query.filter_by(id=invoice_id, owner_id=owner_id).first()


def get_all_outgoing_invoices_by_date(owner_id, invoice_date):
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


def get_all_incoming_invoices_by_date(owner_id, invoice_date):
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


def get_all_invoices_by_date(owner_id, invoice_date):
    inv_date = datetime.strptime(invoice_date, "%Y-%m")
    invs = (
        db.session.query(Invoice)
        .filter(
            and_(
                Invoice.owner_id == owner_id,
                extract("month", Invoice.invoice_date) == inv_date.month,
                extract("year", Invoice.invoice_date) == inv_date.year,
            )
        )
        .order_by(Invoice.invoice_date)
        .all()
    )
    for inv in invs:
        if inv.client_type == client_types.ORGANIZATION:
            cli = organization_service.get_organization_by_id(inv.client_id, owner_id)
            inv.client_name = cli.organization_name
            inv.cli_nrc = cli.nrc
        elif inv.client_type == client_types.PERSON:
            cli = agent_service.get_agent_by_id(inv.client_id, owner_id)
            inv.client_name = cli.agent_name + " " + cli.last_name
            inv.cli_nrc = cli.cnp

        sup = organization_service.get_organization_by_id(inv.supplier_id, owner_id)
        inv.supplier_name = sup.organization_name
        inv.sup_nrc = sup.nrc
    return invs


def get_invoice_dates(owner_id):
    invoices = Invoice.query.filter_by(owner_id=owner_id).all()
    res = []
    for inv in invoices:
        res.append(inv.invoice_date.strftime("%Y-%m"))
    return list(set(res))
