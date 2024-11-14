#Imports:
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget,
                             QHBoxLayout,
                             QLabel,
                             QLineEdit
                             
                             )
"""
Ez a fájl az általánosított Input fieldekhez lett írva:
"""

label_width_setting = 400 # Ez változtatja a jobb oldali szöveg mező méretét
input_fixed_width = 400 #Ez Változtatja  az input field mérettét.
def standardized_input_field(label_text):
    layout = QHBoxLayout
    label = QLabel(label_text)
    label.setFixedWidth(label_width_setting)
    label.setAlignment(Qt.AlignmentFlag.AlignRight)
    input_field = QLineEdit()
    input_field.setFixedWidth(input_fixed_width)
    return input_field
