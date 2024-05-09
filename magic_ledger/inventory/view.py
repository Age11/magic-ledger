import logging

from flask import request

from magic_ledger.inventory import inventory_service
from magic_ledger.inventory.api_model import (
    inventory_model_input,
    inventory_model_output,
    inventory_item_model_input,
    inventory_item_model_output,
)


from flask_restx import Namespace, Resource

ns = Namespace(
    "inventory",
    path="/<project_id>/inventories/",
    description="An api that allows the user to manage a project's inventories",
)


@ns.route("/")
class Inventories(Resource):
    @ns.expect(inventory_model_input, validate=True)
    @ns.response(201, "Inventory created successfully")
    def post(self, project_id):
        logging.info("""Creating an inventory with the following data:""")
        request.json["owner_id"] = project_id
        logging.info(request.json)
        inventory = inventory_service.create_inventory(request.json)
        return (
            {},
            201,
            {"location": "/" + project_id + "/inventories/" + str(inventory.id)},
        )

    @ns.marshal_list_with(inventory_model_output, code=200)
    def get(self, project_id):
        return inventory_service.get_all_inventories(owner_id=project_id), 200


@ns.route("/<inventory_id>/items/", endpoint="inventory_items")
class InventoryItems(Resource):
    @ns.expect(inventory_item_model_input)
    def post(self, project_id, inventory_id):
        logging.info("""Creating inventory item with the following data:""")
        request.json["inventory_id"] = inventory_id
        logging.info(request.json)

        item = inventory_service.create_item(request_body=request.json)

        return (
            {},
            201,
            {
                "location": "/"
                + str(project_id)
                + "/inventories/"
                + str(item.inventory_id)
                + "/items/"
                + str(item.id)
            },
        )

    @ns.marshal_list_with(inventory_item_model_output, code=200)
    def get(self, project_id, inventory_id):
        return (
            inventory_service.get_inventory_items_by_inventory_method(
                inventory_id=inventory_id
            ),
            200,
        )


@ns.route("/<inventory_id>/items/all", endpoint="all_inventory_items")
class AllInventoryItems(Resource):
    @ns.marshal_list_with(inventory_item_model_output, code=200)
    def get(self, project_id, inventory_id):
        return (
            inventory_service.get_all_inventory_items(
                inventory_id=inventory_id,
            ),
            200,
        )


@ns.route("/<inventory_id>/items/<item_id>/", endpoint="inventory_item")
class InventoryItemById(Resource):
    @ns.marshal_with(inventory_item_model_output)
    def get(self, project_id, inventory_id, item_id):
        return (
            inventory_service.get_item_by_id(
                item_id=item_id, inventory_id=inventory_id
            ),
            200,
        )


@ns.route("/<inventory_id>/items/<item_id>/decrease-stock/")
class DecreaseStock(Resource):
    def put(self, project_id, inventory_id, item_id):
        print("""Decreasing stock for item with id: {}""".format(item_id))
        request.json["inventory_id"] = inventory_id
        request.json["item_id"] = item_id
        logging.info(request.json)
        item = inventory_service.decrease_stock(
            item_id=item_id,
            inventory_id=inventory_id,
            quantity=request.json["quantity"],
            invoice_id=request.json["invoice_id"],
        )
        return {}, 204
