# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppLibre01_CalcuTemperatura.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalcuTemperatura(object):
    def setupUi(self, CalcuTemperatura):
        CalcuTemperatura.setObjectName("CalcuTemperatura")
        CalcuTemperatura.resize(300, 212)
        CalcuTemperatura.setWindowTitle("Calculadora de Temperatuta")
        CalcuTemperatura.setToolTip("")
        CalcuTemperatura.setStatusTip("")
        CalcuTemperatura.setWhatsThis("")
        CalcuTemperatura.setAccessibleName("")
        CalcuTemperatura.setAccessibleDescription("")
        CalcuTemperatura.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        CalcuTemperatura.setWindowFilePath("")
        CalcuTemperatura.setWindowIcon(QtGui.QIcon('./Recursos/MCServer-icon-64x64.png'))

        self.listaConversiones = QtWidgets.QComboBox(CalcuTemperatura)
        self.listaConversiones.setGeometry(QtCore.QRect(70, 60, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.listaConversiones.setFont(font)
        self.listaConversiones.setToolTip("")
        self.listaConversiones.setStatusTip("")
        self.listaConversiones.setWhatsThis("")
        self.listaConversiones.setAccessibleName("")
        self.listaConversiones.setAccessibleDescription("")
        self.listaConversiones.setCurrentText("Convertir...")
        self.listaConversiones.setPlaceholderText("Convertir...")
        self.listaConversiones.setObjectName("listaConversiones")
        self.listaConversiones.addItem("")
        self.listaConversiones.setItemText(0, "Celsius a Kelvin")
        self.listaConversiones.addItem("")
        self.listaConversiones.setItemText(1, "Celsius a Fahrenheit")
        self.listaConversiones.addItem("")
        self.listaConversiones.setItemText(2, "Celsius a Rankine")
        self.listaConversiones.addItem("")
        self.listaConversiones.setItemText(3, "Kelvin a Celsius")
        self.listaConversiones.addItem("")
        self.listaConversiones.setItemText(4, "Kelvin a Fahrenheit")
        self.listaConversiones.addItem("")
        self.listaConversiones.setItemText(5, "Kelvin a Rankine")
        self.listaConversiones.addItem("")
        self.listaConversiones.setItemText(6, "Fahrenheit a Celsius")
        self.listaConversiones.addItem("")
        self.listaConversiones.setItemText(7, "Fahrenheit a Kelvin")
        self.listaConversiones.addItem("")
        self.listaConversiones.setItemText(8, "Fahrenheit a Rankine")
        self.txtEntrada = QtWidgets.QLineEdit(CalcuTemperatura)
        self.txtEntrada.setGeometry(QtCore.QRect(10, 110, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.txtEntrada.setFont(font)
        self.txtEntrada.setToolTip("Aquí escriba el valor que quiere convertir.")
        self.txtEntrada.setStatusTip("")
        self.txtEntrada.setWhatsThis("")
        self.txtEntrada.setAccessibleName("")
        self.txtEntrada.setAccessibleDescription("")
        self.txtEntrada.setText("")
        self.txtEntrada.setPlaceholderText("Valor a convertir")
        self.txtEntrada.setObjectName("txtEntrada")
        self.bCalcular = QtWidgets.QPushButton(CalcuTemperatura)
        self.bCalcular.setGeometry(QtCore.QRect(90, 160, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.bCalcular.setFont(font)
        self.bCalcular.setToolTip("Calcular")
        self.bCalcular.setStatusTip("")
        self.bCalcular.setWhatsThis("")
        self.bCalcular.setAccessibleName("")
        self.bCalcular.setAccessibleDescription("")
        self.bCalcular.setText("Calcular")
        self.bCalcular.setShortcut("Return, Enter")
        self.bCalcular.setObjectName("bCalcular")
        self.titulo1 = QtWidgets.QLabel(CalcuTemperatura)
        self.titulo1.setGeometry(QtCore.QRect(20, 20, 260, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.titulo1.setFont(font)
        self.titulo1.setToolTip("")
        self.titulo1.setStatusTip("")
        self.titulo1.setWhatsThis("")
        self.titulo1.setAccessibleName("")
        self.titulo1.setAccessibleDescription("")
        self.titulo1.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.titulo1.setObjectName("titulo1")
        
        self.txtSalida = QtWidgets.QLineEdit(CalcuTemperatura)
        self.txtSalida.setGeometry(QtCore.QRect(160, 110, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.txtSalida.setFont(font)
        self.txtSalida.setToolTip("Aquí verá el valor convertido.")
        self.txtSalida.setStatusTip("")
        self.txtSalida.setWhatsThis("")
        self.txtSalida.setAccessibleName("")
        self.txtSalida.setAccessibleDescription("")
        self.txtSalida.setText("")
        self.txtSalida.setReadOnly(True)
        self.txtSalida.setPlaceholderText("Valor convertido")
        self.txtSalida.setObjectName("txtSalida")

        self.retranslateUi(CalcuTemperatura)
        QtCore.QMetaObject.connectSlotsByName(CalcuTemperatura)

    def retranslateUi(self, CalcuTemperatura):
        _translate = QtCore.QCoreApplication.translate
        self.titulo1.setText(_translate("CalcuTemperatura", "Conversión de Temperatura"))
