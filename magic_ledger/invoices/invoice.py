from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from magic_ledger import db
from magic_ledger.misc.currency import Currency


class PaymentStatus(Enum):
    PAID = "paid"
    DUE = "due"
    OVERDUE = "overdue"


@dataclass
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    serial_number = db.Column(db.String(255), nullable=False)
    issuer_name = db.Column(db.String(255))
    invoice_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    invoice_type = db.Column(db.String(10), nullable=False)
    payment_status = db.Column(db.String(4), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey("organization.id"))
    client_id = db.Column(db.Integer, db.ForeignKey("organization.id"), nullable=False)
    currency = db.Column(db.String(25), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    vat_amount = db.Column(db.Float, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)

    def __init__(
        self,
        serial_number,
        due_date,
        invoice_date,
        invoice_type,
        payment_status,
        owner_id,
        supplier_id,
        client_id,
        currency,
        issuer_name,
        amount,
        vat_amount,
    ):
        self.serial_number = serial_number
        self.invoice_date = datetime.strptime(invoice_date, "%Y-%m-%d")
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.owner_id = owner_id
        self.supplier_id = supplier_id
        self.client_id = client_id
        self.issuer_name = issuer_name

        self.amount = int(amount)
        self.vat_amount = int(vat_amount)
        self.total_amount = self.amount + self.vat_amount

        self.payment_status = payment_status
        self.invoice_type = invoice_type
        self.currency = currency

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]
        state["invoice_date"] = state["invoice_date"].strftime("%Y-%m-%d")
        state["due_date"] = state["due_date"].strftime("%Y-%m-%d")
        return state

    def __repr__(self):
        return str(self.__getstate__())
