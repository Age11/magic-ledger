from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from magic_ledger import db


class InventoryMethodEnum(Enum):
    FIFO = "fifo"
    LIFO = "lifo"
    AVERAGE = "average"
    SPECIFIC = "specific"


@dataclass
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    inv_type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    inventory_method = db.Column(db.Enum(InventoryMethodEnum), nullable=False)
    # must belong to an organization
    organization_id = db.Column(
        db.Integer, db.ForeignKey("organization.id"), nullable=False
    )

    # add a constructor
    def __init__(self, inv_type, name, description, inventory_method, organization_id):
        self.inv_type = inv_type
        self.name = name
        self.description = description
        if inventory_method == "fifo":
            self.inventory_method = InventoryMethodEnum.FIFO
        elif inventory_method == "lifo":
            self.inventory_method = InventoryMethodEnum.LIFO
        elif inventory_method == "average":
            self.inventory_method = InventoryMethodEnum.AVERAGE
        elif inventory_method == "specific":
            self.inventory_method = InventoryMethodEnum.SPECIFIC
        self.organization_id = organization_id

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]
        if state["inventory_method"] == InventoryMethodEnum.FIFO:
            state["inventory_method"] = "fifo"
        elif state["inventory_method"] == InventoryMethodEnum.LIFO:
            state["inventory_method"] = "lifo"
        elif state["inventory_method"] == InventoryMethodEnum.AVERAGE:
            state["inventory_method"] = "average"
        elif state["inventory_method"] == InventoryMethodEnum.SPECIFIC:
            state["inventory_method"] = "specific"
        return state

    def __repr__(self):
        return str(self.__getstate__())
