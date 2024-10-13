#Import's:
from PyQt6.QtWidgets import (QWidget, 
                             QPushButton, 
                             QVBoxLayout,
                             QMainWindow,
                             QStackedWidget,
                             QHBoxLayout,
                             QLineEdit,
                             QLabel
                             )

"""
This is the main page of the software.
You can choose between the button's
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle("Main Window with Navigation")
        self.setGeometry(200, 200, 400, 300)

        # Create the QStackedWidget for holding different pages
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Create pages
        self.create_main_page()
        self.create_page1()
        self.create_page2()
        self.create_page3()
        self.create_page4()

        # Add pages to the QStackedWidget
        self.stacked_widget.addWidget(self.main_page)  # Index 0
        self.stacked_widget.addWidget(self.page1)      # Index 1
        self.stacked_widget.addWidget(self.page2)      # Index 2
        self.stacked_widget.addWidget(self.page3)      # Index 3
        self.stacked_widget.addWidget(self.page4)      # Index 4

        # Show the main page initially
        self.stacked_widget.setCurrentIndex(0)

    def create_main_page(self):
        # Ez itt a főoldal a kétgombbal.
        self.main_page = QWidget()
        layout = QVBoxLayout()

        # Gombok a kezdő lapon.
        page1_button = QPushButton("Hozzáadás")
        page2_button = QPushButton("Keresés")

        # Connect buttons to functions to navigate to respective pages
        page1_button.clicked.connect(self.show_page1)
        page2_button.clicked.connect(self.show_page2)

        layout.addWidget(page1_button)
        layout.addWidget(page2_button)

        self.main_page.setLayout(layout)
    def create_page1(self):
        # Create Page 1 with a form (Name, Age, Profession), Grab Data, and Back button
        self.page1 = QWidget()
        layout = QVBoxLayout()

        # Itt csinálom meg az egymás alatt lévő input dobozokat.
        form_layout = QVBoxLayout()

        #Input doboz a névhez:
        name_layout = QHBoxLayout()
        name_label = QLabel("Name:")
        self.name_input = QLineEdit()

        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)

        #Input doboz a korhoz.
        age_layout = QHBoxLayout()
        age_label = QLabel("Age:")
        self.age_input = QLineEdit()

        age_layout.addWidget(age_label)
        age_layout.addWidget(self.age_input)

        #Input doboz a foglalkozáshoz.
        profession_layout = QHBoxLayout()
        profession_label = QLabel("Profession:")
        self.profession_input = QLineEdit()

        profession_layout.addWidget(profession_label)
        profession_layout.addWidget(self.profession_input)

        # Add all input rows (Name, Age, Profession) to the form layout
        form_layout.addLayout(name_layout)
        form_layout.addLayout(age_layout)
        form_layout.addLayout(profession_layout)

        # Add the form layout to the main layout
        layout.addLayout(form_layout)

        # Add "Grab Data" button
        grab_data_button = QPushButton("Grab Data")
        grab_data_button.clicked.connect(self.grab_data) #Ha ezt itt lenyomom itt az adat
        layout.addWidget(grab_data_button)

        # Back button to return to the main page
        back_button = QPushButton("Back to Main Page")
        back_button.clicked.connect(self.show_main_page)
        layout.addWidget(back_button)

        # Set layout for Page 1
        self.page1.setLayout(layout)

    def create_page2(self):
        # Create Page 2 with buttons for Page 3 and Page 4, and a Back button
        self.page2 = QWidget()
        layout = QVBoxLayout()

        page3_button = QPushButton("Go to Page 3")
        page4_button = QPushButton("Go to Page 4")
        back_button = QPushButton("Back to Main Page")

        # Connect buttons to navigate to respective pages
        page3_button.clicked.connect(self.show_page3)
        page4_button.clicked.connect(self.show_page4)
        back_button.clicked.connect(self.show_main_page)

        layout.addWidget(page3_button)
        layout.addWidget(page4_button)
        layout.addWidget(back_button)

        self.page2.setLayout(layout)

    def create_page3(self):
        # Create Page 3 with a Back button to Page 2
        self.page3 = QWidget()
        layout = QVBoxLayout()

        label = QPushButton("This is Page 3")
        back_button = QPushButton("Back to Page 2")

        # Connect the Back button to navigate back to Page 2
        back_button.clicked.connect(self.show_page2)

        layout.addWidget(label)
        layout.addWidget(back_button)

        self.page3.setLayout(layout)

    def create_page4(self):
        # Create Page 4 with a Back button to Page 2
        self.page4 = QWidget()
        layout = QHBoxLayout()

        label = QPushButton("This is Page 4")
        back_button = QPushButton("Back to Page 2")

        # Connect the Back button to navigate back to Page 2
        back_button.clicked.connect(self.show_page2)

        layout.addWidget(label)
        layout.addWidget(back_button)

        self.page4.setLayout(layout)

    # Navigation functions
    def show_main_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_page1(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_page2(self):
        self.stacked_widget.setCurrentIndex(2)

    def show_page3(self):
        self.stacked_widget.setCurrentIndex(3)

    def show_page4(self):
        self.stacked_widget.setCurrentIndex(4)

    """
    Ez itt feldolgozza az adatot és eljuttatja a process datához.
    """
    def grab_data(self):
        # Retrieve data from input fields
        name = self.name_input.text()
        age = self.age_input.text()
        profession = self.profession_input.text()
        self.process_data(name, age, profession)
    
    def process_data(self, name, age, profession):
        # Example: You could save the data, print it, or perform any operations you need
        print(f"Processing Data:\nName: {name}\nAge: {age}\nProfession: {profession}")