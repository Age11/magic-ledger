import logging

from flask import Blueprint, jsonify, request

from magic_ledger.third_parties import organization_type, agent_type
from magic_ledger.third_parties.organization import Organization
import magic_ledger.third_parties.organization_service as organization_service
import magic_ledger.third_parties.agent_service as agent_service

bp = Blueprint("third-parties", __name__, url_prefix="/<project_id>/third-parties")

@bp.route("/organizations/", methods=("GET", "POST"))
def organizations(project_id):
    if request.method == "POST":
        logging.info("""Creating organization with the following data:""")
        logging.info(request.json)
        organization = organization_service.create_organization(request.json, project_id)
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/third-parties/organizations/" + str(
            organization.id
        )
        response.autocorrect_location_header = False
        return response

    elif request.method == "GET":
        orgs = Organization.query.filter_by(owner_id=project_id).all()
        return jsonify([row.__getstate__() for row in orgs])

@bp.route("/organizations/<org_id>", methods=("GET", "PUT"))
def get_organization_by_id(project_id, org_id):
    if request.method == "PUT":
        logging.info("""Editing supplier with the following data:""")
        logging.info(request.json)
        organization_service.update_organization(request.json, org_id)
        response = jsonify()
        response.status_code = 201
        return response
    elif request.method == "GET":
        organization = organization_service.get_organization_by_id(org_id, project_id)
        return jsonify(organization.__getstate__())
@bp.route("/organizations/suppliers/", methods=("GET", "POST"))
def create_supplier(project_id):
    if request.method == "POST":
        logging.info("""Creating supplier with the following data:""")
        request.json["org_type"] = organization_type.SUPPLIER
        logging.info(request.json)
        new_organization = organization_service.create_organization(request.json, project_id)
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/third-parties/organizations/" + str(
            new_organization.id
        )
        return response

    elif request.method == "GET":
        orgs = organization_service.get_all_suppliers(project_id)
        return jsonify([row.__getstate__() for row in orgs])


@bp.route("/organizations/suppliers/full/", methods=("GET",))
def get_suppliers_full_details(project_id):
    orgs = organization_service.get_suppliers_full_details(project_id)
    return jsonify(
        [{**org[0].__getstate__(), **org[1].__getstate__(), **org[2].__getstate__()} for org in orgs])

@bp.route("/organizations/clients/", methods=("GET", "POST"))
def create_client(project_id):
    if request.method == "POST":
        logging.info("""Creating client with the following data:""")
        request.json["org_type"] = organization_type.CLIENT
        logging.info(request.json)
        new_organization = organization_service.create_organization(request.json, project_id)
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/third-parties/organizations/" + str(
            new_organization.id
        )
        return response

    elif request.method == "GET":
        orgs = organization_service.get_all_clients(project_id)
        return jsonify([row.__getstate__() for row in orgs])

@bp.route("/organizations/clients/full/", methods=("GET",))
def get_client_full_details(project_id):
    orgs = organization_service.get_clients_full_details(project_id)

    return jsonify(
        [{**org[0].__getstate__(), **org[1].__getstate__(), **org[2].__getstate__()} for org in orgs])

@bp.route("/organizations/affiliates/", methods=("GET", "POST"))
def create_affiliate(project_id):
    if request.method == "POST":
        logging.info("""Creating affiliate with the following data:""")
        request.json["org_type"] = organization_type.AFFILIATE
        logging.info(request.json)
        new_organization = organization_service.create_organization(request.json, project_id)
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/third-parties/organizations/" + str(
            new_organization.id
        )
        return response
    elif request.method == "GET":
        orgs = organization_service.get_all_affiliates(project_id)
        return jsonify([row.__getstate__() for row in orgs])

@bp.route("/agents/", methods=("GET", "POST"))
def agents(project_id):
    if request.method == "POST":
        logging.info("""Creating agent with the following data:""")
        logging.info(request.json)

        new_agent = agent_service.create_agent(request.json, project_id)

        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/third-parties/agents/" + str(new_agent.id)
        response.autocorrect_location_header = False
        return response

    elif request.method == "GET":
        orgs = Organization.query.filter_by(owner_id=project_id).all()
        return jsonify([row.__getstate__() for row in orgs])

@bp.route("/agents/clients/", methods=("GET", "POST"))
def create_client_agent(project_id):
    if request.method == "POST":
        logging.info("""Creating agent with the following data:""")
        request.json["agent_type"] = agent_type.CLIENT
        logging.info(request.json)

        new_agent = agent_service.create_agent(request.json, project_id)

        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/third-parties/agents/" + str(new_agent.id)
        response.autocorrect_location_header = False
        return response

    elif request.method == "GET":
        agents = agent_service.get_all_clients(project_id)
        return jsonify([row.__getstate__() for row in agents])

@bp.route("/agents/suppliers/", methods=("GET", "POST"))
def create_supplier_agent(project_id):
    if request.method == "POST":
        logging.info("""Creating agent with the following data:""")
        request.json["agent_type"] = agent_type.SUPPLIER
        logging.info(request.json)

        new_agent = agent_service.create_agent(request.json, project_id)

        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/third-parties/agents/" + str(new_agent.id)
        response.autocorrect_location_header = False
        return response

    elif request.method == "GET":
        agents = agent_service.get_all_suppliers()
        return jsonify([row.__getstate__() for row in agents])

@bp.route("/agents/<agent_id>", methods=("GET",))
def get_agent_by_id(project_id, agent_id):
    agents = agent_service.get_agent_by_id(agent_id, project_id)
    return jsonify(agents.__getstate__())



@bp.route("/agents/clients/full/", methods=("GET",))
def get_supplier_agent_full_details(project_id):
    agts = agent_service.get_clients_full_details(project_id)

    return jsonify(
        [{**org[0].__getstate__(), **org[1].__getstate__(), **org[2].__getstate__()} for org in agts])
#

#
#

#
#
#
#

#
#

#
#

#
#

#

#
#
# @bp.route("/agents/clients/full/", methods=("GET",))
# def get_client_agent_full_details(project_id):
#     agts = Agent.query.join(Addressbook, Agent.address_id == Addressbook.id) \
#         .join(BankingDetails, Agent.banking_details_id == BankingDetails.id) \
#         .add_columns(Addressbook, BankingDetails) \
#         .filter(Agent.owner_id == project_id,
#                 Agent.agent_type == AgentTypeEnum.CLIENT).all()
#
#     return jsonify(
#         [{**org[0].__getstate__(), **org[1].__getstate__(), **org[2].__getstate__()} for org in agts])
#

