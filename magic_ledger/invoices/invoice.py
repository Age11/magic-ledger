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
    owner_id = db.Column(
        db.Integer, db.ForeignKey("project.id"), nullable=False
    )
    serial_number = db.Column(db.String(255), nullable=False)
    issuer_name = db.Column(db.String(255))

    issue_date = db.Column(db.DateTime)
    receive_date = db.Column(db.DateTime, nullable=False)

    due_date = db.Column(db.DateTime, nullable=False)
    payment_status = db.Column(db.Enum(PaymentStatus), nullable=False)

    supplier_id = db.Column(db.Integer, db.ForeignKey("organization.id"))
    client_id = db.Column(db.Integer, db.ForeignKey("organization.id"), nullable=False)

    currency = db.Column(db.Enum(Currency), nullable=False)

    value = db.Column(db.Float, nullable=False)
    vat_amount = db.Column(db.Float, nullable=False)
    total_value = db.Column(db.Float, nullable=False)

    def __init__(
            self,
            inv_type,
            serial_number,
            receive_date,
            due_date,
            issue_date,
            payment_status,
            owner_id,
            supplier_id,
            client_id,
            currency,
            issuer_name,
            value=0,
            vat_amount=0,

    ):
        self.inv_type = inv_type
        self.serial_number = serial_number
        self.receive_date = datetime.strptime(receive_date, "%Y-%m-%d")
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.issue_date = datetime.strptime(issue_date, "%Y-%m-%d")
        self.owner_id = owner_id
        self.supplier_id = supplier_id
        self.client_id = client_id
        self.issuer_name = issuer_name

        self.value = value
        self.vat_amount = vat_amount
        self.total_value = self.value + self.vat_amount

        if payment_status == "paid":
            self.payment_status = PaymentStatus.PAID
        elif payment_status == "due":
            self.payment_status = PaymentStatus.DUE

        if currency == "RON":
            self.currency = Currency.RON
        elif currency == "EUR":
            self.currency = Currency.EUR

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]
        if state["payment_status"] == PaymentStatus.PAID:
            state["payment_status"] = "paid"
        elif state["payment_status"] == PaymentStatus.DUE:
            state["payment_status"] = "due"

        if state["currency"] == Currency.RON:
            state["currency"] = "RON"
        elif state["currency"] == Currency.EUR:
            state["currency"] = "EUR"

        state["receive_date"] = state["receive_date"].strftime("%Y-%m-%d")
        state["due_date"] = state["due_date"].strftime("%Y-%m-%d")
        state["issue_date"] = state["issue_date"].strftime("%Y-%m-%d")

        return state

    def __repr__(self):
        return str(self.__getstate__())
