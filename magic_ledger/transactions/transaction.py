from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from magic_ledger import db
from magic_ledger.misc.currency import Currency


@dataclass
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    debit_account_id = db.Column(
        db.String(255), db.ForeignKey("account_plan.account"), nullable=False
    )
    credit_account_id = db.Column(
        db.String(255), db.ForeignKey("account_plan.account"), nullable=False
    )
    debit_amount = db.Column(db.Float, nullable=False)
    credit_amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.Enum(Currency), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    recorded_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    organization_id = db.Column(
        db.Integer, db.ForeignKey("organization.id"), nullable=False
    )
    details = db.Column(db.String(255), nullable=False)

    def __init__(
        self,
        debit_account_id,
        credit_account_id,
        debit_amount,
        credit_amount,
        currency,
        transaction_date,
        organization_id,
        details,
    ):
        self.debit_account_id = debit_account_id
        self.credit_account_id = credit_account_id
        self.debit_amount = debit_amount
        self.credit_amount = credit_amount
        self.currency = Currency[currency]
        self.transaction_date = datetime.strptime(transaction_date, "%Y-%m-%d")
        self.organization_id = organization_id
        self.details = details

    def __getstate__(self):
        state = self.__dict__.copy()
        state["currency"] = state["currency"].name
        del state["_sa_instance_state"]

        return state

    def __repr__(self):
        return str(self.__getstate__())
