from flask_restx import fields

from magic_ledger.assets import deprecation_method_type
from magic_ledger.extensions import api

asset_entry_model = api.model(
    "asset_entry_model",
    {
        "asset_name": fields.String(required=True, description="The asset name"),
        "description": fields.String(
            required=True, description="The asset description"
        ),
        "depreciation_method": fields.String(
            required=True,
            description="The asset depreciation method",
            enum=[deprecation_method_type.STREIGHT_LINE],
        ),
        "initial_value": fields.Float(
            required=True, description="The asset total amount"
        ),
        "inventory_value": fields.Float(
            required=True, description="The asset total amount"
        ),
        "current_value": fields.Float(
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
        "initial_value": fields.Float(
            required=True, description="The asset total amount"
        ),
        "inventory_value": fields.Float(
            required=True, description="The asset total amount"
        ),
        "current_value": fields.Float(
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
        "rounded_monthly_amount": fields.Float(
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
