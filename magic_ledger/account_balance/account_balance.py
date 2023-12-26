from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from magic_ledger import db


@dataclass
class AccountBalance(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    analytical_account = db.Column(db.String(255), foreign_key="account_plan.account", nullable=False)
    initial_debit = db.Column(db.Float, nullable=False)
    initial_credit = db.Column(db.Float, nullable=False)
    debit = db.Column(db.Float, nullable=False)
    credit = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    calculated_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(
        self,
        analytical_account,
        owner_id,
    ):
        self.analytical_account = analytical_account
        self.initial_debit = 0
        self.initial_credit = 0
        self.owner_id = owner_id
        self.debit = 0
        self.credit = 0

    def update_current_debit(self, amount):
        self.debit += amount

    def update_current_credit(self, amount):
        self.credit += amount

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]
        return state

    def __repr__(self):
        return str(self.__getstate__())
