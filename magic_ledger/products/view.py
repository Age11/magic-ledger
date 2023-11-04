import json

from flask import Blueprint
from flask import request
from flask import flash
from flask import jsonify
from magic_ledger import db
from magic_ledger.products.model import Product
import logging

bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route("/", methods=("GET", "POST"))
def products():
    if request.method == "POST":
        logging.info('''Creating inventory with the following data:''')
        logging.info(request.form)
        logging.info(request.data)

        name = request.json["name"]
        description = request.json["description"]
        quantity = request.json["quantity"]
        measurement_unit = request.json["measurement_unit"]
        acquisition_price = request.json["acquisition_price"]
        total_value = request.json["total_value"]
        organization_id = request.json["organization_id"]
        invoice_id = request.json["invoice_id"]

        error = None

        if not organization_id:
            error = "organization id is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            product = Product(name=name, description=description, quantity=quantity,
                              measurement_unit=measurement_unit, acquisition_price=acquisition_price,
                              total_value=total_value, organization_id=organization_id, invoice_id=invoice_id)
            db.session.add(product)
            db.session.commit()
            return jsonify(product)
    elif request.method == "GET":
        product = Product.query.all()
        json_data = json.dumps([row.__getstate__() for row in product], default=str)
        return json_data
