from magic_ledger.inventory import inventory_type, inventory_item_type
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


def get_inventory_by_id(inventory_id):
    return Inventory.query.filter_by(id=inventory_id).first()


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
            "sale_price",
            "currency",
            "vat_rate",
            "inventory_id",
        )
    }
    if "invoice_id" in request_body.keys():
        item_data["invoice_id"] = request_body["invoice_id"]
    else:
        item_data["invoice_id"] = None

    if "acquisition_date" in request_body.keys():
        item_data["acquisition_date"] = request_body["acquisition_date"]

    if "entry_type" in request_body.keys():
        item_data["entry_type"] = request_body["entry_type"]

    new_item = InventoryItem(**item_data)
    db.session.add(new_item)
    db.session.commit()
    return new_item


def get_item_by_id(item_id, inventory_id):
    return InventoryItem.query.filter_by(
        id=item_id, inventory_id=inventory_id, entry_type=inventory_item_type.STOCK
    ).first()


def get_all_inventory_items(inventory_id):
    return InventoryItem.query.filter_by(
        inventory_id=inventory_id, entry_type=inventory_item_type.STOCK
    ).all()


def get_inventory_items_by_inventory_method(inventory_id):
    inv = get_inventory_by_id(inventory_id)
    if inv.inventory_method == inventory_type.FIFO:
        return get_fifo_inventory_items(inventory_id)
    elif inv.inventory_method == inventory_type.LIFO:
        return get_lifo_inventory_items(inventory_id)
    elif inv.inventory_method == inventory_type.AVERAGE:
        return get_average_inventory_items(inventory_id)
    else:
        return []


def get_fifo_inventory_items(inventory_id):
    inventory_items = (
        InventoryItem.query.filter_by(inventory_id=inventory_id)
        .order_by(InventoryItem.acquisition_date.asc())
        .all()
    )
    selected_items = {}
    for item in inventory_items:
        if item.name not in selected_items and item.quantity > 0:
            selected_items[item.name] = item

    return list(selected_items.values())


def get_lifo_inventory_items(inventory_id):
    inventory_items = (
        InventoryItem.query.filter_by(inventory_id=inventory_id)
        .order_by(InventoryItem.acquisition_date.desc())
        .all()
    )
    selected_items = {}
    for item in inventory_items:
        if item.name not in selected_items and item.quantity > 0:
            selected_items[item.name] = item

    return list(selected_items.values())


def get_average_inventory_items(inventory_id):
    return InventoryItem.query.filter_by(inventory_id=inventory_id).all()


def decrease_stock(item_id, inventory_id, quantity, invoice_id):
    item = get_item_by_id(item_id, inventory_id)
    item.decrease_quantity(quantity)

    return item


def get_items_from_invoice(invoice_id):
    return InventoryItem.query.filter_by(invoice_id=invoice_id).all()
