'''
Filename: createWindow.py
Created Date: Tuesday, May 13th 2025, 11:11:53 am
Author: Pepe Alkalina
'''

from scrcpy import *
import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout ,QMessageBox, QMainWindow
from PySide6.QtGui import QPixmap, QImage

if not QApplication.instance():
    app = QApplication([])
else:
    app = QApplication.instance()

class ImageWindow(QMainWindow):
    app.processEvents()
    def __init__(self, frame, serial: str):
        super().__init__()
        self.setWindowTitle("Serial: " + serial)

    def showWindow(self):
        # Crear un layout vertical
        layout = QVBoxLayout()

        # Crear un QLabel y cargar la imagen
        image_label = QLabel()
        image = QImage(
            frame,
            frame.shape[1],
            frame.shape[0],
            frame.shape[1] * 3,
            QImage.Format_BGR888,
        )
        pixMap = QPixmap(image)  # Cambia esto a la ruta de tu imagen
        image_label.setPixmap( pixMap )
        image_label.show()
        
            
        



