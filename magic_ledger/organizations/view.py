import json

from flask import Blueprint
from flask import request
from flask import flash
from flask import jsonify
from magic_ledger import db
from magic_ledger.organizations.model import Organization
import logging

bp = Blueprint("companies", __name__, url_prefix="/organizations")


@bp.route("/", methods=("GET", "POST"))
def organizations():
    if request.method == "POST":
        logging.info('''Creating company with the following data:''')
        logging.info(request.form)
        logging.info(request.data)

        name = request.json["name"]
        cif = request.json["cif"]
        nrc = request.json["nrc"]
        phone = request.json["phone"]
        email = request.json["email"]
        vat_mode = request.json["vat_mode"]
        caen_code = request.json["caen_code"]
        status = request.json["status"]
        type = request.json["type"]

        error = None

        if not name:
            error = "Name is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            new_organization = Organization(name=name, cif=cif, nrc=nrc,
                                            phone=phone, email=email, vat_mode=vat_mode, status=status,
                                            type=type, caen_code=caen_code)
            db.session.add(new_organization)
            db.session.commit()
            return jsonify(new_organization)

    elif request.method == "GET":
        companies = Organization.query.all()
        json_data = json.dumps([row.__getstate__() for row in companies], default=str)
        return json_data
