from PyQt6.QtGui import *
from PyQt6.QtQuickWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QMainWindow, QApplication,QLabel


import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Window")

        label = QLabel("This goes here")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
