from flask_restx import fields
from magic_ledger.extensions import api
from magic_ledger.inventory import inventory_type, inventory_item_type

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
        "sale_price": fields.Float(required=True, description="The item sale price"),
        "currency": fields.String(required=True, description="The item currency"),
        "vat_rate": fields.Float(required=True, description="The item vat rate"),
        "inventory_id": fields.Integer(
            required=True, description="The item inventory id"
        ),
        "invoice_id": fields.Integer(required=True, description="The item invoice id"),
        "acquisition_date": fields.String(
            required=True, description="The item acquisition date"
        ),
        "entry_type": fields.String(
            required=False,
            description="The item entry type",
            enum=[inventory_item_type.STOCK, inventory_item_type.ORDER],
        ),
    },
)


class DateField(fields.Raw):
    def format(self, value):
        if value is not None:
            return value.strftime(
                "%Y-%m-%d"
            )  # Formats the datetime object to 'YYYY-MM-DD'
        return None


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
        "sale_price": fields.Float(required=True, description="The item sale price"),
        "currency": fields.String(required=True, description="The item currency"),
        "vat_rate": fields.Float(required=True, description="The item vat rate"),
        "total_value": fields.Float(required=True, description="The item total value"),
        "inventory_id": fields.Integer(
            required=True, description="The item inventory id"
        ),
        "invoice_id": fields.Integer(required=True, description="The item invoice id"),
        "acquisition_date": DateField(
            required=True, description="The item acquisition date"
        ),
    },
)
