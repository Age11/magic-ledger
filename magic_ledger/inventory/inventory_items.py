from __future__ import annotations

from dataclasses import dataclass

from magic_ledger import db


@dataclass
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))

    quantity = db.Column(db.Integer, nullable=False)
    measurement_unit = db.Column(db.String(255), nullable=False)
    acquisition_price = db.Column(db.Float, nullable=False)

    value = db.Column(db.Float, nullable=False)
    total_value = db.Column(db.Float, nullable=False)

    vat_rate = db.Column(db.Float, nullable=False)
    vat_amount = db.Column(db.Float, nullable=False)

    in_analytical_account = db.Column(
        db.String(255), db.ForeignKey("account_plan.account"), nullable=False
    )

    out_analytical_account = db.Column(
        db.String(255), db.ForeignKey("account_plan.account"), nullable=False
    )

    invoice_id = db.Column(db.Integer, db.ForeignKey("invoice.id"))
    inventory_id = db.Column(db.Integer, db.ForeignKey("inventory.id"), nullable=False)

    def __init__(
        self,
        name,
        description,
        quantity,
        measurement_unit,
        acquisition_price,
        vat_rate,
        in_analytical_account,
        out_analytical_account,
        invoice_id,
        inventory_id,
    ):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.measurement_unit = measurement_unit
        self.acquisition_price = acquisition_price
        self.vat_rate = vat_rate
        self.in_analytical_account = in_analytical_account
        self.out_analytical_account = out_analytical_account
        self.value = quantity * acquisition_price
        self.vat_amount = self.value * vat_rate / 100
        self.total_value = self.value + self.vat_amount
        self.inventory_id = inventory_id
        self.invoice_id = invoice_id

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]
        return state

    def __repr__(self):
        return str(self.__getstate__())
