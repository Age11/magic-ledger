from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from magic_ledger import db


@dataclass
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    inv_type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    inventory_method = db.Column(db.String(50), nullable=False)
    # must belong to an organization
    owner_id = db.Column(
        db.Integer, db.ForeignKey("project.id"), nullable=False
    )

    def __init__(self, inv_type, name, description, inventory_method, owner_id):
        self.inv_type = inv_type
        self.name = name
        self.description = description
        self.inventory_method = inventory_method
        self.owner_id = owner_id

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]
        return state

    def __repr__(self):
        return str(self.__getstate__())
