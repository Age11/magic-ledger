import magic_ledger.projects.project_status as project_status
import magic_ledger.third_parties.organization_type as organization_type
import magic_ledger.third_parties.service.organization_service as tps
from magic_ledger import db
from magic_ledger.projects.project import Project
from magic_ledger.third_parties.models.addressbook import Addressbook
from magic_ledger.third_parties.models.banking_details import BankingDetails
from magic_ledger.third_parties.models.organization import Organization


def create_project(request_body):
    project_data = {k: request_body[k] for k in ("project_name", "caen_code")}
    project_data["status"] = project_status.ACTIVE
    request_body["org_type"] = organization_type.PROJECT
    new_project = Project(**project_data)
    db.session.add(new_project)
    db.session.commit()

    tps.create_organization(request_body=request_body, project_id=new_project.id)
    return new_project


def get_all_projects_full_details():
    projects = (
        Project.query.join(Project, Project.id == Organization.owner_id)
        .join(Addressbook, Organization.address_id == Addressbook.id)
        .join(BankingDetails, Organization.banking_details_id == BankingDetails.id)
        .add_columns(Organization, Addressbook, BankingDetails)
        .filter(Organization.org_type == organization_type.PROJECT)
        .all()
    )

    return [
        {
            **prj[0].__getstate__(),
            **{
                k: prj[1].__getstate__()[k]
                for k in ("organization_name", "cif", "nrc", "org_type", "vat_mode")
            },
            **{
                k: prj[2].__getstate__()[k]
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
            },
            **{k: prj[3].__getstate__()[k] for k in ("account", "details")},
        }
        for prj in projects
    ]


def get_project_by_id(project_id):
    return Project.query.filter_by(id=project_id).first()
