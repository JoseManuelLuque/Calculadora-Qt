import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore
from Calculadora_ui import Ui_Calculadora
import math

class MainWindow(QDialog, Ui_Calculadora):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Calculadora")

        # Establecer el ícono de la ventana
        self.setWindowIcon(QIcon('icono.ico'))

        # Permitir que la ventana se maximice
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowType.WindowMaximizeButtonHint)

        # Establecer tamaño mínimo de la ventana
        self.setMinimumSize(600, 556)

        # Cargar estilos desde un archivo externo
        with open("styles.qss", "r") as f:
            self.setStyleSheet(f.read())

        # Conectar botones a funciones
        self.boton0.clicked.connect(lambda: self.numero_presionado('0'))
        self.boton1.clicked.connect(lambda: self.numero_presionado('1'))
        self.boton2.clicked.connect(lambda: self.numero_presionado('2'))
        self.boton3.clicked.connect(lambda: self.numero_presionado('3'))
        self.boton4.clicked.connect(lambda: self.numero_presionado('4'))
        self.boton5.clicked.connect(lambda: self.numero_presionado('5'))
        self.boton6.clicked.connect(lambda: self.numero_presionado('6'))
        self.boton7.clicked.connect(lambda: self.numero_presionado('7'))
        self.boton8.clicked.connect(lambda: self.numero_presionado('8'))
        self.boton9.clicked.connect(lambda: self.numero_presionado('9'))
        self.botonComa.clicked.connect(lambda: self.numero_presionado('.'))
        self.botonParentesisIzq.clicked.connect(lambda: self.numero_presionado('('))
        self.botonParentesisDer.clicked.connect(lambda: self.numero_presionado(')'))
        self.botonPorcentaje.clicked.connect(lambda: self.numero_presionado('%'))
        self.botonRaiz.clicked.connect(self.raiz_cuadrada)
        self.botonEliminar.clicked.connect(self.eliminar)

        self.botonS.clicked.connect(lambda: self.operacion_presionada('+'))
        self.botonR.clicked.connect(lambda: self.operacion_presionada('-'))
        self.botonM.clicked.connect(lambda: self.operacion_presionada('*'))
        self.botonD.clicked.connect(lambda: self.operacion_presionada('/'))

        self.BotonIgual.clicked.connect(self.calcular_resultado)

        self.operacion = ''
        self.primer_numero = ''
        self.segundo_numero = ''

        # Configurar la tabla de operaciones
        self.tablaOperaciones.setColumnCount(2)
        self.tablaOperaciones.setHorizontalHeaderLabels(["Operación", "Resultado"])

        self.show()

    def numero_presionado(self, numero):
        # Lógica para manejar el número presionado
        if self.operacion == '':
            self.primer_numero += numero
            self.lcdNumber.display(self.primer_numero)
        else:
            self.segundo_numero += numero
            self.lcdNumber.display(self.segundo_numero)

    def operacion_presionada(self, operacion):
        # Lógica para manejar la operación presionada
        if self.primer_numero != '':
            self.operacion = operacion

    def calcular_resultado(self):
        # Lógica para calcular el resultado
        try:
            if self.operacion == '%':
                resultado = eval(f"{self.primer_numero} / 100")
            else:
                resultado = eval(self.primer_numero + self.operacion + self.segundo_numero)
            self.lcdNumber.display(resultado)
            self.agregar_operacion(self.primer_numero + self.operacion + self.segundo_numero, resultado)
            self.primer_numero = str(resultado)
            self.segundo_numero = ''
            self.operacion = ''
        except Exception as e:
            self.mostrar_error("Operación no válida")

    def raiz_cuadrada(self):
        # Lógica para calcular la raíz cuadrada
        try:
            if self.operacion == '':
                resultado = math.sqrt(float(self.primer_numero))
                self.lcdNumber.display(resultado)
                self.primer_numero = str(resultado)
            else:
                resultado = math.sqrt(float(self.segundo_numero))
                self.lcdNumber.display(resultado)
                self.segundo_numero = str(resultado)
        except Exception as e:
            self.mostrar_error("Operación no válida")

    def eliminar(self):
        # Lógica para eliminar el último carácter
        if self.operacion == '':
            self.primer_numero = self.primer_numero[:-1]
            self.lcdNumber.display(self.primer_numero)
        else:
            self.segundo_numero = self.segundo_numero[:-1]
            self.lcdNumber.display(self.segundo_numero)

    def mostrar_error(self, mensaje):
        # Mostrar mensaje de error
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(mensaje)
        msg.setWindowTitle("Error")
        msg.exec()
        self.primer_numero = ''
        self.segundo_numero = ''
        self.operacion = ''
        self.lcdNumber.display('')

    def agregar_operacion(self, operacion, resultado):
        # Agregar operación válida a la tabla
        row_position = self.tablaOperaciones.rowCount()
        self.tablaOperaciones.insertRow(row_position)
        self.tablaOperaciones.setItem(row_position, 0, QTableWidgetItem(operacion))
        self.tablaOperaciones.setItem(row_position, 1, QTableWidgetItem(str(resultado)))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Establecer el ícono de la aplicación
    app.setWindowIcon(QIcon('icono.ico'))

    w = MainWindow()
    w.show()
    app.exec()