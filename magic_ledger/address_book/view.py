import json

from flask import Blueprint
from flask import request
from flask import flash
from flask import jsonify
from magic_ledger import db
from magic_ledger.address_book.model import Addressbook
import logging

bp = Blueprint("addressbook", __name__, url_prefix="/addressbook")


@bp.route("/", methods=("GET", "POST"))
def invoices():
    if request.method == "POST":
        logging.info('''Creating address with the following data:''')
        logging.info(request.json)

        country = request.json["country"]
        stat_or_province = request.json["stat_or_province"]
        city = request.json["city"]
        street = request.json["street"]
        apartment_or_suite = request.json["apartment_or_suite"]
        postal_code = request.json["postal_code"]
        organization_id = request.json["organization_id"]

        error = None

        if not organization_id:
            error = "organization id is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            address = Addressbook(country=country, stat_or_province=stat_or_province, city=city,
                                  street=street, apartment_or_suite=apartment_or_suite, postal_code=postal_code,
                                  organization_id=organization_id)
            db.session.add(address)
            db.session.commit()
            return jsonify(address)
    elif request.method == "GET":
        addresses = Addressbook.query.all()
        json_data = json.dumps([row.__getstate__() for row in addresses], default=str)
        return json_data
