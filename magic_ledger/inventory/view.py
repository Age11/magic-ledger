import json

from flask import Blueprint
from flask import request
from flask import flash
from flask import jsonify
from magic_ledger import db
from magic_ledger.inventory.model import Inventory
import logging

bp = Blueprint("inventory", __name__, url_prefix="/inventory")


@bp.route("/", methods=("GET", "POST"))
def inventory():
    if request.method == "POST":
        logging.info('''Creating inventory with the following data:''')
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
            inv = Inventory(inv_type, name, description, inventory_method, organization_id)
            db.session.add(inv)
            db.session.commit()
            return jsonify(inv)
    elif request.method == "GET":
        res = Inventory.query.all()
        json_data = json.dumps([row.__getstate__() for row in res], default=str)
        return json_data
