from magic_ledger.payments.installment import Installment
from magic_ledger.payments.payment import Payment
from datetime import datetime

from magic_ledger import db
from magic_ledger.payments import payment_type, payment_status
from magic_ledger.invoices.invoice import Invoice
from sqlalchemy.sql import extract
from sqlalchemy import and_

from magic_ledger.transactions.transaction import Transaction


def create_payment(request_body):
    payment_data = {
        k: request_body[k]
        for k in (
            "owner_id",
            "due_date",
            "payment_date",
            "payment_status",
            "payment_type",
            "currency",
            "amount_due",
        )
    }
    if "amount_paid" in request_body.keys():
        payment_data["amount_paid"] = request_body["amount_paid"]
    if "invoice_id" in request_body.keys():
        payment_data["invoice_id"] = request_body["invoice_id"]
    if "transaction_id" in request_body.keys():
        payment_data["transaction_id"] = request_body["transaction_id"]
    new_payment = Payment(**payment_data)
    db.session.add(new_payment)
    db.session.commit()
    return new_payment


def get_all_payments(owner_id):
    pmts = Payment.query.filter_by(owner_id=owner_id).all()
    for pmt in pmts:
        if pmt.invoice_id is not None:
            inv = Invoice.query.filter_by(id=pmt.invoice_id).first()
            pmt.details = inv.serial_number
        elif pmt.transaction_id is not None:
            txn = Transaction.query.filter_by(id=pmt.transaction_id).first()
            pmt.details = txn.name
        else:
            pmt.details = "Fără detalii"
    print(pmts)
    return pmts


def get_payment_by_id(payment_id, owner_id):
    return Payment.query.filter_by(id=payment_id, owner_id=owner_id).first()


def deposit_payment(invoice_id, owner_id, request_body):
    payment = Payment.query.filter_by(
        id=invoice_id,
        owner_id=owner_id,
        payment_status=payment_status.DUE,
    ).first()
    installment = Installment(
        payment_id=payment.id,
        amount=request_body["amount"],
        installment_type=request_body["installment_type"],
    )
    db.session.add(installment)
    db.session.commit()
    payment.deposit_payment(request_body["amount"])

    db.session.commit()
    return payment


def get_all_receivable_payments_by_date(owner_id, payment_date):
    pmt_dt = datetime.strptime(payment_date, "%Y-%m")

    pmts = (
        db.session.query(Payment)
        .filter(
            and_(
                Payment.owner_id == owner_id,
                Payment.payment_type == payment_type.RECEIVABLE,
                Payment.payment_status == payment_status.DUE,
                extract("month", Payment.payment_date) == pmt_dt.month,
                extract("year", Payment.payment_date) == pmt_dt.year,
            )
        )
        .order_by(Payment.payment_date)
        .all()
    )
    for pmt in pmts:
        if pmt.invoice_id is not None:
            inv = Invoice.query.filter_by(id=pmt.invoice_id).first()
            pmt.details = "Factura " + inv.serial_number
        elif pmt.transaction_id is not None:
            txn = Transaction.query.filter_by(id=pmt.transaction_id).first()
            pmt.details = "Tranzacția " + txn.name
        else:
            pmt.details = "Fără detalii"
    return pmts


def get_all_payable_payments_by_date(owner_id, payment_date):
    pmt_dt = datetime.strptime(payment_date, "%Y-%m")
    pmts = (
        db.session.query(Payment)
        .filter(
            and_(
                Payment.owner_id == owner_id,
                Payment.payment_type == payment_type.PAYABLE,
                Payment.payment_status == payment_status.DUE,
                extract("month", Payment.payment_date) == pmt_dt.month,
                extract("year", Payment.payment_date) == pmt_dt.year,
            )
        )
        .order_by(Payment.payment_date)
        .all()
    )
    for pmt in pmts:
        if pmt.invoice_id is not None:
            inv = Invoice.query.filter_by(id=pmt.invoice_id).first()
            pmt.details = "Factura " + inv.serial_number
        elif pmt.transaction_id is not None:
            txn = Transaction.query.filter_by(id=pmt.transaction_id).first()
            pmt.details = "Tranzacția " + txn.details
        else:
            pmt.details = "Fără detalii"
    return pmts


def get_all_payments_by_date(owner_id, payment_date):
    pmt_dt = datetime.strptime(payment_date, "%Y-%m")
    pmts = (
        db.session.query(Payment)
        .filter(
            and_(
                Payment.owner_id == owner_id,
                extract("month", Payment.payment_date) == pmt_dt.month,
                extract("year", Payment.payment_date) == pmt_dt.year,
            )
        )
        .order_by(Payment.payment_date)
        .all()
    )
    for pmt in pmts:
        if pmt.invoice_id not in (None, -1):
            inv = Invoice.query.filter_by(id=pmt.invoice_id).first()
            pmt.details = "Factura " + inv.serial_number
        elif pmt.transaction_id not in (None, -1):
            txn = Transaction.query.filter_by(id=pmt.transaction_id).first()
            pmt.details = "Tranzacția " + txn.details
        else:
            pmt.details = "Fără detalii"
    return pmts


def get_available_payment_dates(owner_id):
    payments = Payment.query.filter_by(owner_id=owner_id).all()
    res = []
    for payment in payments:
        res.append(payment.payment_date.strftime("%Y-%m"))
    return list(set(res))


def get_payments_journal(owner_id, journal_date):
    resp = []
    pmts = get_all_payments_by_date(owner_id, journal_date)
    for pmt in pmts:
        installments = Installment.query.filter_by(payment_id=pmt.id).all()
        for inst in installments:
            resp.append(
                {
                    "payment_date": pmt.payment_date,
                    "payment_type": pmt.payment_type,
                    "installment_type": inst.installment_type,
                    "details": pmt.details,
                    "amount": inst.amount,
                    "currency": pmt.currency,
                }
            )
    return resp
