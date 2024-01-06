import magic_ledger.third_parties.organization_service as tps
import magic_ledger.projects.project_status as project_status
import magic_ledger.third_parties.organization_type as organization_type
from magic_ledger.projects.project import Project
from magic_ledger import db
from magic_ledger.third_parties.addressbook import Addressbook
from magic_ledger.third_parties.banking_details import BankingDetails
from magic_ledger.third_parties.organization import Organization

def create_project(request_body):
    project_data = {k: request_body[k] for k in ('project_name', 'caen_code')}
    project_data['status'] = project_status.ACTIVE
    request_body['org_type'] = organization_type.PROJECT
    new_project = Project(
        **project_data
    )
    db.session.add(new_project)
    db.session.commit()

    tps.create_organization(request_body=request_body, project_id=new_project.id)
    return new_project

def get_all_projects_full_details():
    return Project.query.join(Project, Project.id == Organization.owner_id) \
        .join(Addressbook, Organization.address_id == Addressbook.id) \
        .join(BankingDetails, Organization.banking_details_id == BankingDetails.id) \
        .add_columns(Organization, Addressbook, BankingDetails) \
        .filter(Organization.org_type == organization_type.PROJECT).all()