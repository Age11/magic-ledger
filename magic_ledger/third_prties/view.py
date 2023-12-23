import logging

from flask import Blueprint, flash, jsonify, request
from magic_ledger import db
from magic_ledger.third_prties.addressbook import Addressbook
from magic_ledger.third_prties.agent import Agent
from magic_ledger.third_prties.banking_details import BankingDetails
from magic_ledger.third_prties.organization import Organization, OrgTypeEnum

bp = Blueprint("third-parties", __name__, url_prefix="/<project_id>/third-parties")


@bp.route("/organizations/", methods=("GET", "POST"))
def organizations(project_id):
    if request.method == "POST":
        logging.info("""Creating organization with the following data:""")
        logging.info(request.json)

        # Organization info
        name = request.json["name"]
        cif = request.json["cif"]
        nrc = request.json["nrc"]
        caen_code = request.json["caen_code"]
        org_type = request.json["org_type"]
        owner_id = project_id

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
            address = Addressbook(
                country=country,
                state_or_province=state_or_province,
                city=city,
                street=street,
                apartment_or_suite=apartment_or_suite,
                postal_code=postal_code,
                phone=phone,
                email=email,
            )
            db.session.add(address)
            db.session.commit()

            banking_details = BankingDetails(account=account, details=details)
            db.session.add(banking_details)
            db.session.commit()

            new_organization = Organization(
                name=name,
                cif=cif,
                nrc=nrc,
                org_type=org_type,
                caen_code=caen_code,
                owner_id=owner_id,
                address_id=address.id,
                banking_details_id=banking_details.id,
            )
            db.session.add(new_organization)
            db.session.commit()

            response = jsonify()
            response.status_code = 201
            response.headers["location"] = "/" + project_id + "/third-parties/organizations/" + str(
                new_organization.id
            )
            response.autocorrect_location_header = False
            return response

    elif request.method == "GET":
        orgs = Organization.query.filter_by(owner_id=project_id).all()
        return jsonify([row.__getstate__() for row in orgs])


@bp.route("/agents/", methods=("GET", "POST"))
def agents(project_id):
    if request.method == "POST":
        logging.info("""Creating agent with the following data:""")
        logging.info(request.json)

        # Organization info
        name = request.json["name"]
        middle_name = request.json["middle_name"]
        surname = request.json["surname"]
        cnp = request.json["cnp"]
        agent_type = request.json["agent_type"]
        owner_id = project_id

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
            address = Addressbook(
                country=country,
                state_or_province=state_or_province,
                city=city,
                street=street,
                apartment_or_suite=apartment_or_suite,
                postal_code=postal_code,
                phone=phone,
                email=email,
            )
            db.session.add(address)
            db.session.commit()

            banking_details = BankingDetails(account=account, details=details)
            db.session.add(banking_details)
            db.session.commit()

            new_agent = Agent(
                name=name,
                middle_name=middle_name,
                surname=surname,
                cnp=cnp,
                agent_type=agent_type,
                owner_id=owner_id,
                address_id=address.id,
                banking_details_id=banking_details.id,
            )
            db.session.add(new_agent)
            db.session.commit()
            response = jsonify()
            response.status_code = 201
            response.headers["location"] = "/" + project_id + "/third-parties/agents/" + str(new_agent.id)
            response.autocorrect_location_header = False
            return response

    elif request.method == "GET":
        orgs = Organization.query.filter_by(owner_id=project_id).all()
        return jsonify([row.__getstate__() for row in orgs])


@bp.route("/addressbook", methods=("GET", "POST"))
def addressbook(project_id):
    if request.method == "POST":
        logging.info("""Creating address with the following data:""")
        logging.info(request.json)

        country = request.json["country"]
        state_or_province = request.json["state_or_province"]
        city = request.json["city"]
        street = request.json["street"]
        apartment_or_suite = request.json["apartment_or_suite"]
        postal_code = request.json["postal_code"]
        phone = request.json["phone"]
        email = request.json["email"]

        error = None

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
def bank_details(project_id):
    if request.method == "POST":
        logging.info("""Creating banking details with the following data:""")
        logging.info(request.json)

        account = request.json["account"]
        details = request.json["details"]

        error = None

        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            banking_details = BankingDetails(account=account, details=details)
            db.session.add(banking_details)
            db.session.commit()
            return jsonify(banking_details)
    elif request.method == "GET":
        bd = BankingDetails.query.all()
        return jsonify([row.__getstate__() for row in bd])


@bp.route("/organizations/<org_id>", methods=("GET",))
def get_organizations_by_id(project_id, org_id):
    organization = Organization.query.filter_by(id=org_id, owner_id=project_id).first()
    return jsonify(organization.__getstate__())


@bp.route("/clients/", methods=("GET",))
def get_clients_by_id(project_id):
    orgs = Organization.query.filter_by(owner_id=project_id, org_type=OrgTypeEnum.CLIENT).all()
    return jsonify([row.__getstate__() for row in orgs])


@bp.route("/suppliers/", methods=("GET",))
def get_suppliers_by_id(project_id):
    orgs = Organization.query.filter_by(owner_id=project_id, org_type=OrgTypeEnum.SUPPLIER).all()
    return jsonify([row.__getstate__() for row in orgs])


@bp.route("/suppliers/", methods=("GET",))
def get_suppliers_full_details_by_id(project_id):
    orgs = Organization.query.join(Addressbook, Organization.address_id == Addressbook.id) \
        .join(BankingDetails, Organization.banking_details_id == BankingDetails.id) \
        .add_columns(Addressbook, BankingDetails) \
        .filter(Organization.owner_id == project_id,
                Organization.org_type == OrgTypeEnum.SUPPLIER).all()

    return jsonify(
        [{**org[0].__getstate__(), **org[1].__getstate__(), **org[2].__getstate__()} for org in orgs])
