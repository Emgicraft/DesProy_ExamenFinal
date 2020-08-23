# -*- coding: utf-8 -*-
"""
Ejercicio 03 - Sistema Domótico Inteligente

@author: Magh
"""

from functools import partial

import serial
import pyttsx3
from PyQt5 import QtGui, QtCore, QtMultimedia
import PyQt5.QtWidgets as qw

from Forms.DomoticaArduino_02 import Ui_SisDomArduino

class ProySisDomIntel(qw.QWidget):
    def __init__(self):
        qw.QWidget.__init__(self)

        self.ventana=Ui_SisDomArduino()
        self.ventana.setupUi(self)

        self.ventana.bConect.clicked.connect(self.iniciaPuerto)
        self.ventana.bDesconect.clicked.connect(self.cierraPuerto)
        self.ventana.bSalir.clicked.connect(self.apagarSistema)
        self.ventana.bLed1.clicked.connect(partial(self.controlaLed, "1"))
        self.ventana.bLed2.clicked.connect(partial(self.controlaLed, "2"))
        self.ventana.bLed3.clicked.connect(partial(self.controlaLed, "3"))
        self.ventana.bLed4.clicked.connect(partial(self.controlaLed, "4"))

        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[3].id)

    def hablar(self, _texto):
        self.engine.say(_texto)
        self.engine.runAndWait()

    def iniciaPuerto(self):
        try:
            #print("Iniciando Puerto "+self.ventana.listaPuertos.currentText()+"...")
            self.hablar("Iniciando Puerto "+self.ventana.listaPuertos.currentText())
            self.puertoSerial=serial.Serial(port=self.ventana.listaPuertos.currentText(), baudrate=9600)
            self.ventana.bDesconect.setEnabled(True)
            self.ventana.bConect.setEnabled(False)
            #print("Puerto "+self.ventana.listaPuertos.currentText()+" iniciado.")
            self.hablar("Puerto "+self.ventana.listaPuertos.currentText()+" iniciado.")
        except:
            #print("Error! Fallo al conectar con el puerto "+self.ventana.listaPuertos.currentText())
            self.hablar("Error! Fallo al conectar con el puerto "+self.ventana.listaPuertos.currentText())
            self.ventana.bDesconect.setEnabled(False)
            self.ventana.bConect.setEnabled(True)

    def cierraPuerto(self):
        self.ventana.bDesconect.setEnabled(False)
        self.ventana.bConect.setEnabled(True)
        self.puertoSerial.close()
        #print("Puerto "+self.ventana.listaPuertos.currentText()+" cerrado.")
        self.hablar("Puerto "+self.ventana.listaPuertos.currentText()+" cerrado.")

    def controlaLed(self, numLed):
        self.hablar("Led "+numLed)
        self.puertoSerial.write(numLed.encode('ascii'))

    def apagarSistema(self):
        try:
            #print("Verificando puertos abiertos...")
            self.hablar("Verificando puertos abiertos.")
            self.cierraPuerto()
            #print("Puertos cerrados.")
            self.hablar("Puertos cerrados. Apagando sistema.")
        except:
            #print("No se inició ningún puerto. Cerrando...")
            self.hablar("No se inició ningún puerto. Apagando sistema.")
        qw.QApplication.instance().quit()


def main():
    from sys import argv, exit

    app = qw.QApplication(argv)
    sisDomIntel=ProySisDomIntel()
    sisDomIntel.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()