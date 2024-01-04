from __future__ import annotations

from dataclasses import dataclass
from magic_ledger import db

from datetime import datetime
from magic_ledger.misc.currency import Currency

@dataclass
class Loans(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    owner_id = db.Column(
        db.Integer, db.ForeignKey("project.id"), nullable=False
    )

    currency_type = db.Column(db.Enum(Currency), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    interest = db.Column(db.Float, nullable=False)
    interest_payment_type = db.Column(db.String(255), nullable=False)

    loan_analytical_account = db.Column(db.String(255), foreign_key="account_plan.account", nullable=False)
    interest_analytical_account = db.Column(db.String(255), foreign_key="account_plan.account", nullable=False)

    term = db.Column(db.DateTime, nullable=False)

    def __init__(
            self,
            owner_id,
            currency_type,
            amount,
            interest,
            interest_payment_type,
            loan_analytical_account,
            interest_analytical_account,
            start_date,
            term
    ):
        self.owner_id = owner_id
        self.currency_type = Currency[currency_type]
        self.amount = amount
        self.interest = interest
        self.paid_interest = 0
        self.interest_payment_type = interest_payment_type
        self.loan_analytical_account = loan_analytical_account
        self.interest_analytical_account = interest_analytical_account
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.term = datetime.strptime(term, "%Y-%m-%d")

    def __getstate__(self):
        state = self.__dict__.copy()
        state["currency_type"] = state["currency_type"].value
        state["start_date"] = state["start_date"].strftime("%Y-%m-%d")
        state["term"] = state["term"].strftime("%Y-%m-%d")

        del state["_sa_instance_state"]
        return state

    def __repr__(self):
        return str(self.__getstate__())
