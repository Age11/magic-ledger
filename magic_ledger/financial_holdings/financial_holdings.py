from __future__ import annotations

from dataclasses import dataclass
from dateutil.relativedelta import relativedelta

from magic_ledger import db

from datetime import datetime, timedelta


@dataclass
class FinancialHoldings(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    organization_id = db.Column(
        db.Integer, db.ForeignKey("organization.id"), nullable=False
    )
    holding_type = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    aquisition_price = db.Column(db.Float, nullable=False)
    total_value = db.Column(db.Float, nullable=False)
    analytical_account = db.Column(
        db.String(255), db.ForeignKey("account_plan.account"), nullable=False
    )
    aquisition_date = db.Column(db.DateTime, nullable=False)

    # add a constructor
    def __init__(
        self,
        owner_id,
        organization_id,
        holding_type,
        quantity,
        aquisition_price,
        analytical_account,
        aquisition_date=datetime.now().strftime("%Y-%m-%d"),
    ):
        self.owner_id = owner_id
        self.organization_id = organization_id
        self.holding_type = holding_type
        self.quantity = quantity
        self.aquisition_price = aquisition_price
        self.total_value = quantity * aquisition_price
        self.analytical_account = analytical_account
        self.aquisition_date = datetime.strptime(aquisition_date, "%Y-%m-%d")

    def __getstate__(self):
        state = self.__dict__.copy()
        state["aquisition_date"] = state["aquisition_date"].strftime("%Y-%m-%d")
        del state["_sa_instance_state"]
        return state

    def __repr__(self):
        return str(self.__getstate__())
