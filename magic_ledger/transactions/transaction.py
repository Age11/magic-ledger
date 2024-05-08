from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from magic_ledger import db


@dataclass
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    debit_account = db.Column(
        db.String(255), db.ForeignKey("account_plan.account"), nullable=False
    )
    credit_account = db.Column(
        db.String(255), db.ForeignKey("account_plan.account"), nullable=False
    )
    debit_amount = db.Column(db.Float, nullable=False)
    credit_amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(20), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    recorded_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    details = db.Column(db.String(255), nullable=False)
    tx_type = db.Column(db.String(255), nullable=False)

    document_type = db.Column(db.String(255), nullable=True)
    document_serial_number = db.Column(db.String(255), nullable=True)
    document_id = db.Column(db.Integer, nullable=True)

    def __init__(
        self,
        debit_account,
        credit_account,
        debit_amount,
        credit_amount,
        currency,
        transaction_date,
        owner_id,
        details,
        tx_type,
        document_type=None,
        document_serial_number=None,
        document_id=None,
    ):
        self.debit_account = debit_account
        self.credit_account = credit_account
        self.debit_amount = round(float(debit_amount), 2)
        self.credit_amount = round(float(credit_amount), 2)
        self.currency = currency
        self.transaction_date = datetime.strptime(transaction_date, "%Y-%m-%d")
        self.owner_id = owner_id
        self.details = details
        self.tx_type = tx_type

        self.document_type = document_type
        self.document_serial_number = document_serial_number
        self.document_id = document_id

    def __getstate__(self):
        state = self.__dict__.copy()
        state["transaction_date"] = state["transaction_date"].strftime("%Y-%m-%d")
        state["recorded_date"] = state["recorded_date"].strftime("%Y-%m-%d")

        del state["_sa_instance_state"]

        return state

    def __repr__(self):
        return str(self.__getstate__())
