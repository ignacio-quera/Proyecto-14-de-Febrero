import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QMessageBox, 
    QHBoxLayout, QCheckBox, QPushButton, QLabel, QButtonGroup, QFrame
)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QColor, QPalette, QPixmap, QFont, QFontDatabase, QMovie
path = os.path.join("frontend", "assets", "ventana_felicidad.ui")
window_name, base_class = uic.loadUiType(path)

class VentanaFelicidad(window_name, base_class):

    senal_musica = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())


        self.movie = QMovie(os.path.join("frontend", "assets", "can-we-get-much-higher.gif"))
        self.label.setMovie(self.movie)


    def abrir_ventana(self):
        # self.senal_empezar_musica.emit()
        self.show()
        self.senal_musica.emit()
        self.movie.start()


    def acceptance(self):
        pass

    def rejection(self):
        self.senal_no.emit()
        self.close()
        pass