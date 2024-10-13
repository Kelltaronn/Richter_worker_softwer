#Imported system
import sys

#Import required window and all other:
import PyQt6
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow

#Model import's:
from software_stater_pg import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())
