import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.assets.api_model import asset_entry_model, asset_output_model
from magic_ledger.assets.assets import Asset
import magic_ledger.assets.asset_service as asset_service

from flask_restx import Namespace, Resource

ns = Namespace(
    "account-balance",
    path="/<project_id>/assets/",
    description="An api that allows the user to manage assets",
)


@ns.route("/")
class Assets(Resource):
    @ns.marshal_list_with(asset_output_model, code=200)
    @ns.response(201, "Get assets")
    def get(self, project_id):
        return asset_service.get_all(owner_id=project_id), 200

    @ns.expect(asset_entry_model)
    @ns.response(201, "Asset created")
    def post(self, project_id):
        """Create a new asset"""
        logging.info("""Creating asset with the following data:""")
        logging.info(request.json)
        request.json["owner_id"] = project_id
        new_asset = asset_service.create_asset(request.json)
        return {}, 201, {"location": "/" + project_id + "/assets/" + str(new_asset.id)}
