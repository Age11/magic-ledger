import json

from flask import Blueprint
from flask import request
from flask import flash
from flask import jsonify
from magic_ledger import db
from magic_ledger.organizations.organization_model import Organization
from magic_ledger.organizations.addressbook_model import Addressbook
from magic_ledger.organizations.banking_details_model import BankingDetails
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
            #retrieve the id of the newly created organization
            org_id = str(Organization.query.filter_by(cif=cif).first().id)

            response = jsonify()
            response.status_code = 201

            response.headers['location'] = '/organizations/' + org_id
            response.autocorrect_location_header = False
            return response

    elif request.method == "GET":
        organizations = Organization.query.all()
        json_data = json.dumps([row.__getstate__() for row in organizations], default=str)
        return json_data
@bp.route("/<id>", methods=("GET",))
def get_organization_by_id(id):
   organization = Organization.query.filter_by(id=id).first()
   json_data = json.dumps(organization.__getstate__(), default=str)
   return json_data

@bp.route("/addressbook", methods=("GET", "POST"))
def addressbook():
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

@bp.route("/banking-details", methods=("GET", "POST"))
def bank_details():
    if request.method == "POST":
        logging.info('''Creating banking details with the following data:''')
        logging.info(request.json)

        organization_id = request.json["organization_id"]
        account = request.json["account"]
        details = request.json["details"]


        error = None

        if not organization_id:
            error = "organization id is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            address = BankingDetails(account=account, organization_id=organization_id, details=details)
            db.session.add(address)
            db.session.commit()
            return jsonify(address)
    elif request.method == "GET":
        addresses = BankingDetails.query.all()
        json_data = json.dumps([row.__getstate__() for row in addresses], default=str)
        return json_data