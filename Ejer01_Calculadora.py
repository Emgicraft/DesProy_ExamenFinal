# -*- coding: utf-8 -*-
"""
Ejercicio 01 - Calculadora Básica

@author: Magh
"""

from functools import partial
from numpy import sqrt
from PyQt5 import QtGui, QtCore
import PyQt5.QtWidgets as qw

from venCalcu import Ui_VenCalcu

class ProyCalcu(qw.QWidget):
    caract=res=temp=mem=""
    def __init__(self):
        qw.QWidget.__init__(self)

        self.ventana=Ui_VenCalcu()
        self.ventana.setupUi(self)

        self.iniciarConect(self.ventana.bNum0,
                        self.ventana.bNum1,
                        self.ventana.bNum2,
                        self.ventana.bNum3,
                        self.ventana.bNum4,
                        self.ventana.bNum5,
                        self.ventana.bNum6,
                        self.ventana.bNum7,
                        self.ventana.bNum8,
                        self.ventana.bNum9,
                        self.ventana.bsParentAbrir,
                        self.ventana.bsParentCerrar,
                        self.ventana.bPunto, txtPantalla=True)

        btnsEsp={'Porcentaje':self.ventana.bPorcentaje,
                        'Suma':self.ventana.boSumar,
                        'Borra':self.ventana.boBorrar,
                        'Limpia':self.ventana.boLimpiar,
                        'Resta':self.ventana.boRestar,
                        'Multi':self.ventana.boMultiplicar,
                        'Pot2':self.ventana.boPotencia,
                        'Raiz':self.ventana.boRaiz,
                        'Divide':self.ventana.boDividir,
                        'Calcula':self.ventana.boCalcular}
        self.iniciarConect(btnsEsp)

    def escribePantalla(self, obj):
        self.ventana.pantallaCalcu.clear()
        if isinstance(obj, qw.QPushButton):
            if self.mem=="":
                self.res+=obj.text()
                self.ventana.pantallaCalcu.setPlainText(self.res)
            else:
                self.res=self.mem
                self.res+=obj.text()
                self.ventana.pantallaCalcu.setPlainText(self.res)
                self.mem=""
        elif isinstance(obj, str):
            self.ventana.pantallaCalcu.setPlainText(obj)
        else:
            print("<func: escribirPantalla>Error! No se reconoció el parámetro.")

    def cargarRes(self):
        self.res+=self.caract
        self.caract=""
        self.ventana.pantallaCalcu.clear()

    def borraCaracter(self, cadena):
        cadena=cadena[::-1].replace(cadena[::-1][0], "", 1)[::-1]
        return cadena
    
    def operar(self, cad):
        if cad=='Porcentaje':
            self.mem=str(float(self.res)/100)
            self.escribePantalla(self.mem)
        elif cad=='Suma':
            if self.mem=="":
                self.temp=self.res
            else:
                self.temp=self.mem
            self.escribePantalla(self.ventana.boSumar)
        elif cad=='Borra':
            self.res=self.borraCaracter(self.res)
            self.escribePantalla(self.res)
        elif cad=='Limpia':
            self.ventana.pantallaCalcu.clear()
            self.res=self.temp=self.mem=""
        elif cad=='Resta':
            if self.mem=="":
                self.temp=self.res
            else:
                self.temp=self.mem
            self.escribePantalla(self.ventana.boRestar)
        elif cad=='Multi':
            if self.mem=="":
                self.temp=self.res
            else:
                self.temp=self.mem
            self.escribePantalla(self.ventana.boMultiplicar)
        elif cad=='Pot2':
            if self.mem!="":
                self.res=self.mem
            self.mem=str(float(self.res)**2)
            self.escribePantalla(self.res+"²"+"="+self.mem)
        elif cad=='Raiz':
            if self.mem!="":
                self.res=self.mem
            self.mem=str(sqrt(float(self.res)))
            self.escribePantalla("√"+self.res+"="+self.mem)
        elif cad=='Divide':
            if self.mem=="":
                self.temp=self.res
            else:
                self.temp=self.mem
            self.escribePantalla(self.ventana.boDividir)
        elif cad=='Calcula':
            if self.res.find("+")>0:
                self.res=self.res[self.res.find("+")::] #Signo + dentro de la cadena
                self.mem=str(float(self.res)+float(self.temp)) #Toma en cuenta el signo +
                self.escribePantalla(self.mem)
            elif self.res.find("-")>0:
                self.res=self.res[self.res.find("-")+1::]
                self.mem=str(float(self.temp)-float(self.res))
                self.escribePantalla(self.mem)
            elif self.res.find("*")>0:
                self.res=self.res[self.res.find("*")+1::]
                self.mem=str(float(self.res)*float(self.temp))
                self.escribePantalla(self.mem)
            elif self.res.find("/")>0:
                self.res=self.res[self.res.find("/")+1::]
                self.mem=str(float(self.temp)/float(self.res))
                self.escribePantalla(self.mem)
            self.res=self.temp=""
        else:
            print("<func: iniciarConect>Error! No se reconoce el parámetro.")

    def iniciarConect(self, *botones, txtPantalla=False):
        if txtPantalla:
            for btn in botones:
                #btn.pressed.connect(lambda: self.escribePantalla(btn))
                btn.pressed.connect(partial(self.escribePantalla, btn))
        else:
            for clv in botones[0]:
                botones[0][clv].pressed.connect(partial(self.operar, clv))


def main():
    from sys import argv, exit

    app = qw.QApplication(argv)
    calcu=ProyCalcu()
    calcu.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()