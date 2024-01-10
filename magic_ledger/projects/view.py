import magic_ledger.projects.project_service as project_service
from flask import request
from flask_restx import Namespace, Resource
from magic_ledger.projects.api_models import (project_model_input,
                                              project_model_output,
                                              simple_project_model_output)

ns = Namespace(
    "projects",
    description="Accounting projects. Each project is related to an organizations operations and identity",
)


@ns.route("/")
class Projects(Resource):
    @ns.expect(project_model_input)
    @ns.response(201, "Project created")
    def post(self):
        new_project = project_service.create_project(request_body=request.json)
        return {}, 201, {"location": "/projects/" + str(new_project.id)}

    @ns.marshal_list_with(
        project_model_output, code=200, description="All projects with full details"
    )
    @ns.response(200, "Get all projects with full details")
    def get(self):
        return project_service.get_all_projects_full_details()


@ns.route("/<project_id>", endpoint="project_by_id")
class ProjectById(Resource):
    @ns.doc(params={"project_id": "The project identifier"})
    @ns.response(200, "Returns the project having the specified identifier")
    @ns.marshal_with(simple_project_model_output)
    def get(self, project_id):
        return project_service.get_project_by_id(project_id)
