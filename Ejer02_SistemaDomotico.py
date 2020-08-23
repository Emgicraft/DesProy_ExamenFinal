# -*- coding: utf-8 -*-
"""
Ejercicio 02 - Sistema Domótico

@author: Magh
"""

from functools import partial
import serial

from numpy import sqrt
from PyQt5 import QtGui, QtCore
import PyQt5.QtWidgets as qw

from Forms.DomoticaArduino_01 import Ui_SisDomArduino

class ProySisDom(qw.QWidget):
    #puertoSerial=None
    def __init__(self):
        qw.QWidget.__init__(self)

        self.ventana=Ui_SisDomArduino()
        self.ventana.setupUi(self)

        self.ventana.bConect.clicked.connect(self.iniciaPuerto)
        self.ventana.bDesconect.clicked.connect(self.cierraPuerto)
        #self.ventana.bLed1.clicked.connect(self)
        self.ventana.bSalir.clicked.connect(self.apagarSistema)

    def iniciaPuerto(self):
        try:
            print("Iniciando Puerto "+self.ventana.listaPuertos.currentText()+"...")
            self.puertoSerial=serial.Serial(port=self.ventana.listaPuertos.currentText(), baudrate=9600)
            self.ventana.bDesconect.setEnabled(True)
            self.ventana.bConect.setEnabled(False)
            print("Puerto "+self.ventana.listaPuertos.currentText()+" iniciado.")
        except:
            print("Error! Fallo al conectar con el puerto "+self.ventana.listaPuertos.currentText())
            self.ventana.bDesconect.setEnabled(False)
            self.ventana.bConect.setEnabled(True)

    def cierraPuerto(self):
        self.ventana.bDesconect.setEnabled(False)
        self.ventana.bConect.setEnabled(True)
        self.puertoSerial.close()
        print("Puerto "+self.ventana.listaPuertos.currentText()+" cerrado.")

    def apagarSistema(self):
        try:
            print("Verificando puertos abiertos...")
            self.cierraPuerto()
            print("Puertos cerrados.")
        except:
            print("No se inició ningún puerto. Cerrando...")
        #Con cualquiera de las siguiente líneas funciona para cerrar la ventana:
        #self.ProySisDom.close()
        qw.QApplication.instance().quit() #Pero este no da errores.

def main():
    from sys import argv, exit

    app = qw.QApplication(argv)
    sisDom=ProySisDom()
    sisDom.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()