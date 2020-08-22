# -*- coding: utf-8 -*-
"""
Ejercicio 01 - Calculadora Básica

@author: Magh
"""

from functools import partial
from PyQt5 import QtGui, QtCore
import PyQt5.QtWidgets as qw

from venCalcu import Ui_VenCalcu

class ProyCalcu(qw.QWidget):
    texto=res=""
    def __init__(self):
        qw.QWidget.__init__(self)

        self.ventana=Ui_VenCalcu()
        self.ventana.setupUi(self)

        btnsNum = {'bNum0':self.ventana.bNum0,
                'bNum1':self.ventana.bNum1,
                'bNum2':self.ventana.bNum2,
                'bNum3':self.ventana.bNum3,
                'bNum4':self.ventana.bNum4,
                'bNum5':self.ventana.bNum5,
                'bNum6':self.ventana.bNum6,
                'bNum7':self.ventana.bNum7,
                'bNum8':self.ventana.bNum8,
                'bNum9':self.ventana.bNum9}
        for i in range(10):
            self.iniciarConect(btnsNum["bNum"+str(i)], txtPantalla=True)
        self.iniciarConect(self.ventana.bsParentAbrir,
                        self.ventana.bsParentCerrar, txtPantalla=True)
        self.iniciarConect(self.ventana.bPorcentaje,
                        self.ventana.bPunto,
                        self.ventana.boSumar,
                        self.ventana.boBorrar,
                        self.ventana.boLimpiar,
                        self.ventana.boRestar,
                        self.ventana.boMultiplicar,
                        self.ventana.boPotencia,
                        self.ventana.boRaiz,
                        self.ventana.boDividir,
                        self.ventana.boCalcular)
        self.ventana.boLimpiar.pressed.connect(self.ventana.pantallaCalcu.clear)
        #self.ventana.boLimpiar.pressed.connect(self.borrarPantalla)

    def escribePantalla(self, obj):
        if isinstance(obj, qw.QPushButton):
            #self.ventana.pantallaCalcu.appendPlainText(self.texto)
            self.res+=obj.text()
            self.ventana.pantallaCalcu.setPlainText(self.res)
            #self.ventana.pantallaCalcu.setPlainText(obj.text())
        elif isinstance(obj, str):
            self.ventana.pantallaCalcu.setPlainText(obj)
        else:
            print("<func: escribirPantalla> Error! No se reconoció el parámetro.")

    def cargarRes(self):
        self.ventana.pantallaCalcu.clear()
        self.res+=self.texto
        self.texto=""
    
    def iniciarConect(self, *botones, txtPantalla=False):
        if txtPantalla:
            for btn in botones:
                #btn.pressed.connect(lambda: self.escribePantalla(btn))
                btn.pressed.connect(partial(self.escribePantalla, btn))
                print(btn.text())
    
    def borraCaracter(self, cadena):
        cadena[::-1].replace(cadena[::-1][0], "", 1)[::-1]
        self.ventana.pantallaCalcu.setPlainText(self.res)


def main():
    from sys import argv, exit
    
    app = qw.QApplication(argv)
    calcu=ProyCalcu()
    calcu.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()