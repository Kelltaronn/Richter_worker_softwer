from PyQt6.QtWidgets import QFileDialog

def open_file_system(self):
    file_dialog = QFileDialog()
    file_path = file_dialog.getOpenFileName(self,"Fájl Keresése","",filter="*.txt")

    if file_path:
        print(f"Selected file: {file_path}")  # Do something with the selected file path
        return file_path