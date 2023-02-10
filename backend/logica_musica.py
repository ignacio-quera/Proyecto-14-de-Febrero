from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtMultimedia

class Musica(QObject):

    def __init__(self, ruta_cancion):
        super().__init__()
        self.ruta_cancion = ruta_cancion
        self.cancion = ''

    def comenzar(self):
        try:
            self.cancion = QtMultimedia.QSound(self.ruta_cancion)
            self.cancion.Loop()
            self.cancion.play()
        except Exception as error:
            print('No se pudo iniciar la cancion', error)
    
    def parar(self):
        if self.cancion:
            self.cancion.stop()