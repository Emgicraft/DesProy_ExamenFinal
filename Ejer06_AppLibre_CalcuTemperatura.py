# -*- coding: utf-8 -*-
"""
Ejercicio 06 - Aplicación Libre - Calculadora de Temperaturas

@author: Magh
"""

import pyttsx3
import PyQt5.QtWidgets as qw

from Forms.AppLibre01_CalcuTemperatura import Ui_CalcuTemperatura


class ProyCalcuTemp(qw.QWidget):
    def __init__(self):
        qw.QWidget.__init__(self)

        self.ventana=Ui_CalcuTemperatura()
        self.ventana.setupUi(self)

        self.ventana.bCalcular.clicked.connect(self.convertir)

        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[3].id)

    def hablar(self, _texto):
        self.engine.say(_texto)
        self.engine.runAndWait()

    def mostrar(self, *_txt): #1.txtActual / 2.txtRes / 3.txtBox
        self.ventana.txtSalida.setText(_txt[1])
        palabras=_txt[2].split(" ")
        self.hablar(_txt[0]+" grados "+palabras[0]+" equivalen a "+_txt[1]+" grados "+palabras[2])

    def convertir(self):
        txtActual=self.ventana.listaConversiones.currentText()
        if txtActual=="Convertir...":
            self.hablar("Por favor, seleccione una opción de conversión.")
        elif txtActual=="Celsius a Kelvin":
            self.mostrar(self.ventana.txtEntrada.text(), str(round(float(self.ventana.txtEntrada.text())+273.15, 3)), txtActual)
        elif txtActual=="Celsius a Fahrenheit":
            self.mostrar(self.ventana.txtEntrada.text(), str(round(float(self.ventana.txtEntrada.text())*(9/5)+32.0, 3)), txtActual)
        elif txtActual=="Celsius a Rankine":
            self.mostrar(self.ventana.txtEntrada.text(), str(round(float(self.ventana.txtEntrada.text())*(9/5)+491.67, 3)), txtActual)
        elif txtActual=="Kelvin a Celsius":
            self.mostrar(self.ventana.txtEntrada.text(), str(round(float(self.ventana.txtEntrada.text())-273.15, 3)), txtActual)
        elif txtActual=="Kelvin a Fahrenheit":
            self.mostrar(self.ventana.txtEntrada.text(), str(round(((float(self.ventana.txtEntrada.text())-273.15)*(9/5))+32.0, 3)), txtActual)
        elif txtActual=="Kelvin a Rankine":
            self.mostrar(self.ventana.txtEntrada.text(), str(round(((float(self.ventana.txtEntrada.text())-273.15)*(9/5))+491.67, 3)), txtActual)
        elif txtActual=="Fahrenheit a Celsius":
            self.mostrar(self.ventana.txtEntrada.text(), str(round((float(self.ventana.txtEntrada.text())-32.0)*(5/9), 3)), txtActual)
        elif txtActual=="Fahrenheit a Kelvin":
            self.mostrar(self.ventana.txtEntrada.text(), str(round(((float(self.ventana.txtEntrada.text())-32.0)*(5/9))+273.15, 3)), txtActual)
        elif txtActual=="Fahrenheit a Rankine":
            self.mostrar(self.ventana.txtEntrada.text(), str(round(float(self.ventana.txtEntrada.text())+459.67, 3)), txtActual)


def main():
    from sys import argv, exit

    app = qw.QApplication(argv)
    sisDomIntel=ProyCalcuTemp()
    sisDomIntel.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()