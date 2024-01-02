from __future__ import annotations

from dataclasses import dataclass
from magic_ledger import db

from datetime import datetime
from magic_ledger.misc.currency import Currency

@dataclass
class ForeignCurrencyReserves(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    owner_id = db.Column(
        db.Integer, db.ForeignKey("project.id"), nullable=False
    )

    currency_type = db.Column(db.Enum(Currency), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    acquisition_price = db.Column(db.Float, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    analytical_account = db.Column(db.String(255), foreign_key="account_plan.account", nullable=False)
    acquisition_date = db.Column(db.DateTime, nullable=False)

    # add a constructor
    def __init__(
            self,
            owner_id,
            currency_type,
            quantity,
            acquisition_price,
            analytical_account,
            acquisition_date=datetime.now().strftime("%Y-%m-%d"),
    ):
        self.owner_id = owner_id
        self.currency_type = Currency[currency_type]
        self.quantity = quantity
        self.acquisition_price = acquisition_price
        self.total_amount = quantity * acquisition_price
        self.analytical_account = analytical_account
        self.acquisition_date = datetime.strptime(acquisition_date, "%Y-%m-%d")


    def __getstate__(self):
        state = self.__dict__.copy()
        state["currency_type"] = state["currency_type"].value
        state["acquisition_date"] = state["acquisition_date"].strftime("%Y-%m-%d")
        del state["_sa_instance_state"]
        return state

    def __repr__(self):
        return str(self.__getstate__())
