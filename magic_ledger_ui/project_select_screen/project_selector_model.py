import configparser

import requests


class ProjectSelectorModel:
    column_names = ["Nume", "CIF", "NRC", "Status"]

    def __init__(self):
        self.projects = []
        self.config = configparser.ConfigParser().read(
            r"C:\Users\ageor\PycharmProjects\magic-ledger\magic_ledger_ui\config.ini"
        )

    def get_projects(self):
        response = requests.get("http://127.0.0.1:5000/organizations/projects")
        resp = response.json()
        for project in resp:
            self.projects.append(
                {
                    "name": project["name"],
                    "cif": project["cif"],
                    "nrc": project["nrc"],
                    "status": project["status"],
                }
            )
        return self.projects
