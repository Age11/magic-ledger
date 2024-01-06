import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.inventory import inventory_service
from magic_ledger.inventory.inventory import Inventory
from magic_ledger.inventory.inventory_items import InventoryItem

bp = Blueprint("inventory", __name__, url_prefix="/<project_id>/inventory")


@bp.route("/", methods=("GET", "POST"))
def inventory(project_id):
    if request.method == "POST":
        logging.info("""Creating inventory with the following data:""")
        request.json["owner_id"] = project_id
        logging.info(request.json)
        inventory = inventory_service.create_inventory(request_body=request.json)

        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/inventory/" + str(inventory.id)
        response.autocorrect_location_header = False
        return response
    elif request.method == "GET":
        res = Inventory.query.all()
        return jsonify([row.__getstate__() for row in res])


@bp.route("<inventory_id>/items/", methods=("GET", "POST"))
def inventory_items(project_id, inventory_id):
    if request.method == "POST":
        logging.info("""Creating inventory item with the following data:""")
        request.json["inventory_id"] = inventory_id
        logging.info(request.json)

        item = inventory_service.create_item(request_body=request.json)

        db.session.add(item)
        db.session.commit()
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/inventory/" + inventory_id + "/items/" + str(item.id)
        return response
    elif request.method == "GET":
        product = InventoryItem.query.filter_by(inventory_id=inventory_id).all()
        return [row.__getstate__() for row in product]
