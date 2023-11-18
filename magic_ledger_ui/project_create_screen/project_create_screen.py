import sys

from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw

from magic_ledger_ui.project_create_screen.UI.project_create_screen import (
    Ui_w_CreateProjet,
)


class ProjectCreateScreen(qtw.QWidget, Ui_w_CreateProjet):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.vat_mode = "on_invoice"
        # Retrieve the text input from the line edit
        self.le_Name.textChanged.connect(self.get_project_name)
        self.le_CIF.textChanged.connect(self.get_project_cif)
        self.le_NRC.textChanged.connect(self.get_project_nrc)
        self.cb_VAT_Mode.currentTextChanged.connect(self.get_vat_mode)
        self.le_CAEN.textChanged.connect(self.get_caen_code)
        self.pb_Create.clicked.connect(self.create_project)

    def get_project_name(self):
        self.project_name = self.le_Name.text()
        print("name changed")
        return self.project_name

    def get_project_cif(self):
        self.project_cif = self.le_CIF.text()
        return self.project_cif

    def get_project_nrc(self):
        self.project_nrc = self.le_NRC.text()
        return self.project_nrc

    def get_caen_code(self):
        self.project_caen_code = self.le_CAEN.text()
        return self.project_caen_code

    def get_vat_mode(self):
        option = self.cb_VAT_Mode.currentIndex()
        print(type(self.cb_VAT_Mode.currentIndex()))
        print(self.cb_VAT_Mode.itemText(self.cb_VAT_Mode.currentIndex()))
        if option == 0:
            self.vat_mode = "on_invoice"
        elif option == 1:
            self.vat_mode = "on_cash_in"
        else:
            self.vat_mode = "no_vat"
        return self.vat_mode

    def create_project(self):
        # create a project object
        project = {
            "name": self.project_name,
            "cif": self.project_cif,
            "nrc": self.project_nrc,
            "vat_mode": self.vat_mode,
            "caen_code": self.project_caen_code,
            "status": "active",
            "type": "project",
        }
        # send the project object to the server


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = ProjectCreateScreen()
    window.show()
    sys.exit(app.exec())
