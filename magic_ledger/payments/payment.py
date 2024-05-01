from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from magic_ledger import db
from magic_ledger.misc.currency import Currency
from magic_ledger.payments import payment_status


@dataclass
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    payment_status = db.Column(db.String(4), nullable=False)
    payment_type = db.Column(db.String(10), nullable=False)
    currency = db.Column(db.String(25), nullable=False)
    amount_due = db.Column(db.Float, nullable=False)
    amount_paid = db.Column(db.Float, nullable=False)
    pending_amount = db.Column(db.Float, nullable=False)
    invoice_id = db.Column(db.Integer, db.ForeignKey("invoice.id"), nullable=True)
    transaction_id = db.Column(
        db.Integer, db.ForeignKey("transaction.id"), nullable=True
    )

    def __init__(
        self,
        owner_id,
        payment_date,
        due_date,
        payment_status,
        payment_type,
        currency,
        amount_due,
        amount_paid=0.00,
        invoice_id=None,
        transaction_id=None,
    ):
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.payment_date = datetime.strptime(payment_date, "%Y-%m-%d")
        self.owner_id = owner_id
        self.amount_due = round(float(amount_due), 2)
        self.amount_paid = round(float(amount_paid), 2)
        self.pending_amount = self.amount_due - self.amount_paid
        self.payment_status = payment_status
        self.currency = currency
        self.invoice_id = invoice_id
        self.transaction_id = transaction_id
        self.payment_type = payment_type

    def deposit_payment(self, amount):
        self.amount_paid += amount
        self.pending_amount -= amount
        if self.pending_amount <= 0:
            self.payment_status = payment_status.PAID

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]
        state["due_date"] = state["due_date"].strftime("%Y-%m-%d")
        return state

    def __repr__(self):
        return str(self.__getstate__())
