from flask_restx import fields

from magic_ledger.assets import deprecation_method
from magic_ledger.extensions import api

asset_entry_model = api.model(
    "asset_entry_model",
    {
        # "asset_name", "description", "asset_class", "depreciation_method", "total_amount", "total_duration", "acquisition_date", "recording_date", "analytical_account", "deprecation_analytical_account", "owner_id"
        "asset_name": fields.String(required=True, description="The asset name"),
        "description": fields.String(
            required=True, description="The asset description"
        ),
        "asset_class": fields.String(required=True, description="The asset class"),
        "depreciation_method": fields.String(
            required=True,
            description="The asset depreciation method",
            enum=[deprecation_method.STREIGHT_LINE],
        ),
        "total_amount": fields.Float(
            required=True, description="The asset total amount"
        ),
        "total_duration": fields.Integer(
            required=True, description="The asset total duration"
        ),
        "acquisition_date": fields.String(
            required=True, description="The asset acquisition date"
        ),
        "recording_date": fields.String(
            required=True, description="The asset recording date"
        ),
        "analytical_account": fields.String(
            required=True, description="The asset analytical account"
        ),
        "deprecation_analytical_account": fields.String(
            required=True, description="The asset deprecation analytical account"
        ),
        "owner_id": fields.Integer(required=True, description="The asset owner id"),
    },
)

asset_output_model = api.model(
    "asset_output_model",
    {
        "id": fields.Integer(required=True, description="The asset id"),
        "asset_name": fields.String(required=True, description="The asset name"),
        "description": fields.String(
            required=True, description="The asset description"
        ),
        "asset_class": fields.String(required=True, description="The asset class"),
        "analytical_account": fields.String(
            required=True, description="The asset analytical account"
        ),
        "deprecation_analytical_account": fields.String(
            required=True, description="The asset deprecation analytical account"
        ),
        "total_amount": fields.Float(
            required=True, description="The asset total amount"
        ),
        "depreciation_method": fields.String(
            required=True, description="The asset depreciation method"
        ),
        "remaining_amount": fields.Float(
            required=True, description="The asset remaining amount"
        ),
        "deprecated_amount": fields.Float(
            required=True, description="The asset deprecated amount"
        ),
        "remaining_duration": fields.Integer(
            required=True, description="The asset remaining duration"
        ),
        "monthly_amount": fields.Float(
            required=True, description="The asset monthly amount"
        ),
        "total_duration": fields.Integer(
            required=True, description="The asset total duration"
        ),
        "acquisition_date": fields.String(
            required=True, description="The asset acquisition date"
        ),
        "deprecation_start_date": fields.String(
            required=True, description="The asset deprecation start date"
        ),
        "recording_date": fields.String(
            required=True, description="The asset recording date"
        ),
        "owner_id": fields.Integer(required=True, description="The asset owner id"),
    },
)
