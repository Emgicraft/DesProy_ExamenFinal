# -*- coding: utf-8 -*-
"""
Ejercicio 06 - Aplicación Libre - Calculadora de Temperaturas

@author: Magh
"""

import PyQt5.QtWidgets as qw

from Forms.AppLibre01_CalcuTemperatura import Ui_CalcuTemperatura


class ProyCalcuTemp(qw.QWidget):
    def __init__(self):
        qw.QWidget.__init__(self)

        self.ventana=Ui_CalcuTemperatura()
        self.ventana.setupUi(self)


def main():
    from sys import argv, exit

    app = qw.QApplication(argv)
    sisDomIntel=ProyCalcuTemp()
    sisDomIntel.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()