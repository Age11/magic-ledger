import magic_ledger.third_parties.organization_type as organization_type
from magic_ledger import db
from magic_ledger.third_parties.models.addressbook import Addressbook
from magic_ledger.third_parties.models.banking_details import BankingDetails
from magic_ledger.third_parties.models.organization import Organization


def create_organization(request_body, project_id):
    # Address
    addressbook_data = {
        k: request_body[k]
        for k in (
            "country",
            "state_or_province",
            "city",
            "street",
            "apartment_or_suite",
            "postal_code",
            "phone",
            "email",
        )
    }
    address = Addressbook(
        **addressbook_data,
    )
    db.session.add(address)
    db.session.commit()
    # Banking details
    banking_details_data = {k: request_body[k] for k in ("account", "details")}
    banking_details = BankingDetails(**banking_details_data)
    db.session.add(banking_details)
    db.session.commit()
    # Organization
    organization_data = {
        k: request_body[k]
        for k in ("organization_name", "cif", "nrc", "org_type", "vat_mode")
    }
    organization_data["address_id"] = address.id
    organization_data["banking_details_id"] = banking_details.id
    organization_data["owner_id"] = project_id
    new_organization = Organization(**organization_data)
    db.session.add(new_organization)
    db.session.commit()
    return new_organization


def get_all_organizations(owner_id):
    return Organization.query.filter_by(owner_id=owner_id).all()


def update_organization(request_body, organization_id):
    organization = Organization.query.filter_by(id=organization_id).first()

    # Address
    addressbook_data = {
        k: request_body[k]
        for k in (
            "country",
            "state_or_province",
            "city",
            "street",
            "apartment_or_suite",
            "postal_code",
            "phone",
            "email",
        )
    }
    address = Addressbook.query.filter_by(id=organization.address_id).first()
    address.update_fields(addressbook_data)
    db.session.add(address)
    db.session.commit()

    # Banking details
    banking_details_data = {k: request_body[k] for k in ("account", "details")}
    banking_details = BankingDetails.query.filter_by(
        id=organization.banking_details_id
    ).first()
    banking_details.update_fields(banking_details_data)
    db.session.add(banking_details)
    db.session.commit()

    # Organization
    organization_data = {
        k: request_body[k] for k in ("organization_name", "cif", "nrc", "vat_mode")
    }
    organization.update_fields(organization_data)
    db.session.add(organization)
    db.session.commit()

    return organization


def get_organization_by_id(organization_id, owner_id):
    return Organization.query.filter_by(id=organization_id, owner_id=owner_id).first()


def create_supplier(request_body, project_id):
    request_body["org_type"] = organization_type.SUPPLIER
    return create_organization(request_body, project_id)


def get_all_suppliers(owner_id):
    return Organization.query.filter_by(
        org_type=organization_type.SUPPLIER, owner_id=owner_id
    ).all()


def get_supplier_by_id(supplier_id, owner_id):
    return Organization.query.filter_by(
        org_type=organization_type.SUPPLIER, id=supplier_id, owner_id=owner_id
    ).first()


def create_client(request_body, project_id):
    request_body["org_type"] = organization_type.CLIENT
    return create_organization(request_body, project_id)


def get_all_clients(owner_id):
    return Organization.query.filter_by(
        org_type=organization_type.CLIENT, owner_id=owner_id
    ).all()


def create_affiliate(request_body, project_id):
    request_body["org_type"] = organization_type.AFFILIATE
    return create_organization(request_body, project_id)


def get_all_affiliates(owner_id):
    return Organization.query.filter_by(
        org_type=organization_type.AFFILIATE, owner_id=owner_id
    ).all()


def get_clients_full_details(owner_id):
    return (
        Organization.query.join(Addressbook, Organization.address_id == Addressbook.id)
        .join(BankingDetails, Organization.banking_details_id == BankingDetails.id)
        .add_columns(Addressbook, BankingDetails)
        .filter(
            Organization.owner_id == owner_id,
            Organization.org_type == organization_type.CLIENT,
        )
        .all()
    )


def get_project_organizations(owner_id):
    return Organization.query.filter_by(
        org_type=organization_type.PROJECT, owner_id=owner_id
    ).all()
