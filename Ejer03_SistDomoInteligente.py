# -*- coding: utf-8 -*-
"""
Ejercicio 03 - Sistema Domótico Inteligente

@author: Magh
"""

from functools import partial

import serial
import pyttsx3
import PyQt5.QtWidgets as qw
import speech_recognition as sr

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
        self.ventana.bEscuchar.clicked.connect(self.escucharOrden)

        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[3].id)

    def hablar(self, _texto):
        self.engine.say(_texto)
        self.engine.runAndWait()

    def escuchar(self):
        self.hablar("Micrófono Activado")
        self.ventana.txt1.setText("Estado: Micrófono activado")
        r = sr.Recognizer()

        with sr.Microphone() as source:
            self.ventana.txt1.setText('Esperando orden...')
            self.hablar("Dicte la orden.")
            audioE = r.listen(source)
            try:
                textoR = r.recognize_google(audioE)
                self.ventana.txt1.setText("Usted ordenó: {}".format(textoR))
                self.hablar("Usted ordenó: {}".format(textoR))
            except:
                self.ventana.txt1.setText('No se escuchó la orden.')

        return textoR

    def escucharOrden(self):
        orden=self.escuchar().lower()
        if orden=='puerto 4' or orden=='puerto cuatro':
            self.ventana.listaPuertos.setCurrentText(self.ventana.listaPuertos.itemText(3))
        elif orden=='conectar' or orden=='connector' or orden=='connect':
            self.iniciaPuerto()
        elif orden=='desconectar' or orden=='disconnect':
            self.cierraPuerto()
        elif orden=='controller 1' or orden=='controller uno' or orden=='controla uno' or orden=='controla 1' or orden=='controlar 1' or orden=='controlla uno' or orden=='controlla 1' or orden=='verde uno' or orden=='verde 1':
            self.controlaLed("1")
        elif orden=='controller 2' or orden=='controller dos' or orden=='controla dos' or orden=='controla 2' or orden=='controlar 2' or orden=='controlla dos' or orden=='controlla 2' or orden=='verde dos' or orden=='verde 2':
            self.controlaLed("2")
        elif orden=='controller 3' or orden=='controller tres' or orden=='controla tres' or orden=='controla 3' or orden=='controlar 3' or orden=='controlla tres' or orden=='controlla 3' or orden=='verde tres' or orden=='verde 3':
            self.controlaLed("3")
        elif orden=='controller 4' or orden=='controller cuatro' or orden=='controla cuatro' or orden=='controla 4' or orden=='controlar 4' or orden=='controlla cuatro' or orden=='controlla 4' or orden=='verde cuatro' or orden=='verde 4':
            self.controlaLed("4")
        elif orden=='apagar' or orden=='apagar sistema':
            self.apagarSistema()
        else:
            self.ventana.txt1.setText('Vuelva a intentarlo.')
            self.hablar('No se entendió la orden. Vuelva a intentarlo.')

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