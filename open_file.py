from error_handling_messages import warning_error_message
from File_searching_module import open_file_system
import pandas as pd

def open_file(filename):
    try:
        database_file = open(filename,"r",errors='strict')
    except FileNotFoundError:
        message = " Hiányzó fájl"
        information = "A program hibába ütközött nem találja a szükséges adat bázist."
        warning_error_message(message,information)


        selected_file = open_file_system()
    return database_file


