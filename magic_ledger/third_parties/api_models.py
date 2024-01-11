from flask_restx import fields
from magic_ledger.extensions import api
from magic_ledger.inflow import vat_mode
from magic_ledger.third_parties import organization_type

organization_model_input = api.model(
    "input_organization_address_bank_details",
    {
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


organization_model_output = api.model(
    "output_organziation",
    {
        "id": fields.Integer(required=True, description="The organization id"),
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
        "org_type": fields.String(
            required=True,
            description="The organization type",
            enum=[
                organization_type.PROJECT,
                organization_type.CLIENT,
                organization_type.SUPPLIER,
            ],
        ),
        "address_id": fields.Integer(
            required=True, description="The organization's addressbook id"
        ),
        "banking_details_id": fields.Integer(
            required=True, description="The organization's banking details id"
        ),
        "owner_id": fields.Integer(
            required=True, description="The organization's owner id"
        ),
    },
)

agent_model_input = api.model(
    "input_agent_address_bank_details",
    {
        "agent_name": fields.String(
            required=True, description="The agent's first name"
        ),
        "last_name": fields.String(required=True, description="The agent's last name"),
        "cnp": fields.String(
            required=True, description="The agent's personal identification number"
        ),
        "country": fields.String(
            required=True, description="The agent's address country field"
        ),
        "state_or_province": fields.String(
            required=True, description="The agent's address state or province field"
        ),
        "city": fields.String(
            required=True, description="The agent's address city field"
        ),
        "street": fields.String(
            required=True, description="The agent's address street field"
        ),
        "apartment_or_suite": fields.String(
            required=True, description="The agent's address apartment or suite field"
        ),
        "postal_code": fields.String(
            required=True, description="The agent's address postal code field"
        ),
        "phone": fields.String(required=True, description="The agent's phone field"),
        "email": fields.String(required=True, description="The agent's email field"),
        "account": fields.String(
            required=True, description="The agent's bank-account field"
        ),
        "details": fields.String(
            required=True, description="The agent's bank-account details field"
        ),
    },
)

agent_model_output = api.model(
    "output_agent",
    {
        "id": fields.Integer(required=True, description="The agent id"),
        "agent_name": fields.String(
            required=True, description="The agent's first name"
        ),
        "last_name": fields.String(required=True, description="The agent's last name"),
        "cnp": fields.String(
            required=True, description="The agent's personal identification number"
        ),
        "agent_type": fields.String(
            required=True,
            description="The agent's type",
            enum=["client", "supplier"],
        ),
        "address_id": fields.Integer(
            required=True, description="The agent's addressbook id"
        ),
        "banking_details_id": fields.Integer(
            required=True, description="The agent's banking details id"
        ),
        "owner_id": fields.Integer(required=True, description="The agent's owner id"),
        "creation_date": fields.String(
            required=True, description="The agent's creation date"
        ),
    },
)

addressbook_model_output = api.model(
    "output_addressbook",
    {
        "id": fields.Integer(required=True, description="The addressbook id"),
        "country": fields.String(
            required=True, description="The addressbook country field"
        ),
        "state_or_province": fields.String(
            required=True, description="The addressbook state or province field"
        ),
        "city": fields.String(required=True, description="The addressbook city field"),
        "street": fields.String(
            required=True, description="The addressbook street field"
        ),
        "apartment_or_suite": fields.String(
            required=True, description="The addressbook apartment or suite field"
        ),
        "postal_code": fields.String(
            required=True, description="The addressbook postal code field"
        ),
        "phone": fields.String(
            required=True, description="The addressbook phone field"
        ),
        "email": fields.String(
            required=True, description="The addressbook email field"
        ),
    },
)

banking_details_model_output = api.model(
    "output_banking_details",
    {
        "id": fields.Integer(required=True, description="The banking details id"),
        "account": fields.String(
            required=True, description="The banking details account field"
        ),
        "details": fields.String(
            required=True, description="The banking details details field"
        ),
    },
)
