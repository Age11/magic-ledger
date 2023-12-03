import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.third_prties.addressbook import Addressbook
from magic_ledger.third_prties.banking_details import BankingDetails
from magic_ledger.third_prties.organization import Organization, OrgTypeEnum

bp = Blueprint("organizations", __name__, url_prefix="/organizations")


@bp.route("/", methods=("GET", "POST"))
def organizations():
    if request.method == "POST":
        logging.info("""Creating company with the following data:""")
        logging.info(request.json)

        # Organization info
        name = request.json["name"]
        cif = request.json["cif"]
        nrc = request.json["nrc"]
        caen_code = request.json["caen_code"]
        org_type = request.json["org_type"]
        owner_id = request.json["owner_id"]

        # Address
        country = request.json["country"]
        state_or_province = request.json["state_or_province"]
        city = request.json["city"]
        street = request.json["street"]
        apartment_or_suite = request.json["apartment_or_suite"]
        postal_code = request.json["postal_code"]
        phone = request.json["phone"]
        email = request.json["email"]

        # Banking details
        account = request.json["account"]
        details = request.json["details"]

        error = None

        if not name:
            error = "Name is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            new_organization = Organization(
                name=name,
                cif=cif,
                nrc=nrc,
                org_type=org_type,
                caen_code=caen_code,
                owner_id=owner_id,
            )
            db.session.add(new_organization)
            db.session.commit()
            # retrieve the id of the newly created organization
            org_id = new_organization.id

            address = Addressbook(
                country=country,
                state_or_province=state_or_province,
                city=city,
                street=street,
                apartment_or_suite=apartment_or_suite,
                postal_code=postal_code,
                organization_id=org_id,
                phone=phone,
                email=email,
            )
            db.session.add(address)
            db.session.commit()

            banking_details = BankingDetails(
                account=account, organization_id=org_id, details=details
            )
            db.session.add(banking_details)
            db.session.commit()

            response = jsonify()
            response.status_code = 201

            response.headers["location"] = "/organizations/" + str(org_id)
            response.autocorrect_location_header = False

            return response

    elif request.method == "GET":
        orgs = Organization.query.all()
        return jsonify([row.__getstate__() for row in orgs])


@bp.route("/addressbook", methods=("GET", "POST"))
def addressbook():
    if request.method == "POST":
        logging.info("""Creating address with the following data:""")
        logging.info(request.json)

        country = request.json["country"]
        state_or_province = request.json["state_or_province"]
        city = request.json["city"]
        street = request.json["street"]
        apartment_or_suite = request.json["apartment_or_suite"]
        postal_code = request.json["postal_code"]
        organization_id = request.json["organization_id"]
        phone = request.json["phone"]
        email = request.json["email"]

        error = None

        if not organization_id:
            error = "organization id is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            address = Addressbook(
                country=country,
                state_or_province=state_or_province,
                city=city,
                street=street,
                apartment_or_suite=apartment_or_suite,
                postal_code=postal_code,
                organization_id=organization_id,
                phone=phone,
                email=email,
            )
            db.session.add(address)
            db.session.commit()
            return jsonify(address)
    elif request.method == "GET":
        addresses = Addressbook.query.all()
        return jsonify([row.__getstate__() for row in addresses])


@bp.route("/banking-details", methods=("GET", "POST"))
def bank_details():
    if request.method == "POST":
        logging.info("""Creating banking details with the following data:""")
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
            banking_details = BankingDetails(
                account=account, organization_id=organization_id, details=details
            )
            db.session.add(banking_details)
            db.session.commit()
            return jsonify(banking_details)
    elif request.method == "GET":
        bd = BankingDetails.query.all()
        return jsonify([row.__getstate__() for row in bd])


@bp.route("/<identifier>", methods=("GET",))
def get_organization_by_id(identifier):
    organization = Organization.query.filter_by(id=identifier).first()
    return jsonify(organization.__getstate__())


@bp.route("/<identifier>/addressbook", methods=("GET",))
def get_address_by_organization_id(identifier):
    address = Addressbook.query.filter_by(organization_id=identifier).first()
    return jsonify(address.__getstate__())


@bp.route("/<identifier>/banking-details", methods=("GET",))
def get_banking_details_by_organization_id(identifier):
    bank_details = BankingDetails.query.filter_by(organization_id=identifier).first()
    return jsonify(bank_details.__getstate__())
