from magic_ledger.inventory.inventory import Inventory
from magic_ledger.inventory.inventory_items import InventoryItem
from magic_ledger import db


def create_inventory(request_body):
    inventory_data = {
        k: request_body[k]
        for k in ("name", "description", "inventory_method", "owner_id")
    }
    new_inventory = Inventory(**inventory_data)
    db.session.add(new_inventory)
    db.session.commit()
    return new_inventory


def get_all_inventories(owner_id):
    return Inventory.query.filter_by(owner_id=owner_id).all()


def create_item(request_body):
    item_data = {
        k: request_body[k]
        for k in (
            "name",
            "description",
            "quantity",
            "measurement_unit",
            "acquisition_price",
            "vat_rate",
            "in_analytical_account",
            "out_analytical_account",
            "inventory_id",
            "invoice_id",
        )
    }
    new_item = InventoryItem(**item_data)
    db.session.add(new_item)
    db.session.commit()
    return new_item


def get_item_by_id(item_id, inventory_id):
    return InventoryItem.query.filter_by(id=item_id, inventory_id=inventory_id).first()


def get_all_inventory_items(inventory_id):
    return InventoryItem.query.filter_by(inventory_id=inventory_id).all()
