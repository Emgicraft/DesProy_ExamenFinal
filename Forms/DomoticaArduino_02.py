# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DomoticaArduino_02.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SisDomArduino(object):
    def setupUi(self, SisDomArduino):
        SisDomArduino.setObjectName("SisDomArduino")
        SisDomArduino.resize(500, 400)
        SisDomArduino.setWindowIcon(QtGui.QIcon('./Recursos/MCServer-icon-64x64.png'))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        SisDomArduino.setFont(font)
        SisDomArduino.setWindowTitle("Sistema Domótico")
        SisDomArduino.setToolTip("")
        SisDomArduino.setStatusTip("")
        SisDomArduino.setWhatsThis("")
        SisDomArduino.setAccessibleName("")
        SisDomArduino.setAccessibleDescription("")
        SisDomArduino.setAutoFillBackground(False)
        SisDomArduino.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        SisDomArduino.setWindowFilePath("")
        self.bConect = QtWidgets.QPushButton(SisDomArduino)
        self.bConect.setEnabled(True)
        self.bConect.setGeometry(QtCore.QRect(30, 100, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bConect.setFont(font)
        self.bConect.setToolTip("Conectar")
        self.bConect.setStatusTip("")
        self.bConect.setWhatsThis("")
        self.bConect.setAccessibleName("")
        self.bConect.setAccessibleDescription("")
        self.bConect.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.bConect.setText("Conectar")
        self.bConect.setObjectName("bConect")
        self.bLed1 = QtWidgets.QPushButton(SisDomArduino)
        self.bLed1.setGeometry(QtCore.QRect(310, 100, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bLed1.setFont(font)
        self.bLed1.setToolTip("Controla Led 01")
        self.bLed1.setStatusTip("")
        self.bLed1.setWhatsThis("")
        self.bLed1.setAccessibleName("")
        self.bLed1.setAccessibleDescription("")
        self.bLed1.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.bLed1.setText("Led 01 On/Off")
        self.bLed1.setObjectName("bLed1")

        self.bEscuchar = QtWidgets.QPushButton(SisDomArduino)
        self.bEscuchar.setEnabled(True)
        self.bEscuchar.setGeometry(QtCore.QRect(80, 310, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bEscuchar.setFont(font)
        self.bEscuchar.setToolTip("Activar micrófono")
        self.bEscuchar.setStatusTip("")
        self.bEscuchar.setWhatsThis("")
        self.bEscuchar.setAccessibleName("")
        self.bEscuchar.setAccessibleDescription("")
        self.bEscuchar.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.bEscuchar.setText("Escuchar")
        self.bEscuchar.setObjectName("bEscuchar")

        self.bSalir = QtWidgets.QPushButton(SisDomArduino)
        self.bSalir.setGeometry(QtCore.QRect(20, 360, 460, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.bSalir.setFont(font)
        self.bSalir.setToolTip("Desconecta y Cierra la aplicación")
        self.bSalir.setStatusTip("")
        self.bSalir.setWhatsThis("")
        self.bSalir.setAccessibleName("")
        self.bSalir.setAccessibleDescription("")
        self.bSalir.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.bSalir.setText("Salir")
        self.bSalir.setObjectName("bSalir")
        self.titulo01 = QtWidgets.QLabel(SisDomArduino)
        self.titulo01.setGeometry(QtCore.QRect(40, 20, 420, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.titulo01.setFont(font)
        self.titulo01.setToolTip("")
        self.titulo01.setWhatsThis("")
        self.titulo01.setAccessibleName("")
        self.titulo01.setAccessibleDescription("")
        self.titulo01.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.titulo01.setText("Sistema Domótico con Pyhton + Arduino")
        self.titulo01.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo01.setObjectName("titulo01")
        self.titulo02 = QtWidgets.QLabel(SisDomArduino)
        self.titulo02.setGeometry(QtCore.QRect(30, 60, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.titulo02.setFont(font)
        self.titulo02.setToolTip("")
        self.titulo02.setWhatsThis("")
        self.titulo02.setAccessibleName("")
        self.titulo02.setAccessibleDescription("")
        self.titulo02.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.titulo02.setText("Comunicación Serial")
        self.titulo02.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo02.setObjectName("titulo02")
        self.listaPuertos = QtWidgets.QComboBox(SisDomArduino)
        self.listaPuertos.setGeometry(QtCore.QRect(150, 100, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.listaPuertos.setFont(font)
        self.listaPuertos.setToolTip("Selecciona el Puerto Serial a usar.")
        self.listaPuertos.setStatusTip("")
        self.listaPuertos.setWhatsThis("")
        self.listaPuertos.setAccessibleName("")
        self.listaPuertos.setAccessibleDescription("")
        self.listaPuertos.setCurrentText("Puerto")
        self.listaPuertos.setPlaceholderText("Puerto")
        self.listaPuertos.setObjectName("listaPuertos")
        self.listaPuertos.addItem("")
        self.listaPuertos.setItemText(0, "COM1")
        self.listaPuertos.addItem("")
        self.listaPuertos.setItemText(1, "COM2")
        self.listaPuertos.addItem("")
        self.listaPuertos.setItemText(2, "COM3")
        self.listaPuertos.addItem("")
        self.listaPuertos.setItemText(3, "COM4")
        self.listaPuertos.addItem("")
        self.listaPuertos.setItemText(4, "COM5")
        self.listaPuertos.addItem("")
        self.listaPuertos.setItemText(5, "COM6")
        self.listaPuertos.addItem("")
        self.listaPuertos.setItemText(6, "COM7")
        self.listaPuertos.addItem("")
        self.listaPuertos.setItemText(7, "COM8")
        self.listaPuertos.addItem("")
        self.listaPuertos.setItemText(8, "COM9")
        self.listaPuertos.addItem("")
        self.listaPuertos.setItemText(9, "COM10")
        self.listaPuertos.addItem("")
        self.listaPuertos.setItemText(10, "COM11")
        self.listaPuertos.addItem("")
        self.listaPuertos.setItemText(11, "COM12")
        self.titulo03 = QtWidgets.QLabel(SisDomArduino)
        self.titulo03.setGeometry(QtCore.QRect(270, 60, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.titulo03.setFont(font)
        self.titulo03.setToolTip("")
        self.titulo03.setWhatsThis("")
        self.titulo03.setAccessibleName("")
        self.titulo03.setAccessibleDescription("")
        self.titulo03.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.titulo03.setText("Control de Cargas")
        self.titulo03.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo03.setObjectName("titulo03")
        self.bDesconect = QtWidgets.QPushButton(SisDomArduino)
        self.bDesconect.setEnabled(False)
        self.bDesconect.setGeometry(QtCore.QRect(30, 150, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bDesconect.setFont(font)
        self.bDesconect.setToolTip("Desconectar")
        self.bDesconect.setStatusTip("")
        self.bDesconect.setWhatsThis("")
        self.bDesconect.setAccessibleName("")
        self.bDesconect.setAccessibleDescription("")
        self.bDesconect.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.bDesconect.setText("Desconectar")
        self.bDesconect.setObjectName("bDesconect")
        self.titulo04 = QtWidgets.QLabel(SisDomArduino)
        self.titulo04.setEnabled(True)
        self.titulo04.setGeometry(QtCore.QRect(40, 270, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.titulo04.setFont(font)
        self.titulo04.setToolTip("")
        self.titulo04.setWhatsThis("")
        self.titulo04.setAccessibleName("")
        self.titulo04.setAccessibleDescription("")
        self.titulo04.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.titulo04.setText("Sistema Inteligente")
        self.titulo04.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo04.setObjectName("titulo04")

        self.txt1 = QtWidgets.QLabel(SisDomArduino)
        self.txt1.setEnabled(True)
        self.txt1.setGeometry(QtCore.QRect(170, 310, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.txt1.setFont(font)
        self.txt1.setToolTip("")
        self.txt1.setWhatsThis("")
        self.txt1.setAccessibleName("")
        self.txt1.setAccessibleDescription("")
        self.txt1.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.txt1.setText("Estado: No iniciado.")
        self.txt1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt1.setObjectName("txt1")
        
        self.bLed2 = QtWidgets.QPushButton(SisDomArduino)
        self.bLed2.setGeometry(QtCore.QRect(310, 140, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bLed2.setFont(font)
        self.bLed2.setToolTip("Controla Led 02")
        self.bLed2.setStatusTip("")
        self.bLed2.setWhatsThis("")
        self.bLed2.setAccessibleName("")
        self.bLed2.setAccessibleDescription("")
        self.bLed2.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.bLed2.setText("Led 02 On/Off")
        self.bLed2.setObjectName("bLed2")
        self.bLed3 = QtWidgets.QPushButton(SisDomArduino)
        self.bLed3.setGeometry(QtCore.QRect(310, 180, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bLed3.setFont(font)
        self.bLed3.setToolTip("Controla Led 03")
        self.bLed3.setStatusTip("")
        self.bLed3.setWhatsThis("")
        self.bLed3.setAccessibleName("")
        self.bLed3.setAccessibleDescription("")
        self.bLed3.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.bLed3.setText("Led 03 On/Off")
        self.bLed3.setObjectName("bLed3")
        self.bLed4 = QtWidgets.QPushButton(SisDomArduino)
        self.bLed4.setGeometry(QtCore.QRect(310, 220, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bLed4.setFont(font)
        self.bLed4.setToolTip("Controla Led 04")
        self.bLed4.setStatusTip("")
        self.bLed4.setWhatsThis("")
        self.bLed4.setAccessibleName("")
        self.bLed4.setAccessibleDescription("")
        self.bLed4.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.bLed4.setText("Led 04 On/Off")
        self.bLed4.setObjectName("bLed4")
        self.img01 = QtWidgets.QLabel(SisDomArduino)
        self.img01.setGeometry(QtCore.QRect(50, 200, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.img01.setFont(font)
        self.img01.setToolTip("")
        self.img01.setWhatsThis("")
        self.img01.setAccessibleName("")
        self.img01.setAccessibleDescription("")
        self.img01.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.img01.setText("<html><head/><body><p><img src=\"./Recursos/ConectorSerial_64x64.png\"/></p></body></html>")
        self.img01.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.img01.setObjectName("img01")
        self.img02 = QtWidgets.QLabel(SisDomArduino)
        self.img02.setGeometry(QtCore.QRect(180, 170, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.img02.setFont(font)
        self.img02.setToolTip("")
        self.img02.setWhatsThis("")
        self.img02.setAccessibleName("")
        self.img02.setAccessibleDescription("")
        self.img02.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.img02.setText("<html><head/><body><p><img src=\"./Recursos/ImagenDeLed__64x64.png\"/></p></body></html>")
        self.img02.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.img02.setObjectName("img02")
        self.img03 = QtWidgets.QLabel(SisDomArduino)
        self.img03.setEnabled(True)
        self.img03.setGeometry(QtCore.QRect(330, 280, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.img03.setFont(font)
        self.img03.setToolTip("")
        self.img03.setWhatsThis("")
        self.img03.setAccessibleName("")
        self.img03.setAccessibleDescription("")
        self.img03.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.img03.setText("<html><head/><body><p><img src=\"./Recursos/Microfono_64x64.png\"/></p></body></html>")
        self.img03.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.img03.setObjectName("img03")

        self.retranslateUi(SisDomArduino)
        self.bSalir.clicked.connect(SisDomArduino.close)
        QtCore.QMetaObject.connectSlotsByName(SisDomArduino)
        SisDomArduino.setTabOrder(self.bConect, self.bDesconect)
        SisDomArduino.setTabOrder(self.bDesconect, self.listaPuertos)
        SisDomArduino.setTabOrder(self.listaPuertos, self.bEscuchar)
        SisDomArduino.setTabOrder(self.bEscuchar, self.bLed1)
        SisDomArduino.setTabOrder(self.bLed1, self.bLed2)
        SisDomArduino.setTabOrder(self.bLed2, self.bLed3)
        SisDomArduino.setTabOrder(self.bLed3, self.bLed4)
        SisDomArduino.setTabOrder(self.bLed4, self.bSalir)

    def retranslateUi(self, SisDomArduino):
        _translate = QtCore.QCoreApplication.translate
        self.bSalir.setShortcut(_translate("SisDomArduino", "Ctrl+W"))