from __future__ import annotations

from dataclasses import dataclass
from magic_ledger import db
from enum import Enum


@dataclass
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    quantity = db.Column(db.Integer, nullable=False)
    measurement_unit = db.Column(db.String(255), nullable=False)
    acquisition_price = db.Column(db.Float, nullable=False)
    total_value = db.Column(db.Float, nullable=False)
    # could be linked to a specific invoice
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))
    # must belong to an organization
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)

    # add a constructor
    def __init__(self, name, description, quantity, measurement_unit, acquisition_price, invoice_id,
                 inventory_id):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.measurement_unit = measurement_unit
        self.acquisition_price = acquisition_price
        self.total_value = quantity * acquisition_price
        self.inventory_id = inventory_id
        self.invoice_id = invoice_id

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_sa_instance_state']
        return state

    def __repr__(self):
        return str(self.__getstate__())
