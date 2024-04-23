from flask_restx import fields
from magic_ledger.extensions import api
from magic_ledger.inflow import vat_mode
from magic_ledger.projects import project_status
from magic_ledger.third_parties import organization_type


project_model_input = api.model(
    "input_project_organization_address_bank_details",
    {
        "project_name": fields.String(required=True, description="The project name"),
        "caen_code": fields.String(required=True, description="The project CAEN code"),
        "organization_name": fields.String(
            required=True, description="The organization name"
        ),
        "cif": fields.String(
            required=True,
            description="The organization fiscal identification code - CIF",
        ),
        "nrc": fields.String(
            required=True, description="The project registry of commerce number - NRC"
        ),
        "vat_mode": fields.String(
            required=True,
            description="The project VAT mode",
            enum=[vat_mode.ON_INVOICE, vat_mode.ON_CASH_IN, vat_mode.NO_VAT],
        ),
        "country": fields.String(
            required=True, description="The organization's address country field"
        ),
        "state_or_province": fields.String(
            required=True,
            description="The organization's address state or province field",
        ),
        "city": fields.String(
            required=True, description="The organization's address city field"
        ),
        "street": fields.String(
            required=True, description="The organization's address street field"
        ),
        "apartment_or_suite": fields.String(
            required=True,
            description="The organization's address apartment or suite field",
        ),
        "postal_code": fields.String(
            required=True, description="The organization's address postal code field"
        ),
        "phone": fields.String(
            required=True, description="The organization's phone field"
        ),
        "email": fields.String(
            required=True, description="The organization's email field"
        ),
        "account": fields.String(
            required=True, description="The organization's bank-account field"
        ),
        "details": fields.String(
            required=True, description="The organization's bank-account details field"
        ),
    },
)

project_model_output = api.model(
    "output_project_organization_address_bank_details",
    {
        "id": fields.Integer(required=True, description="The project id"),
        "project_name": fields.String(required=True, description="The project name"),
        "status": fields.String(
            required=True,
            description="The project status",
            enum=[
                project_status.ACTIVE,
                project_status.INACTIVE,
                project_status.DELETED,
            ],
        ),
        "creation_date": fields.String(description="The project creation date"),
        "organization_name": fields.String(
            required=True, description="The organization name"
        ),
        "caen_code": fields.String(required=True, description="The project CAEN code"),
        "cif": fields.String(
            required=True,
            description="The organization fiscal identification code - CIF",
        ),
        "nrc": fields.String(
            required=True, description="The project registry of commerce number - NRC"
        ),
        "vat_mode": fields.String(
            required=True,
            description="The project VAT mode",
            enum=[vat_mode.ON_INVOICE, vat_mode.ON_CASH_IN, vat_mode.NO_VAT],
        ),
        "org_type": fields.String(
            required=True,
            description="The organization type",
            enum=[
                organization_type.PROJECT,
                organization_type.CLIENT,
                organization_type.SUPPLIER,
            ],
        ),
        "country": fields.String(
            required=True, description="The organization's address country field"
        ),
        "state_or_province": fields.String(
            required=True,
            description="The organization's address state or province field",
        ),
        "city": fields.String(
            required=True, description="The organization's address city field"
        ),
        "street": fields.String(
            required=True, description="The organization's address street field"
        ),
        "apartment_or_suite": fields.String(
            required=True,
            description="The organization's address apartment or suite field",
        ),
        "postal_code": fields.String(
            required=True, description="The organization's address postal code field"
        ),
        "phone": fields.String(
            required=True, description="The organization's phone field"
        ),
        "email": fields.String(
            required=True, description="The organization's email field"
        ),
        "account": fields.String(
            required=True, description="The organization's bank-account field"
        ),
        "details": fields.String(
            required=True, description="The organization's bank-account details field"
        ),
    },
)

simple_project_model_output = api.model(
    "project",
    {
        "id": fields.Integer(required=True, description="The project id"),
        "project_name": fields.String(required=True, description="The project name"),
        "cae_code": fields.String(required=True, description="The project CAEN code"),
        "status": fields.String(
            required=True,
            description="The project status",
            enum=[
                project_status.ACTIVE,
                project_status.INACTIVE,
                project_status.DELETED,
            ],
        ),
        "creation_date": fields.String(description="The project creation date"),
    },
)
