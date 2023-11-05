import json

from flask import Blueprint
from flask import request
from flask import flash
from flask import jsonify
from magic_ledger import db
from magic_ledger.inventory_item.model import InventoryItem
import logging

bp = Blueprint("inventory_item", __name__, url_prefix="/inventory_item")


@bp.route("/", methods=("GET", "POST"))
def products():
    if request.method == "POST":
        logging.info('''Creating inventory item with the following data:''')
        logging.info(request.json)

        name = request.json["name"]
        description = request.json["description"]
        quantity = request.json["quantity"]
        measurement_unit = request.json["measurement_unit"]
        acquisition_price = request.json["acquisition_price"]
        total_value = request.json["total_value"]
        inventory_id = request.json["inventory_id"]
        invoice_id = request.json["invoice_id"]

        error = None

        if not inventory_id:
            error = "inventory id is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            product = InventoryItem(name=name, description=description, quantity=quantity,
                                    measurement_unit=measurement_unit, acquisition_price=acquisition_price,
                                    total_value=total_value, inventory_id=inventory_id, invoice_id=invoice_id)
            db.session.add(product)
            db.session.commit()
            return jsonify(product)
    elif request.method == "GET":
        product = InventoryItem.query.all()
        json_data = json.dumps([row.__getstate__() for row in product], default=str)
        return json_data
