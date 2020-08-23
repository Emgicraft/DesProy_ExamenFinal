# -*- coding: utf-8 -*-
"""
Ejercicio 06 - Aplicación Libre - Reproductor Multimedia

@author: Magh
"""

import PyQt5.QtCore as qc
import PyQt5.QtMultimedia as qmulti
import PyQt5.QtMultimediaWidgets as qmultiWid
import PyQt5.QtWidgets as qw
from PyQt5 import QtGui


class VideoPlayer(qw.QWidget):
    def __init__(self, ancho, alto, parent=None):
        super(VideoPlayer, self).__init__(parent)

        self.setWindowTitle('Reproductor de Video')
        self.resize(ancho, alto)
        self.setWindowIcon(QtGui.QIcon('Recursos/MCServer-icon-64x64.png'))

        openButton = qw.QPushButton("Buscar...")
        openButton.clicked.connect(self.openFile)

        self.playButton = qw.QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(qw.QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = qw.QSlider(qc.Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        controlLayout = qw.QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(openButton)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        videoWidget = qmultiWid.QVideoWidget()

        layout = qw.QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)

        self.setLayout(layout)

        self.mediaPlayer = qmulti.QMediaPlayer(None, qmulti.QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

    def openFile(self):
        fileName, _ = qw.QFileDialog.getOpenFileName(self, "Elegir archivo de video", qc.QDir.homePath())

        if fileName != '':
            self.mediaPlayer.setMedia(qmulti.QMediaContent(qc.QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def play(self):
        if self.mediaPlayer.state() == qmulti.QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == qmulti.QMediaPlayer.PlayingState:
            self.playButton.setIcon(self.style().standardIcon(qw.QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(self.style().standardIcon(qw.QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)


def main():
    from sys import argv, exit

    app=qw.QApplication(argv)
    videoPlayer=VideoPlayer(800, 600)
    videoPlayer.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()