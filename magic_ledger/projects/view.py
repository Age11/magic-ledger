import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.projects.project import Project
from magic_ledger.third_prties.addressbook import Addressbook
from magic_ledger.third_prties.banking_details import BankingDetails
from magic_ledger.third_prties.organization import Organization, OrgTypeEnum

bp = Blueprint("projects", __name__, url_prefix="/projects")


@bp.route("/", methods=("GET", "POST"))
def projects():
    if request.method == "POST":
        # Project info
        project_name = request.json["project_name"]
        vat_mode = request.json["vat_mode"]
        status = "active"

        # Organization info
        org_name = request.json["organization_name"]
        cif = request.json["cif"]
        nrc = request.json["nrc"]
        caen_code = request.json["caen_code"]
        org_type = "project"

        # Address info
        country = request.json["country"]
        state_or_province = request.json["state_or_province"]
        city = request.json["city"]
        street = request.json["street"]
        apartment_or_suite = request.json["apartment_or_suite"]
        postal_code = request.json["postal_code"]
        phone = request.json["phone"]
        email = request.json["email"]

        # Bank details
        account = request.json["account"]
        details = request.json["details"]

        error = None
        if not org_name:
            error = "Name is required."
        # TODO: add more validation

        if error is not None:
            flash(error)
        else:
            new_project = Project(
                name=project_name,
                vat_mode=vat_mode,
                status=status,
                caen_code=caen_code,
            )
            db.session.add(new_project)
            db.session.commit()

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
                name=org_name,
                cif=cif,
                nrc=nrc,
                org_type=org_type,
                caen_code=caen_code,
                owner_id=new_project.id,
                address_id=address.id,
                banking_details_id=banking_details.id,
            )
            db.session.add(new_organization)
            db.session.commit()

            response = jsonify()
            response.status_code = 201
            response.headers["location"] = "/projects/" + str(new_project.id)
            response.autocorrect_location_header = False

            return response

    elif request.method == "GET":
        projects = Organization.query.filter_by(org_type=OrgTypeEnum.PROJECT).all()
        return jsonify([row.__getstate__() for row in projects])
