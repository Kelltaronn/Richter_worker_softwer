from PyQt6.QtWidgets import QMessageBox

def warning_error_message(self,message,information):
    warning_message_box = QMessageBox()
    warning_message_box.setIcon(QMessageBox.Icon.Warning)
    warning_message_box.setWindowTitle("Warning")
    warning_message_box.setText(message)
    warning_message_box.setInformativeText(information)
    warning_message_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)