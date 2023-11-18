import sys

from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw

from magic_ledger_ui.project_select_screen.project_selector_model import (
    ProjectSelectorModel,
)
from magic_ledger_ui.project_select_screen.UI.project_select_screen import (
    Ui_w_SelectProject,
)


class ProjectSelectScreen(qtw.QWidget, Ui_w_SelectProject):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # populate the table view with data from a request to the server

        self.tv_Projects.setModel(self.get_projects_model())
        # make table resizeable
        self.tv_Projects.horizontalHeader().setSectionResizeMode(
            qtw.QHeaderView.Stretch
        )

        # show
        self.show()

    def get_projects_model(self):
        # create a table model that displays projects as per the magic ledger Organization__getstate__ method
        projects_model = qtg.QStandardItemModel()
        psm = ProjectSelectorModel()
        projects_model.setHorizontalHeaderLabels(psm.column_names)
        projects_model.setColumnCount(len(psm.column_names))
        prjcts = psm.get_projects()
        for i in range(len(prjcts)):
            projects_model.setItem(i, 0, qtg.QStandardItem(prjcts[i]["name"]))
            projects_model.setItem(i, 1, qtg.QStandardItem(prjcts[i]["cif"]))
            projects_model.setItem(i, 2, qtg.QStandardItem(prjcts[i]["nrc"]))
            projects_model.setItem(i, 3, qtg.QStandardItem(prjcts[i]["status"]))
            # add the row cells and add row to layout so it resizes
        return projects_model


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = ProjectSelectScreen()
    window.show()
    sys.exit(app.exec())
