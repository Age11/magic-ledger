import logging
import magic_ledger.third_parties.service.agent_service as agent_service
import magic_ledger.third_parties.service.organization_service as organization_service
from flask import request
from flask_restx import Namespace, Resource
from magic_ledger.third_parties.api_models import (
    addressbook_model_output,
    agent_model_input,
    agent_model_output,
    banking_details_model_output,
    organization_model_input,
    organization_model_output,
)
from magic_ledger.third_parties.service import (
    addressbook_service,
    banking_details_service,
)

ns = Namespace(
    "third-parties",
    path="/<project_id>/third-parties/",
    description="An api that allows the user to manage third parties related to the project (organizations and agents)",
)


@ns.route("/organizations/", endpoint="organization")
class Organizations(Resource):
    @ns.expect(organization_model_input)
    @ns.response(201, "Organization created")
    def post(self, project_id):
        logging.info("""Creating organization with the following data:""")
        logging.info(request.json)
        organization = organization_service.create_organization(
            request.json, project_id
        )
        return (
            {},
            201,
            {
                "location": "/"
                + project_id
                + "/third-parties/organizations/"
                + str(organization.id)
            },
        )

    @ns.marshal_list_with(organization_model_output, code=200)
    def get(self, project_id):
        return organization_service.get_all_organizations(project_id), 200


@ns.route("/organizations/<org_id>", endpoint="organization_by_id")
class OrganizationById(Resource):
    @ns.expect(organization_model_input)
    @ns.response(201, "Organization updated")
    def put(self, project_id, org_id):
        logging.info("""Editing organization with the following data:""")
        logging.info(request.json)
        organization_service.update_organization(request.json, org_id)
        return {}, 201

    @ns.marshal_with(organization_model_output, code=200)
    def get(self, project_id, org_id):
        return organization_service.get_organization_by_id(org_id, project_id), 200


@ns.route("/organizations/suppliers/", endpoint="organization_suppliers")
class SuppliersOrganization(Resource):
    @ns.expect(organization_model_input)
    @ns.response(201, "Supplier created")
    def post(self, project_id):
        logging.info("""Creating supplier with the following data:""")
        logging.info(request.json)
        organization = organization_service.create_supplier(request.json, project_id)
        return (
            {},
            201,
            {
                "location": "/"
                + project_id
                + "/third-parties/organizations/"
                + str(organization.id)
            },
        )

    @ns.marshal_list_with(organization_model_output, code=200)
    def get(self, project_id):
        return organization_service.get_all_suppliers(project_id), 200


@ns.route("/organizations/clients/", endpoint="organization_client")
class ClientsOrganization(Resource):
    @ns.expect(organization_model_input)
    @ns.response(201, "Client created")
    def post(self, project_id):
        logging.info("""Creating client with the following data:""")
        logging.info(request.json)
        organization = organization_service.create_client(request.json, project_id)
        return (
            {},
            201,
            {
                "location": "/"
                + project_id
                + "/third-parties/organizations/"
                + str(organization.id)
            },
        )

    @ns.marshal_list_with(organization_model_output, code=200)
    def get(self, project_id):
        return organization_service.get_all_clients(project_id), 200


@ns.route("/organizations/affiliates/", endpoint="affiliates")
class AffiliateOrganization(Resource):
    @ns.expect(organization_model_input)
    @ns.response(201, "Affiliate created")
    def post(self, project_id):
        logging.info("""Creating affiliate with the following data:""")
        logging.info(request.json)
        organization = organization_service.create_affiliate(request.json, project_id)
        return (
            {},
            201,
            {
                "location": "/"
                + project_id
                + "/third-parties/organizations/"
                + str(organization.id)
            },
        )

    @ns.marshal_list_with(organization_model_output, code=200)
    def get(self, project_id):
        return organization_service.get_all_affiliates(project_id), 200


@ns.route("/agents/", endpoint="agents")
class Agents(Resource):
    @ns.expect(agent_model_input)
    def post(self, project_id):
        logging.info("""Creating agent with the following data:""")
        logging.info(request.json)

        new_agent = agent_service.create_agent(request.json, project_id)

        return (
            {},
            201,
            {
                "location": "/"
                + project_id
                + "/third-parties/agents/"
                + str(new_agent.id)
            },
        )

    @ns.marshal_list_with(agent_model_output, code=200)
    def get(self, project_id):
        return agent_service.get_all_agents(project_id), 200


@ns.route("/agents/<agent_id>", endpoint="agent_by_id")
class AgentById(Resource):
    @ns.marshal_with(agent_model_output, code=200)
    def get(self, project_id, agent_id):
        return agent_service.get_agent_by_id(agent_id, project_id), 200

    @ns.expect(agent_model_input)
    def put(self, project_id, agent_id):
        logging.info("""Editing agent with the following data:""")
        logging.info(request.json)
        agent_service.update_agent(request.json, agent_id, project_id)
        return {}, 201


@ns.route("/agents/clients/", endpoint="agents_clients")
class ClientAgent(Resource):
    @ns.expect(agent_model_input)
    def post(self, project_id):
        logging.info("""Creating client agent with the following data:""")
        logging.info(request.json)
        new_agent = agent_service.create_client_agent(request.json, project_id)
        return (
            {},
            201,
            {
                "location": "/"
                + project_id
                + "/third-parties/agents/"
                + str(new_agent.id)
            },
        )

    @ns.marshal_list_with(agent_model_output)
    def get(self, project_id):
        return agent_service.get_all_clients(project_id), 200


@ns.route("/agents/suppliers/", endpoint="agents_suppliers")
class SupplierAgent(Resource):
    @ns.expect(agent_model_input)
    def post(self, project_id):
        logging.info("""Creating supplier agent with the following data:""")
        logging.info(request.json)
        new_agent = agent_service.create_supplier_agent(request.json, project_id)
        return (
            {},
            201,
            {
                "location": "/"
                + project_id
                + "/third-parties/agents/"
                + str(new_agent.id)
            },
        )

    @ns.marshal_list_with(agent_model_output)
    def get(self, project_id):
        return agent_service.get_all_suppliers(project_id), 200


@ns.route("/addressbook/<address_id>", endpoint="addressbook_by_id")
class AddressbookById(Resource):
    @ns.marshal_with(addressbook_model_output, code=200)
    def get(self, project_id, address_id):
        return addressbook_service.get_addressbook_by_id(address_id), 200


@ns.route("/banking_details/<banking_details_id>", endpoint="banking_details_by_id")
class BankingDetailsById(Resource):
    @ns.marshal_with(banking_details_model_output, code=200)
    def get(self, project_id, banking_details_id):
        return (
            banking_details_service.get_banking_details_by_id(banking_details_id),
            200,
        )
