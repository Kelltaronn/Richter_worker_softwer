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

def standardized_input_field_generator(self,name_of_the_generator,standardized_label_width,standardized_input_width):
    layout = QHBoxLayout()

    label = QLabel(name_of_the_generator)
    label.setFixedWidth(standardized_label_width)

    name_input = QLineEdit()
    name_input.setFixedWidth(standardized_input_width)
    layout.addWidget(label,alignment=Qt.AlignmentFlag.AlignRight)
    layout.addWidget(name_input,alignment=Qt.AlignmentFlag.AlignLeft)
    print("Létrehoztam a Labelt = {} és az input fieldet".format(name_of_the_generator))
    return layout ,name_input

