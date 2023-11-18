# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_create_screendikuKL.ui'
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
    QComboBox,
    QGridLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_w_CreateProjet(object):
    def setupUi(self, w_CreateProjet):
        if not w_CreateProjet.objectName():
            w_CreateProjet.setObjectName("w_CreateProjet")
        w_CreateProjet.resize(634, 452)
        self.gridLayout = QGridLayout(w_CreateProjet)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QGroupBox(w_CreateProjet)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lb_Vat_Mode = QLabel(self.groupBox)
        self.lb_Vat_Mode.setObjectName("lb_Vat_Mode")

        self.gridLayout_2.addWidget(self.lb_Vat_Mode, 3, 0, 1, 1)

        self.le_Name = QLineEdit(self.groupBox)
        self.le_Name.setObjectName("le_Name")
        self.le_Name.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.le_Name, 0, 2, 1, 1)

        self.lb_caen_code = QLabel(self.groupBox)
        self.lb_caen_code.setObjectName("lb_caen_code")

        self.gridLayout_2.addWidget(self.lb_caen_code, 4, 0, 1, 1)

        self.le_CIF = QLineEdit(self.groupBox)
        self.le_CIF.setObjectName("le_CIF")
        self.le_CIF.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.le_CIF, 1, 2, 1, 1)

        self.lb_NRC = QLabel(self.groupBox)
        self.lb_NRC.setObjectName("lb_NRC")
        self.lb_NRC.setToolTipDuration(-1)

        self.gridLayout_2.addWidget(self.lb_NRC, 2, 0, 1, 1)

        self.lb_CIF = QLabel(self.groupBox)
        self.lb_CIF.setObjectName("lb_CIF")
        self.lb_CIF.setToolTipDuration(-1)

        self.gridLayout_2.addWidget(self.lb_CIF, 1, 0, 1, 1)

        self.pb_Cancel = QPushButton(self.groupBox)
        self.pb_Cancel.setObjectName("pb_Cancel")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_Cancel.sizePolicy().hasHeightForWidth())
        self.pb_Cancel.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.pb_Cancel, 5, 2, 1, 1)

        self.le_NRC = QLineEdit(self.groupBox)
        self.le_NRC.setObjectName("le_NRC")
        self.le_NRC.setAutoFillBackground(True)
        self.le_NRC.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.le_NRC, 2, 2, 1, 1)

        self.lb_namel = QLabel(self.groupBox)
        self.lb_namel.setObjectName("lb_namel")

        self.gridLayout_2.addWidget(self.lb_namel, 0, 0, 1, 2)

        self.le_CAEN = QLineEdit(self.groupBox)
        self.le_CAEN.setObjectName("le_CAEN")
        self.le_CAEN.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.le_CAEN, 4, 2, 1, 1)

        self.pb_Create = QPushButton(self.groupBox)
        self.pb_Create.setObjectName("pb_Create")
        sizePolicy.setHeightForWidth(self.pb_Create.sizePolicy().hasHeightForWidth())
        self.pb_Create.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.pb_Create, 5, 0, 1, 2)

        self.cb_VAT_Mode = QComboBox(self.groupBox)
        self.cb_VAT_Mode.addItem("")
        self.cb_VAT_Mode.addItem("")
        self.cb_VAT_Mode.addItem("")
        self.cb_VAT_Mode.setObjectName("cb_VAT_Mode")

        self.gridLayout_2.addWidget(self.cb_VAT_Mode, 3, 2, 1, 1)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.retranslateUi(w_CreateProjet)

        QMetaObject.connectSlotsByName(w_CreateProjet)

    # setupUi

    def retranslateUi(self, w_CreateProjet):
        w_CreateProjet.setWindowTitle(
            QCoreApplication.translate("w_CreateProjet", "Creaza proiect", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("w_CreateProjet", "Creaza un proiect nou", None)
        )
        # if QT_CONFIG(tooltip)
        self.lb_Vat_Mode.setToolTip(
            QCoreApplication.translate("w_CreateProjet", "Mod TVA", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_Vat_Mode.setText(
            QCoreApplication.translate("w_CreateProjet", "Mod TVA", None)
        )
        self.lb_caen_code.setText(
            QCoreApplication.translate("w_CreateProjet", "Cod CAEN", None)
        )
        # if QT_CONFIG(tooltip)
        self.lb_NRC.setToolTip(
            QCoreApplication.translate(
                "w_CreateProjet", "Numar inregistrare la Registrul Comertului", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_NRC.setText(QCoreApplication.translate("w_CreateProjet", "NRC", None))
        # if QT_CONFIG(tooltip)
        self.lb_CIF.setToolTip(
            QCoreApplication.translate(
                "w_CreateProjet", "Cod de identificare fiscala", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_CIF.setText(QCoreApplication.translate("w_CreateProjet", "CIF", None))
        self.pb_Cancel.setText(
            QCoreApplication.translate("w_CreateProjet", "Creeaza", None)
        )
        # if QT_CONFIG(tooltip)
        self.lb_namel.setToolTip(
            QCoreApplication.translate("w_CreateProjet", "Numele societatii", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_namel.setText(
            QCoreApplication.translate("w_CreateProjet", "Nume", None)
        )
        self.pb_Create.setText(
            QCoreApplication.translate("w_CreateProjet", "Inapoi", None)
        )
        self.cb_VAT_Mode.setItemText(
            0, QCoreApplication.translate("w_CreateProjet", "TVA La Facturare", None)
        )
        self.cb_VAT_Mode.setItemText(
            1, QCoreApplication.translate("w_CreateProjet", "TVA La incasare", None)
        )
        self.cb_VAT_Mode.setItemText(
            2, QCoreApplication.translate("w_CreateProjet", "Neplatitor TVA", None)
        )

        # if QT_CONFIG(tooltip)
        self.cb_VAT_Mode.setToolTip(
            QCoreApplication.translate("w_CreateProjet", "Mod TVA", None)
        )


# endif // QT_CONFIG(tooltip)
# retranslateUi
