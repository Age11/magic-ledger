from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from magic_ledger import db
from magic_ledger.inventory import inventory_item_type


@dataclass
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))

    quantity = db.Column(db.Integer, nullable=False)
    measurement_unit = db.Column(db.String(255), nullable=False)
    acquisition_price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    total_value = db.Column(db.Float, nullable=False)
    sale_price = db.Column(db.Float, nullable=True)

    vat_rate = db.Column(db.Float, nullable=False)

    invoice_id = db.Column(db.Integer, db.ForeignKey("invoice.id"))
    inventory_id = db.Column(db.Integer, db.ForeignKey("inventory.id"), nullable=False)

    acquisition_date = db.Column(db.DateTime, nullable=False)
    entry_type = db.Column(db.String(7), nullable=False)

    def __init__(
        self,
        name,
        description,
        quantity,
        measurement_unit,
        acquisition_price,
        sale_price,
        vat_rate,
        invoice_id,
        inventory_id,
        currency="RON",
        acquisition_date=datetime.now().strftime("%Y-%m-%d"),
        entry_type=inventory_item_type.STOCK,
    ):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.measurement_unit = measurement_unit
        self.acquisition_price = acquisition_price
        self.vat_rate = vat_rate
        self.total_value = round(quantity * acquisition_price, 2)
        self.sale_price = sale_price
        self.inventory_id = inventory_id
        self.invoice_id = invoice_id
        self.currency = currency
        self.acquisition_date = datetime.strptime(acquisition_date, "%Y-%m-%d")
        self.entry_type = entry_type

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]
        state["acquisition_date"] = state["acquisition_date"].strftime("%Y-%m-%d")
        return state

    def __repr__(self):
        return str(self.__getstate__())

    def decrease_quantity(self, quantity):
        self.quantity -= quantity
        self.total_value = self.quantity * self.acquisition_price
        db.session.commit()
