import sys

from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw

from magic_ledger_ui.project_select_screen.UI.project_select_screen import (
    Ui_w_SelectProject,
)


class ProjectSelectScreen(qtw.QWidget, Ui_w_SelectProject):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # populate the table view with data from a request to the server

        self.tv_Projects.setModel(self.get_projects_model())
        # show
        self.show()

    def get_projects_model(self):
        # create a table model that displays projects as per the magic ledger Organization__getstate__ method
        projects_model = qtg.QStandardItemModel()
        projects_model.setHorizontalHeaderLabels(
            ["Name", "CIF", "NRC", "Phone", "Email", "VAT Mode", "Status", "Type"]
        )
        projects_model.setVerticalHeaderLabels(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        )
        # Add a default row
        projects_model.setItem(0, 0, qtg.QStandardItem("Name"))
        projects_model.setItem(0, 1, qtg.QStandardItem("CIF"))
        projects_model.setItem(0, 2, qtg.QStandardItem("NRC"))
        projects_model.setItem(0, 3, qtg.QStandardItem("Phone"))
        projects_model.setItem(0, 4, qtg.QStandardItem("Email"))
        projects_model.setItem(0, 5, qtg.QStandardItem("VAT Mode"))
        projects_model.setItem(0, 6, qtg.QStandardItem("Status"))
        projects_model.setItem(0, 7, qtg.QStandardItem("Type"))
        return projects_model


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = ProjectSelectScreen()
    window.show()
    sys.exit(app.exec())
