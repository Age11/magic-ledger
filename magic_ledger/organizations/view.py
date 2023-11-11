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
        logging.info(request.json)

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
            response = jsonify()
            response.status_code = 201
            response.headers['location'] = '/organizations/' + cif
            response.autocorrect_location_header = False
            return response

    elif request.method == "GET":
        companies = Organization.query.all()
        json_data = json.dumps([row.__getstate__() for row in companies], default=str)
        return json_data

@bp.route("/<cif>", methods=("GET",))
def get_organization_by_cif(cif):

    organization = Organization.query.filter_by(cif=cif).first()
    json_data = json.dumps(organization.__getstate__(), default=str)
    return json_data

