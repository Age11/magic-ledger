import configparser

import requests


class ProjectSelectorModel:
    def __init__(self, url):
        self.url = url
        self.projects = []
        self.selected_project = None
        self.config = configparser.ConfigParser().read("config.ini")

    def get_projects(self):
        response = requests.get(self.config["URL"] + self.config["PROJECTS"])
        self.projects = response.json()
        return self.projects
