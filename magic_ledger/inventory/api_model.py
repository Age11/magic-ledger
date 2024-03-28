from flask_restx import fields
from magic_ledger.extensions import api
from magic_ledger.inventory import inventory_type

inventory_model_output = api.model(
    "output_inventory",
    {
        "id": fields.Integer(required=True, description="The inventory id"),
        "name": fields.String(required=True, description="The inventory name"),
        "description": fields.String(
            required=True, description="The inventory description"
        ),
        "inventory_method": fields.String(
            required=True,
            description="The inventory method",
            enum=[
                inventory_type.FIFO,
                inventory_type.LIFO,
                inventory_type.AVERAGE,
            ],
        ),
        "owner_id": fields.Integer(required=True, description="The inventory owner id"),
    },
)

inventory_model_input = api.model(
    "input_inventory",
    {
        "name": fields.String(required=True, description="The inventory name"),
        "description": fields.String(
            required=True, description="The inventory description"
        ),
        "inventory_method": fields.String(
            required=True,
            description="The inventory method",
            enum=[
                inventory_type.FIFO,
                inventory_type.LIFO,
                inventory_type.AVERAGE,
            ],
        ),
    },
)

inventory_item_model_input = api.model(
    "inventory_item",
    {
        "name": fields.String(required=True, description="The item name"),
        "description": fields.String(required=True, description="The item description"),
        "quantity": fields.Integer(required=True, description="The item quantity"),
        "measurement_unit": fields.String(
            required=True, description="The item measurement unit"
        ),
        "acquisition_price": fields.Float(
            required=True, description="The item acquisition price"
        ),
        "vat_rate": fields.Float(required=True, description="The item vat rate"),
        "inventory_id": fields.Integer(
            required=True, description="The item inventory id"
        ),
        "invoice_id": fields.Integer(required=True, description="The item invoice id"),
    },
)


inventory_item_model_output = api.model(
    "inventory_item",
    {
        "id": fields.Integer(required=True, description="The item id"),
        "name": fields.String(required=True, description="The item name"),
        "description": fields.String(required=True, description="The item description"),
        "quantity": fields.Integer(required=True, description="The item quantity"),
        "measurement_unit": fields.String(
            required=True, description="The item measurement unit"
        ),
        "acquisition_price": fields.Float(
            required=True, description="The item acquisition price"
        ),
        "vat_rate": fields.Float(required=True, description="The item vat rate"),
        "vat_amount": fields.Float(required=True, description="The item total value"),
        "value": fields.Float(required=True, description="The item value"),
        "total_value": fields.Float(required=True, description="The item total value"),
        "inventory_id": fields.Integer(
            required=True, description="The item inventory id"
        ),
        "invoice_id": fields.Integer(required=True, description="The item invoice id"),
    },
)
