import json
import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.inventory.inventory import Inventory
from magic_ledger.inventory.inventory_items import InventoryItem

bp = Blueprint("inventory", __name__, url_prefix="/inventory")


@bp.route("/", methods=("GET", "POST"))
def inventory():
    if request.method == "POST":
        logging.info("""Creating inventory with the following data:""")
        logging.info(request.json)

        inv_type = request.json["inv_type"]
        name = request.json["name"]
        description = request.json["description"]
        inventory_method = request.json["inventory_method"]
        organization_id = request.json["organization_id"]

        error = None

        if not organization_id:
            error = "organization id is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            inv = Inventory(
                inv_type, name, description, inventory_method, organization_id
            )
            db.session.add(inv)
            db.session.commit()
            response = jsonify()
            response.status_code = 201
            response.headers["location"] = "/organizations/" + str(inv.id)
            response.autocorrect_location_header = False
            return response
    elif request.method == "GET":
        res = Inventory.query.all()
        json_data = json.dumps([row.__getstate__() for row in res], default=str)
        return json_data


@bp.route("/items/", methods=("GET", "POST"))
def products():
    if request.method == "POST":
        logging.info("""Creating inventory item with the following data:""")
        logging.info(request.json)

        name = request.json["name"]
        description = request.json["description"]
        quantity = request.json["quantity"]
        measurement_unit = request.json["measurement_unit"]
        acquisition_price = request.json["acquisition_price"]
        inventory_id = request.json["inventory_id"]
        invoice_id = request.json["invoice_id"]

        error = None

        if not inventory_id:
            error = "inventory id is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            item = InventoryItem(
                name=name,
                description=description,
                quantity=quantity,
                measurement_unit=measurement_unit,
                acquisition_price=acquisition_price,
                inventory_id=inventory_id,
                invoice_id=invoice_id,
            )
            db.session.add(item)
            db.session.commit()
            response = jsonify()
            response.status_code = 201
            response.headers["location"] = "/inventory/items/" + str(item.id)
            return response
    elif request.method == "GET":
        product = InventoryItem.query.all()
        json_data = json.dumps([row.__getstate__() for row in product], default=str)
        return json_data
