from __future__ import annotations

from dataclasses import dataclass
from dateutil.relativedelta import relativedelta

from magic_ledger import db

from datetime import datetime
from magic_ledger.assets import deprecation_method_type


@dataclass
class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    asset_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))

    initial_value = db.Column(db.Float, nullable=False)
    inventory_value = db.Column(db.Float, nullable=False)
    current_value = db.Column(db.Float, nullable=False)

    depreciation_method = db.Column(db.String(255), nullable=False)
    remaining_amount = db.Column(db.Float, nullable=False)
    deprecated_amount = db.Column(db.Float, nullable=False)
    remaining_duration = db.Column(db.Integer, nullable=False)
    monthly_amount = db.Column(db.Float, nullable=False)
    rounded_monthly_amount = db.Column(db.Float, nullable=False)
    total_duration = db.Column(db.Integer, nullable=False)
    acquisition_date = db.Column(db.DateTime, nullable=False)
    deprecation_start_date = db.Column(db.DateTime, nullable=False)
    recording_date = db.Column(db.DateTime, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)

    # add a constructor
    def __init__(
        self,
        asset_name,
        description,
        initial_value,
        inventory_value,
        current_value,
        depreciation_method,
        total_duration,
        acquisition_date,
        owner_id,
        recording_date=datetime.now().strftime("%Y-%m"),
    ):
        self.asset_name = asset_name
        self.description = description
        self.current_value = current_value
        self.initial_value = initial_value
        self.inventory_value = inventory_value
        self.total_duration = total_duration

        self.acquisition_date = datetime.strptime(acquisition_date, "%Y-%m")
        self.recording_date = datetime.strptime(recording_date, "%Y-%m")
        self.deprecation_start_date = self.acquisition_date + relativedelta(months=1)

        self.remaining_duration = self.total_duration - (
            (self.recording_date.month - self.deprecation_start_date.month)
            + 12 * (self.recording_date.year - self.deprecation_start_date.year)
        )

        self.depreciation_method = depreciation_method
        self.owner_id = owner_id
        if depreciation_method == deprecation_method_type.STREIGHT_LINE:
            self.monthly_amount = self.current_value / self.remaining_duration
            self.remaining_amount = round(
                self.monthly_amount * self.remaining_duration, 2
            )
            self.deprecated_amount = round(
                self.current_value - self.remaining_amount, 2
            )
        else:
            raise NotImplementedError(
                "Only straight line depreciation is supported at the moment."
            )
        self.rounded_monthly_amount = round(self.monthly_amount, 2)

    def __getstate__(self):
        state = self.__dict__.copy()
        state["total_duration"] = state["total_duration"] / 12
        del state["_sa_instance_state"]
        return state

    def __repr__(self):
        return str(self.__getstate__())
