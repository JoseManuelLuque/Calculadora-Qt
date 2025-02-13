# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QHeaderView, QLCDNumber, QLayout, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Calculadora(object):
    def setupUi(self, Calculadora):
        if not Calculadora.objectName():
            Calculadora.setObjectName(u"Calculadora")
        Calculadora.setEnabled(True)
        Calculadora.resize(600, 556)
        Calculadora.setMinimumSize(QSize(600, 556))
        Calculadora.setStyleSheet(u"\n"
"QDialog {\n"
"    background-color: #444040;\n"
"}\n"
"QPushButton {\n"
"    background-color: #e58900;\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 26px;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7f4c00;\n"
"}\n"
"QLCDNumber {\n"
"    background-color: rgb(49, 53, 69);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QTableWidget {\n"
"    background-color: rgb(49, 53, 69);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 16px;\n"
"}\n"
"/* Esta es la parte del encabezado de la tabla */\n"
"QHeaderView::section {\n"
"    background-color: #555555;\n"
"    color: #ffffff;\n"
"    padding: 4px;\n"
"    border: 1px solid #444444;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(Calculadora)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ColumnaPrincipalApp = QVBoxLayout()
        self.ColumnaPrincipalApp.setSpacing(6)
        self.ColumnaPrincipalApp.setObjectName(u"ColumnaPrincipalApp")
        self.ColumnaPrincipalApp.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.ColumnaPrincipalApp.setContentsMargins(12, 12, 12, 12)
        self.lcdNumber = QLCDNumber(Calculadora)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)

        self.ColumnaPrincipalApp.addWidget(self.lcdNumber)

        self.Botones = QGridLayout()
        self.Botones.setObjectName(u"Botones")
        self.botonParentesisIzq = QPushButton(Calculadora)
        self.botonParentesisIzq.setObjectName(u"botonParentesisIzq")

        self.Botones.addWidget(self.botonParentesisIzq, 0, 0, 1, 1)

        self.botonParentesisDer = QPushButton(Calculadora)
        self.botonParentesisDer.setObjectName(u"botonParentesisDer")

        self.Botones.addWidget(self.botonParentesisDer, 0, 1, 1, 1)

        self.botonRaiz = QPushButton(Calculadora)
        self.botonRaiz.setObjectName(u"botonRaiz")

        self.Botones.addWidget(self.botonRaiz, 0, 2, 1, 1)

        self.botonEliminar = QPushButton(Calculadora)
        self.botonEliminar.setObjectName(u"botonEliminar")

        self.Botones.addWidget(self.botonEliminar, 0, 3, 1, 1)

        self.boton7 = QPushButton(Calculadora)
        self.boton7.setObjectName(u"boton7")

        self.Botones.addWidget(self.boton7, 1, 0, 1, 1)

        self.boton8 = QPushButton(Calculadora)
        self.boton8.setObjectName(u"boton8")

        self.Botones.addWidget(self.boton8, 1, 1, 1, 1)

        self.boton9 = QPushButton(Calculadora)
        self.boton9.setObjectName(u"boton9")

        self.Botones.addWidget(self.boton9, 1, 2, 1, 1)

        self.botonD = QPushButton(Calculadora)
        self.botonD.setObjectName(u"botonD")

        self.Botones.addWidget(self.botonD, 1, 3, 1, 1)

        self.boton4 = QPushButton(Calculadora)
        self.boton4.setObjectName(u"boton4")

        self.Botones.addWidget(self.boton4, 2, 0, 1, 1)

        self.boton5 = QPushButton(Calculadora)
        self.boton5.setObjectName(u"boton5")

        self.Botones.addWidget(self.boton5, 2, 1, 1, 1)

        self.boton6 = QPushButton(Calculadora)
        self.boton6.setObjectName(u"boton6")

        self.Botones.addWidget(self.boton6, 2, 2, 1, 1)

        self.botonM = QPushButton(Calculadora)
        self.botonM.setObjectName(u"botonM")

        self.Botones.addWidget(self.botonM, 2, 3, 1, 1)

        self.boton1 = QPushButton(Calculadora)
        self.boton1.setObjectName(u"boton1")

        self.Botones.addWidget(self.boton1, 3, 0, 1, 1)

        self.boton2 = QPushButton(Calculadora)
        self.boton2.setObjectName(u"boton2")

        self.Botones.addWidget(self.boton2, 3, 1, 1, 1)

        self.boton3 = QPushButton(Calculadora)
        self.boton3.setObjectName(u"boton3")

        self.Botones.addWidget(self.boton3, 3, 2, 1, 1)

        self.botonR = QPushButton(Calculadora)
        self.botonR.setObjectName(u"botonR")

        self.Botones.addWidget(self.botonR, 3, 3, 1, 1)

        self.boton0 = QPushButton(Calculadora)
        self.boton0.setObjectName(u"boton0")

        self.Botones.addWidget(self.boton0, 4, 0, 1, 1)

        self.botonComa = QPushButton(Calculadora)
        self.botonComa.setObjectName(u"botonComa")

        self.Botones.addWidget(self.botonComa, 4, 1, 1, 1)

        self.botonPorcentaje = QPushButton(Calculadora)
        self.botonPorcentaje.setObjectName(u"botonPorcentaje")

        self.Botones.addWidget(self.botonPorcentaje, 4, 2, 1, 1)

        self.botonS = QPushButton(Calculadora)
        self.botonS.setObjectName(u"botonS")

        self.Botones.addWidget(self.botonS, 4, 3, 1, 1)

        self.botonCE = QPushButton(Calculadora)
        self.botonCE.setObjectName(u"botonCE")

        self.Botones.addWidget(self.botonCE, 5, 0, 1, 2)

        self.BotonIgual = QPushButton(Calculadora)
        self.BotonIgual.setObjectName(u"BotonIgual")

        self.Botones.addWidget(self.BotonIgual, 5, 2, 1, 2)


        self.ColumnaPrincipalApp.addLayout(self.Botones)


        self.horizontalLayout.addLayout(self.ColumnaPrincipalApp)

        self.tablaOperaciones = QTableWidget(Calculadora)
        if (self.tablaOperaciones.columnCount() < 2):
            self.tablaOperaciones.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaOperaciones.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaOperaciones.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tablaOperaciones.setObjectName(u"tablaOperaciones")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tablaOperaciones.sizePolicy().hasHeightForWidth())
        self.tablaOperaciones.setSizePolicy(sizePolicy1)
        self.tablaOperaciones.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.tablaOperaciones)


        self.retranslateUi(Calculadora)

        QMetaObject.connectSlotsByName(Calculadora)
    # setupUi

    def retranslateUi(self, Calculadora):
        Calculadora.setWindowTitle(QCoreApplication.translate("Calculadora", u"Calculadora", None))
        self.botonParentesisIzq.setText(QCoreApplication.translate("Calculadora", u"(", None))
        self.botonParentesisDer.setText(QCoreApplication.translate("Calculadora", u")", None))
        self.botonRaiz.setText(QCoreApplication.translate("Calculadora", u"\u221a", None))
        self.botonEliminar.setText(QCoreApplication.translate("Calculadora", u"DEL", None))
        self.boton7.setText(QCoreApplication.translate("Calculadora", u"7", None))
        self.boton8.setText(QCoreApplication.translate("Calculadora", u"8", None))
        self.boton9.setText(QCoreApplication.translate("Calculadora", u"9", None))
        self.botonD.setText(QCoreApplication.translate("Calculadora", u"/", None))
        self.boton4.setText(QCoreApplication.translate("Calculadora", u"4", None))
        self.boton5.setText(QCoreApplication.translate("Calculadora", u"5", None))
        self.boton6.setText(QCoreApplication.translate("Calculadora", u"6", None))
        self.botonM.setText(QCoreApplication.translate("Calculadora", u"*", None))
        self.boton1.setText(QCoreApplication.translate("Calculadora", u"1", None))
        self.boton2.setText(QCoreApplication.translate("Calculadora", u"2", None))
        self.boton3.setText(QCoreApplication.translate("Calculadora", u"3", None))
        self.botonR.setText(QCoreApplication.translate("Calculadora", u"-", None))
        self.boton0.setText(QCoreApplication.translate("Calculadora", u"0", None))
        self.botonComa.setText(QCoreApplication.translate("Calculadora", u",", None))
        self.botonPorcentaje.setText(QCoreApplication.translate("Calculadora", u"%", None))
        self.botonS.setText(QCoreApplication.translate("Calculadora", u"+", None))
        self.botonCE.setText(QCoreApplication.translate("Calculadora", u"CE", None))
        self.BotonIgual.setText(QCoreApplication.translate("Calculadora", u"=", None))
        ___qtablewidgetitem = self.tablaOperaciones.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Calculadora", u"Operaci\u00f3n", None));
        ___qtablewidgetitem1 = self.tablaOperaciones.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Calculadora", u"Resultado", None));
    # retranslateUi

