import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QMessageBox,
    QHBoxLayout, QCheckBox, QPushButton, QLabel, QButtonGroup, QFrame
)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QColor, QPalette, QPixmap, QFont, QFontDatabase
path = os.path.join("frontend", "assets", "ventana_sad_1.ui")
window_name, base_class = uic.loadUiType(path)

class VentanaSad1(window_name, base_class):

    senal_si = pyqtSignal()
    senal_no = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())

        self.label.setFont(QFont("Vivaldi", 20))
        self.pushButton.clicked.connect(self.acceptance)
        self.pushButton_2.clicked.connect(self.rejection)

        self.font_size = 30
        self.contador = 0


    def abrir_ventana(self):
        # self.senal_empezar_musica.emit()
        self.show()

    def acceptance(self):
        self.senal_si.emit()
        self.close()
        pass

    def rejection(self):
        self.contador += 1
        self.font_size+=10
        self.label.setStyleSheet(f"font-size: {self.font_size}px")
        if self.contador == 10:
            self.pushButton.setText("No")
            self.pushButton_2.setText("Si")
            self.pushButton_2.clicked.disconnect()
            self.pushButton.clicked.disconnect()
            self.pushButton_2.clicked.connect(self.acceptance)
            self.pushButton.clicked.connect(self.rejection)
            self.contador+=1
        elif self.contador > 10:
            self.senal_no.emit()
            self.close()        