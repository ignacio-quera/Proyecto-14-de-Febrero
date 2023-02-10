import sys
from frontend.ventana_pregunta_inicial import VentanaPreguntaInicial
from frontend.ventana_confirmacion import VentanaConfirmacion
from frontend.ventana_felicidad import VentanaFelicidad
from frontend.ventana_sad_1 import VentanaSad1
from frontend.ventana_sad_2 import VentanaSad2

from backend.logica_musica import Musica

from PyQt5.QtWidgets import QApplication
from pathlib import Path

import os

def hook(type_error, traceback):
    print(type_error)
    print(traceback)


if __name__ == '__main__':

    # Inicialización de la aplicación

    sys.__excepthook__ = hook
    app = QApplication(sys.argv)
    # app.setStyleSheet(Path('login.qss').read_text())

    ventana_pregunta_inicial = VentanaPreguntaInicial()
    ventana_confirmacion = VentanaConfirmacion()
    ventana_felicidad = VentanaFelicidad()
    ventana_sad_1 = VentanaSad1()
    ventana_sad_2 = VentanaSad2()

    path_musica = os.path.join("frontend", "assets", "can-we-get-much-higher.wav")
    cancion_higher = Musica(path_musica)

    ventana_pregunta_inicial.senal_si.connect(ventana_confirmacion.abrir_ventana)
    ventana_pregunta_inicial.senal_no.connect(ventana_sad_1.abrir_ventana)

    ventana_confirmacion.senal_no.connect(ventana_pregunta_inicial.abrir_ventana)
    ventana_confirmacion.senal_si.connect(ventana_felicidad.abrir_ventana)
    
    ventana_felicidad.senal_musica.connect(cancion_higher.comenzar)

    ventana_sad_1.senal_no.connect(ventana_sad_2.abrir_ventana)
    ventana_sad_1.senal_si.connect(ventana_confirmacion.abrir_ventana)

    ventana_pregunta_inicial.abrir_ventana()
    
    sys.exit(app.exec())