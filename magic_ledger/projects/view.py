from flask import Blueprint, jsonify, request
from magic_ledger.projects.project import Project
import magic_ledger.projects.project_service as project_service

bp = Blueprint("projects", __name__, url_prefix="/projects")

@bp.route("/", methods=("GET", "POST"))
def projects():
    if request.method == "POST":
        new_project = project_service.create_project(request_body=request.json)
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/projects/" + str(new_project.id)
        response.autocorrect_location_header = False

        return response

    elif request.method == "GET":
        projects = project_service.get_all_projects_full_details()
        return jsonify(
            [{**prj[0].__getstate__(), **prj[1].__getstate__(), **prj[2].__getstate__(), **prj[3].__getstate__()} for
             prj in projects])

@bp.route("/<project_id>", methods=("GET",))
def get_project(project_id):
    return jsonify(Project.query.filter_by(id=project_id).first().__getstate__())
