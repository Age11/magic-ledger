from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from magic_ledger import db
from magic_ledger.misc.currency import Currency
from magic_ledger.payments import payment_status


@dataclass
class Installment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    payment_id = db.Column(db.Integer, db.ForeignKey("payment.id"), nullable=False)
    installment_type = db.Column(db.String(10), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def __init__(
        self,
        payment_id,
        installment_type,
        amount,
    ):
        self.payment_id = payment_id
        self.installment_type = installment_type
        self.amount = round(float(amount), 2)
