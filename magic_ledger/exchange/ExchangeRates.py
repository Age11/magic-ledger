from __future__ import annotations

from dataclasses import dataclass

from magic_ledger import db

from datetime import datetime
from magic_ledger.misc.currency import Currency

@dataclass
class ExchangeRate(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    currency_type = db.Column(db.Enum(Currency), nullable=False)
    value = db.Column(db.Float, nullable=False)
    reference_currency = db.Column(db.Enum(Currency), nullable=False)

    def __init__(
            self,
            date,
            currency_type,
            value,
            reference_currency,
    ):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.currency_type = Currency[currency_type]
        self.value = value
        self.reference_currency = Currency[reference_currency]

    def __getstate__(self):
        state = self.__dict__.copy()
        state["date"] = state["date"].strftime("%Y-%m-%d")
        state["currency_type"] = state["currency_type"].value
        state["reference_currency"] = state["reference_currency"].value
        del state["_sa_instance_state"]
        return state



