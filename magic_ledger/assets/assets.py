from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from magic_ledger import db


@dataclass
class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    asset_class = db.Column(db.String(255), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    depreciation_method = db.Column(db.String(255), nullable=False)
    remaining_value = db.Column(db.Float, nullable=False)
    remaining_duration = db.Column(db.Integer, nullable=False)
    monthly_amount = db.Column(db.Float, nullable=False)
    total_duration = db.Column(db.Integer, nullable=False)
    acquisition_date = db.Column(db.DateTime, nullable=False)
    organization_id = db.Column(
        db.Integer, db.ForeignKey("organization.id"), nullable=False
    )

    # add a constructor
    def __init__(
        self,
        name,
        description,
        asset_class,
        total_amount,
        depreciation_method,
        total_duration,
        acquisition_date,
        organization_id,
    ):
        self.name = name
        self.description = description
        self.asset_class = asset_class
        self.total_amount = total_amount
        self.total_duration = total_duration
        self.depreciation_method = depreciation_method
        self.organization_id = organization_id
        if depreciation_method == "straight_line":
            self.remaining_value = total_amount
            self.monthly_amount = total_amount / total_duration
            self.acquisition_date = datetime.strptime(acquisition_date, "%Y-%m-%d")
            self.recording_date = datetime.now()
            self.remaining_duration = total_duration - (
                (self.recording_date.month - self.acquisition_date.month)
                + 12 * (self.recording_date.year - self.acquisition_date.year)
            )
            self.remaining_amount = self.total_amount - (
                self.monthly_amount * self.remaining_duration
            )
        else:
            raise NotImplementedError(
                "Only straight line depreciation is supported at the moment."
            )

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]
        return state

    def __repr__(self):
        return str(self.__getstate__())
