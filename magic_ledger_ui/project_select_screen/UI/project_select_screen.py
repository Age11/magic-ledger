# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_select_screenrKvFcP.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QGroupBox,
    QHeaderView,
    QPushButton,
    QSizePolicy,
    QTableView,
    QWidget,
)


class Ui_w_SelectProject(object):
    def setupUi(self, w_SelectProject):
        if not w_SelectProject.objectName():
            w_SelectProject.setObjectName("w_SelectProject")
        w_SelectProject.resize(485, 393)
        self.gridLayout = QGridLayout(w_SelectProject)
        self.gridLayout.setObjectName("gridLayout")
        self.gb_SelecteazaProiect = QGroupBox(w_SelectProject)
        self.gb_SelecteazaProiect.setObjectName("gb_SelecteazaProiect")
        self.gridLayout_2 = QGridLayout(self.gb_SelecteazaProiect)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pb_NewProject = QPushButton(self.gb_SelecteazaProiect)
        self.pb_NewProject.setObjectName("pb_NewProject")

        self.gridLayout_2.addWidget(self.pb_NewProject, 1, 1, 1, 1)

        self.pb_Select = QPushButton(self.gb_SelecteazaProiect)
        self.pb_Select.setObjectName("pb_Select")

        self.gridLayout_2.addWidget(self.pb_Select, 1, 0, 1, 1)

        self.pb_Edit = QPushButton(self.gb_SelecteazaProiect)
        self.pb_Edit.setObjectName("pb_Edit")

        self.gridLayout_2.addWidget(self.pb_Edit, 1, 2, 1, 1)

        self.tv_Projects = QTableView(self.gb_SelecteazaProiect)
        self.tv_Projects.setObjectName("tv_Projects")

        self.gridLayout_2.addWidget(self.tv_Projects, 0, 0, 1, 3)

        self.gridLayout.addWidget(self.gb_SelecteazaProiect, 0, 0, 1, 1)

        self.retranslateUi(w_SelectProject)

        QMetaObject.connectSlotsByName(w_SelectProject)

    # setupUi

    def retranslateUi(self, w_SelectProject):
        w_SelectProject.setWindowTitle(
            QCoreApplication.translate("w_SelectProject", "Selecteaza Proiect", None)
        )
        self.gb_SelecteazaProiect.setTitle(
            QCoreApplication.translate("w_SelectProject", "Proiecte", None)
        )
        self.pb_NewProject.setText(
            QCoreApplication.translate("w_SelectProject", "Proiect Nou", None)
        )
        self.pb_Select.setText(
            QCoreApplication.translate("w_SelectProject", "Selecteaza", None)
        )
        self.pb_Edit.setText(
            QCoreApplication.translate("w_SelectProject", "Editeaza", None)
        )

    # retranslateUi
