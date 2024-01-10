from magic_ledger import db
from magic_ledger.third_parties import agent_type
from magic_ledger.third_parties.models.addressbook import Addressbook
from magic_ledger.third_parties.models.agent import Agent
from magic_ledger.third_parties.models.banking_details import BankingDetails


def create_agent(request_body, project_id):
    # Address
    addressbook_data = {
        k: request_body[k]
        for k in (
            "country",
            "state_or_province",
            "city",
            "street",
            "apartment_or_suite",
            "postal_code",
            "phone",
            "email",
        )
    }
    address = Addressbook(
        **addressbook_data,
    )
    db.session.add(address)
    db.session.commit()

    # Banking details
    banking_details_data = {k: request_body[k] for k in ("account", "details")}
    banking_details = BankingDetails(**banking_details_data)
    db.session.add(banking_details)
    db.session.commit()

    # Agent
    agent_data = {
        k: request_body[k] for k in ("agent_name", "last_name", "cnp", "agent_type")
    }
    agent_data["address_id"] = address.id
    agent_data["banking_details_id"] = banking_details.id
    agent_data["owner_id"] = project_id
    agent = Agent(**agent_data)
    db.session.add(agent)
    db.session.commit()
    return agent


def update_agent(request_body, owner_id, organization_id):
    agent = Agent.query.filter_by(id=organization_id, owner_id=owner_id).first()

    # Address
    addressbook_data = {
        k: request_body[k]
        for k in (
            "country",
            "state_or_province",
            "city",
            "street",
            "apartment_or_suite",
            "postal_code",
            "phone",
            "email",
        )
    }
    address = Addressbook.query.filter_by(id=agent.address_id).first()
    address.update_fields(addressbook_data)
    db.session.add(address)
    db.session.commit()

    # Banking details
    banking_details_data = {k: request_body[k] for k in ("account", "details")}
    banking_details = BankingDetails.query.filter_by(
        id=agent.banking_details_id
    ).first()
    banking_details.update_fields(banking_details_data)
    db.session.add(banking_details)
    db.session.commit()

    # Organization
    agent_data = {
        k: request_body[k] for k in ("agent_name", "last_name", "cnp", "agent_type")
    }
    agent.update_fields(agent_data)
    db.session.add(agent_data)
    db.session.commit()

    return agent_data


def create_client_agent(request_body, project_id):
    request_body["agent_type"] = agent_type.CLIENT
    return create_agent(request_body, project_id)


def create_supplier_agent(request_body, project_id):
    request_body["agent_type"] = agent_type.SUPPLIER
    return create_agent(request_body, project_id)


def get_all_agents(owner_id):
    return Agent.query.filter_by(owner_id=owner_id).all()


def get_agent_by_id(agent_id, owner_id):
    return Agent.query.filter_by(id=agent_id, owner_id=owner_id).first()


def get_all_suppliers(owner_id):
    return Agent.query.filter_by(
        agent_type=agent_type.SUPPLIER, owner_id=owner_id
    ).all()


def get_all_clients(owner_id):
    return Agent.query.filter_by(agent_type=agent_type.CLIENT, owner_id=owner_id).all()


def get_clients_full_details(owner_id):
    return (
        Agent.query.join(Addressbook, Agent.address_id == Addressbook.id)
        .join(BankingDetails, Agent.banking_details_id == BankingDetails.id)
        .add_columns(Addressbook, BankingDetails)
        .filter(Agent.owner_id == owner_id, Agent.agent_type == agent_type.CLIENT)
        .all()
    )
