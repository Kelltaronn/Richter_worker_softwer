"""
A szükséges könyvtár betöltések és egyéb futás előtti  műveletek helyei
"""
import pandas as pd
from File_searching_module import open_file_system
from open_file import open_file
from openpyxl import load_workbook
#Import's:
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, 
                             QPushButton, 
                             QVBoxLayout,
                             QMainWindow,
                             QStackedWidget,
                             QHBoxLayout,
                             QLineEdit,
                             QLabel,
                             QListWidget,
                             QMessageBox,
                             QCheckBox,
                             QRadioButton,
                             QButtonGroup,
                             QFileDialog,
                             QApplication,
                             QSpacerItem,
                             QSizePolicy
                             )
#Other Modules:
from Standardized_input_field import standardized_input_field_generator



"""
Ez A szoftver GUI-ja itt változtathatóak az oldalak számai funkciói a rajtuk lévő elemek mennyisége és minősége.

A MainWindow class foglalja magába mind ezt.
"""
class User():
    def __init__(self,
                 system_serial_name,
                 system_owner,
                 user_name,
                 work_task,
                 user_number,
                 login_name,
                 organization_unit,
                 phone_number,
                 date_of_education,
                 education_serial_number,
                 server_administrator,
                 ):
        self.system_serial_name = system_serial_name
        self.system_owner = system_owner
        self.user_name = user_name
        self.work_task = work_task
        self.user_number = user_number
        self.login_name = login_name
        self.organization_unit = organization_unit
        self.phone_number = phone_number
        self.date_of_education = date_of_education
        self.education_serial_number = education_serial_number
        self.server_administrator = server_administrator

    def __repr__(self):
        return (f"User("
                f"system_serial_name={self.system_serial_name!r}, "
                f"system_owner={self.system_owner!r}, "
                f"user_name={self.user_name!r}, "
                f"work_task={self.work_task!r}, "
                f"user_number={self.user_number!r}, "
                f"login_name={self.login_name!r}, "
                f"organization_unit={self.organization_unit!r}, "
                f"phone_number={self.phone_number!r}, "
                f"date_of_education={self.date_of_education!r}, "
                f"education_serial_number={self.education_serial_number!r}, "
                f"server_administrator={self.server_administrator!r})")

def make_user(
        system_serial_name,
        system_owner,
        user_name,
        work_task,
        user_number,
        login_name,
        organization_unit,
        phone_number,
        date_of_education,
        education_serial_number,
        server_administrator,
                ):
    user = User(
        system_serial_name,
        system_owner,
        user_name,
        work_task,
        user_number,
        login_name,
        organization_unit,
        phone_number,
        date_of_education,
        education_serial_number,
        server_administrator,
                )
    return user


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        """
        try:
            database_file = open("local.txt","r",errors='strict')
        except FileNotFoundError:
            message = " Hiányzó fájl"
            information = "A program hibába ütközött nem találja a szükséges adat bázist."
            warning_error_message(self,message,information)


            selected_file = open_file_system(self)
            if not database_file:
                QApplication.quit()
            try:
                database_file = open(selected_file,"r",errors='strict')
            except Exception as e:
                warning_error_message(self, "Hiba a fájl megnyitásakor", f"A fájlt nem sikerült megnyitni: {str(e)}")
                QApplication.quit()
                """
                

        # Alap funkciók és méretek a software-hez.
        
        self.setWindowTitle("Main Window with Navigation")
        self.setGeometry(200, 200, 1000, 800)

        """
         Ez a rész határozza meg hogy az egymáson lévő oldalak-ból mennyi legyen illetve hogy az oldalak
         hozzá vannak-e adva vagy sem a GUI-hoz.
        """
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Itt lehet létrehozni az egyes lapokat:
        self.create_main_page()
        self.create_page1()
        self.create_page2()
        self.create_page3()
        self.create_page4()
        self.create_page5()

        # Itt lehet hozzá adni az egyes lapokat a stacked widget-hez
        #FONTOS HA KIVESZEL LAPOT KIVESZED AZ INDEXET NEM TUDOM MIÉRT DE ELCSÚSZIK EZÁLTAL TEHÁT HA 5 OLDALAD VAN
        # HOZZÁ ADVA DE KIKAPCSOLSZ 2-ÖT NEM JELENITI MEG.
        # NE KÉRDEZD MIÉRT.
        self.stacked_widget.addWidget(self.main_page)  # Index 0
        self.stacked_widget.addWidget(self.page1)      # Index 1
        self.stacked_widget.addWidget(self.page2)      # Index 2
        self.stacked_widget.addWidget(self.page3)      # Index 3
        self.stacked_widget.addWidget(self.page4)      # Index 4
        self.stacked_widget.addWidget(self.page5)      # Index 5

        # A szoftver nyitásnál egyből a kezdőlapra lépjen ez az indextől fog függni lásd feljebb:
        self.stacked_widget.setCurrentIndex(0)

    """
    Ez a kód részlet meghatározza hogy az egyes oldalak mint önálló funkciók hogy viselkedjenek és mi legyen a tartalmuk.
    """

    """
    Ez itt a főoldal:
    """
    def create_main_page(self):
        # Ez itt a főoldal.
        """
        EZ ITT S FILE VALIDÁTOR EZT ITT ELLENŐRZI A PROGRAM MEGNYITÁSAKOR A FILE JELENLÉTÉT.
        
        try:
            database_file = open("local.txt","r",errors='strict')
        except FileNotFoundError:
            database_file = open_file_system(self)
            if database_file == None:
                print(database_file)
                database_file.close()
                self.close()
            else:
                pass
        """
        self.main_page = QWidget()
        layout = QVBoxLayout()

        # Gombok a kezdő lapon.
        page1_button = QPushButton("Hozzáadás")
        page2_button = QPushButton("Keresés")
        find_table_button = QPushButton("Tallóz")

        # Ezek kötik össze a gombokat a funkciókkal ha hibába futsz nézd meg lejjebb hogy a funkció jó-e vagy van.
        page1_button.clicked.connect(self.show_page1)
        page2_button.clicked.connect(self.show_page2)
        find_table_button.clicked.connect(lambda: open_file_system(self))

        layout.addWidget(page1_button)
        layout.addWidget(page2_button)
        layout.addWidget(find_table_button)

        self.main_page.setLayout(layout)


    """
    Ez itt a hozzáadási oldal:
    """
    def create_page1(self):
        # Ezzel lehet állítani a  szélességét az input mezőnek.
        standardized_label_width = 400
        standardized_input_width = 400

        self.page1 = QWidget()
        layout = QVBoxLayout()

        # Itt csinálom meg az egymás alatt lévő input dobozokat.
        form_layout = QVBoxLayout()
        #Input 1:
        system_serial_name_layout, self.system_serial_name_input =  standardized_input_field_generator(self,"Rendszer Azonosítója és Megnvezése:",standardized_label_width,standardized_input_width)
        #Input 2:.
        system_owner_layout,self.system_owner_input = standardized_input_field_generator(self,"Rendszer Tulajdonos:",standardized_label_width,standardized_input_width)
        #Input 3:
        user_name_layout,self.user_name_input = standardized_input_field_generator(self,"Felhasználó Neve:",standardized_label_width,standardized_input_width)
        #Input 4:
        work_task_layout,self.work_task_input = standardized_input_field_generator(self,"Felhasznaló Feladatköre a rendszerben",standardized_label_width,standardized_input_width)
        #Input 5:
        user_number_layout,self.user_number_input = standardized_input_field_generator(self,"Törzs száma:",standardized_label_width,standardized_input_width)
        #Input 6:
        login_name_layout,self.login_name_input = standardized_input_field_generator(self,"Login Név:",standardized_label_width,standardized_input_width)
        #Input 7:
        organisation_unit_layout,self.organisation_unit_input = standardized_input_field_generator(self,"Szervezeti egység:",standardized_label_width,standardized_input_width)
        #Input 8:
        phone_number_layout,self.phone_number_input = standardized_input_field_generator(self,"Telefonszám:",standardized_label_width,standardized_input_width)
        #Input 9:
        date_of_education_layout,self.date_of_education_input = standardized_input_field_generator(self,"Oktatás Dátuma:",standardized_label_width,standardized_input_width)
        #Input 10:
        education_serial_number_layout,self.education_serial_number_input = standardized_input_field_generator(self,"Oktatási Azonosító:",standardized_label_width,standardized_input_width)
        #Input 11:
        server_administrator_layout,self.server_administrator_input = standardized_input_field_generator(self,"Rendszer Adminisztrátor:",standardized_label_width,standardized_input_width)
        """
        #Checkbox items:
        """
        #Checkbox 1:
        checkbox_user_layout = QHBoxLayout()

        new_user_label = QRadioButton("Új Felhasználó:")
        change_user_label = QRadioButton("Módosítás:")
        cancel_user_label = QRadioButton("Visszavonás:")

        checkbox_user_layout.setContentsMargins(0,0,0,0)
        checkbox_user_layout.setSpacing(10)

        checkbox_user_layout.addWidget(new_user_label,alignment=Qt.AlignmentFlag.AlignCenter)
        checkbox_user_layout.addWidget(change_user_label,alignment=Qt.AlignmentFlag.AlignCenter)
        checkbox_user_layout.addWidget(cancel_user_label,alignment=Qt.AlignmentFlag.AlignCenter)

        self.user_action_group = QButtonGroup()
        self.user_action_group.addButton(new_user_label, id=1)
        self.user_action_group.addButton(change_user_label, id=2)
        self.user_action_group.addButton(cancel_user_label, id=3)


        """
        #Az előző text inputokat hozzáadás a  layouthoz:
        """
        # Az Indexelt text inputok hozzáadása az formhoz:
        form_layout.addLayout(system_serial_name_layout)
        form_layout.addLayout(system_owner_layout)
        form_layout.addLayout(user_name_layout)
        form_layout.addLayout(work_task_layout)
        form_layout.addLayout(user_number_layout)
        form_layout.addLayout(login_name_layout)
        form_layout.addLayout(organisation_unit_layout)
        form_layout.addLayout(phone_number_layout)
        form_layout.addLayout(date_of_education_layout)
        form_layout.addLayout(education_serial_number_layout)
        form_layout.addLayout(server_administrator_layout)

        # A checkbox hozzáadás:
        form_layout.addLayout(checkbox_user_layout)

        

        # Form hozzá adása a layouthoz.
        layout.addLayout(form_layout)
        # Form méretek megadása:
        layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))


        

        # Ez itt az adatbevétel gombja
        grab_data_button = QPushButton("Adatbevitel")
        grab_data_button.clicked.connect(lambda: self.process_data(self.grab_data()))
        layout.addWidget(grab_data_button)

        # Vissza gomb:
        back_button = QPushButton("Vissza a Kezdőlapra")
        back_button.clicked.connect(self.show_main_page)
        layout.addWidget(back_button)

        # Létre hozom a layout-ot az egyes oldalhoz.
        self.page1.setLayout(layout)


    """
    Ez választható kereső oldalas GUI az oldalon elhelyzkednek a beirható kereső sorok, az egyes sorok ki-be lesznek
    kapcsolhatóak attól függően mire miért keresünk rá.
    """
    def create_page2(self):
        # A kereső oldal fő layout-ja
        self.page2 = QWidget()
        layout = QVBoxLayout()

        # Ez a kikapcsolható  Törzsszám alapú kereső mező:
        self.user_number_checkbox = QCheckBox("Keresés Törzsszám alapján:")
        self.user_number_input = QLineEdit()
        self.user_number_input.setEnabled(False)  # Ezek a sorok meglesznek ismételve alapból kilesz kapcsolva az összes.

        # Ez a kikapcsolható  Név alapú kereső mező:
        self.user_name_checkbox = QCheckBox("Keresés Név alapján")
        self.user_name_input = QLineEdit()
        self.user_name_input.setEnabled(False)  # Ezek a sorok meglesznek ismételve alapból kilesz kapcsolva az összes.

        # Ez a kikapcsolható  Gépüzemrészére alapú kereső mező:
        self.organization_unit_checkbox = QCheckBox("Keresés beosztás alapján:")
        self.organisation_unit_input = QLineEdit()
        self.organisation_unit_input.setEnabled(False)  # Ezek a sorok meglesznek ismételve alapból kilesz kapcsolva az összes.
        
        self.system_serial_name_checkbox = QCheckBox("Keresés SYSID alapján:")
        self.system_serial_name_input = QLineEdit()
        self.system_serial_name_input.setEnabled(False) # Ezek a sorok meglesznek ismételve alapból kilesz kapcsolva az összes.

        self.system_name_checkbox= QCheckBox("Keresés Rendszer megnevezés alapján:")
        self.system_name_input = QLineEdit()
        self.system_name_input.setEnabled(False) # Ezek a sorok meglesznek ismételve alapból kilesz kapcsolva az összes.

        self.login_name_checkbox = QCheckBox("Keresés Login Felhasználó kör alapján:")
        self.login_name_input= QLineEdit()
        self.login_name_input.setEnabled(False) # Ezek a sorok meglesznek ismételve alapból kilesz kapcsolva az összes.

        self.work_task_checkbox = QCheckBox("Keresés Feladatkör alapján:")
        self.work_task_input = QLineEdit()
        self.work_task_input.setEnabled(False) # Ezek a sorok meglesznek ismételve alapból kilesz kapcsolva az összes.

        self.education_serial_number_checkbox = QCheckBox("Keresés Igénylőlap azonosító (kiadás) alapján:")
        self.education_serial_number_input = QLineEdit()
        self.education_serial_number_input.setEnabled(False) # Ezek a sorok meglesznek ismételve alapból kilesz kapcsolva az összes.

        self.education_serial_number_cancel_checkbox = QCheckBox("Keresés Igénylőlap azonosító (Visszavonás) alapján:")
        self.education_serial_number_cancel_input = QLineEdit()
        self.education_serial_number_cancel_input.setEnabled(False) # Ezek a sorok meglesznek ismételve alapból kilesz kapcsolva az összes.

        self.job_status_checkbox = QCheckBox("Keresés Státusz alapján:")
        self.job_status_input = QLineEdit()
        self.job_status_input.setEnabled(False)

        self.clearance_level_checkbox = QCheckBox("Keresés Gépfelhasználói szint alapján:")
        self.clearance_level_input = QLineEdit()
        self.clearance_level_input.setEnabled(False)

        # Itt kel bekotni a  ki-be kapcsoló gombokat a mezőkhöz.
        self.user_number_checkbox.stateChanged.connect(lambda: self.user_number_input.setEnabled(self.user_number_checkbox.isChecked()))
        self.user_name_checkbox.stateChanged.connect(lambda: self.user_name_input.setEnabled(self.user_name_checkbox.isChecked()))
        self.organization_unit_checkbox.stateChanged.connect(lambda: self.organisation_unit_input.setEnabled(self.organization_unit_checkbox.isChecked()))
        self.system_serial_name_checkbox.stateChanged.connect(lambda: self.system_serial_name_input.setEnabled(self.system_serial_name_checkbox.isChecked()))
        self.system_name_checkbox.stateChanged.connect(lambda: self.system_name_input.setEnabled(self.system_name_checkbox.isChecked()))
        self.login_name_checkbox.stateChanged.connect(lambda: self.login_name_input.setEnabled(self.login_name_checkbox.isChecked()))
        self.work_task_checkbox.stateChanged.connect(lambda: self.work_task_input.setEnabled(self.work_task_checkbox.isChecked()))
        self.education_serial_number_checkbox.stateChanged.connect(lambda: self.education_serial_number_input.setEnabled(self.education_serial_number_checkbox.isChecked()))
        self.education_serial_number_cancel_checkbox.stateChanged.connect(lambda: self.education_serial_number_cancel_input.setEnabled(self.education_serial_number_cancel_checkbox.isChecked()))
        self.job_status_checkbox.stateChanged.connect(lambda: self.job_status_input.setEnabled(self.job_status_checkbox.isChecked()))
        self.clearance_level_checkbox.stateChanged.connect(lambda: self.clearance_level_input.setEnabled(self.clearance_level_checkbox.isChecked()))


        # Ez betölti  az egyes már előzőleg meghatárott gombokat mezőket. Ez a kereseő motor bevitelének a GUI-ja
        #FONTOS A SORREND SZÁMÍT!!!!!!!!!!!!!!!!
        layout.addWidget(self.user_number_checkbox)
        layout.addWidget(self.user_number_input)

        layout.addWidget(self.user_name_checkbox)
        layout.addWidget(self.user_name_input)

        layout.addWidget(self.organization_unit_checkbox)
        layout.addWidget(self.organisation_unit_input)

        layout.addWidget(self.system_serial_name_checkbox)
        layout.addWidget(self.system_serial_name_input)

        layout.addWidget(self.system_name_checkbox)
        layout.addWidget(self.system_name_input)

        layout.addWidget(self.login_name_checkbox)
        layout.addWidget(self.login_name_input)

        layout.addWidget(self.work_task_checkbox)
        layout.addWidget(self.work_task_input)

        layout.addWidget(self.education_serial_number_checkbox)
        layout.addWidget(self.education_serial_number_input) 

        layout.addWidget(self.education_serial_number_cancel_checkbox)
        layout.addWidget(self.education_serial_number_cancel_input)

        layout.addWidget(self.job_status_checkbox)
        layout.addWidget(self.job_status_input)

        layout.addWidget(self.clearance_level_checkbox)
        layout.addWidget(self.clearance_level_input)         
        # A kereső gomb:
        search_button = QPushButton("Keresés a beírt adatok alapján")
        search_button.clicked.connect(self.perform_search)

        # A Vissza gomb:
        back_button = QPushButton("Vissza")
        back_button.clicked.connect(self.show_main_page)

        layout.addWidget(search_button)
        layout.addWidget(back_button)
        self.page2.setLayout(layout)

    """
    Ez itt kiköttötem később töröld vagy fejleszd le a  dinamikus keresést.
    """
    def create_page3(self):
        
        self.page3 = QWidget()
        layout = QVBoxLayout()

        label = QPushButton("3-as oldal")
        back_button = QPushButton("Előző Oldal")

    
        back_button.clicked.connect(self.show_page2)

        layout.addWidget(label)
        layout.addWidget(back_button)

        self.page3.setLayout(layout)

    def create_page4(self):
        
        self.page4 = QWidget()
        layout = QHBoxLayout()

        label = QPushButton("4-es oldal")
        back_button = QPushButton("Előző oldal")

        
        back_button.clicked.connect(self.show_page2)

        layout.addWidget(label)
        layout.addWidget(back_button)

        self.page4.setLayout(layout)

    """
    Ez az eredmény oldal amely kimutatja a pandas-ból visszadobott eredményeket egy görgethető listába dobja ahonnan
    egy  kiválasztott eredménnyel lehet majd műveletet végezni.
    """
    def create_page5(self):
        # Ez lesz az kereső eredmény oldal alap layoutja:
        self.page5 = QWidget()
        layout = QVBoxLayout()

        # Ez itt a lényeg a QListWidget hogy a lista görgethető legyen.
        self.result_list = QListWidget()
        self.result_list.setSelectionMode(QListWidget.SelectionMode.SingleSelection)

        # Itt hozzom létre a szükséges gombokat:
        print_button = QPushButton("Nyomtat")
        print_button.clicked.connect(self.print_selected_item)

        delete_button = QPushButton("Töröl")
        delete_button.clicked.connect(self.delete_selected_item)

        back_button = QPushButton("Vissza")
        back_button.clicked.connect(self.show_page2)

        # Az elején létre hozott widget-hez hozzá adom GUI funkciókat.
        layout.addWidget(self.result_list)
        layout.addWidget(print_button)
        layout.addWidget(delete_button)
        layout.addWidget(back_button)

        self.page5.setLayout(layout)

    """
     Ez a navigációs funkció a funkció változtatja vagy lépteti az oldalakat a setCurrentIndex-et változtatva
    """
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

    def show_page5(self):
        self.stacked_widget.setCurrentIndex(5)

    """
    Ez a hozzáadás fülön lévő adat grabber amely az egyes adatokat  megfogja és átadja a funkciónak.
    """
    def grab_data(self):
        # Retrieve the current values from the input fields
        
        user_data = make_user(
            self.system_serial_name_input.text(),
            self.system_owner_input.text(),
            self.user_name_input.text(),
            self.work_task_input.text(),
            self.user_number_input.text(),
            self.login_name_input.text(),
            self.organisation_unit_input.text(),
            self.phone_number_input.text(),
            self.date_of_education_input.text(),
            self.education_serial_number_input.text(),
            self.server_administrator_input.text(),
            
        )
        print(user_data)
        # Ez egy User objectet dob vissza a kimeneten.
        return user_data
    """
    Az adat feldolgozó egység a beolvasott adat és az excell között.
    """
    
    def process_data(self, data):
        if data is None:
            QMessageBox.warning(self, "Warning", "Nincs feldolgozható adat!")
            return
        
        # Excel fájl betöltése DataFrame-be
        file_path = "Névsor-jogigénylő_v4.252.xlsm"
        sheet_name = "új stuktúra"
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")
        
        # Az új adat objektummá alakítása
        # ITT MAJD MÉG MÓDOSÍTANI KELL ÉS STANDARDIZÁLNI KELL AZ INPUTOKAT. 
        # Hogy miből lehet választani illetve hogy mennyi kell.
        input_data = {
            "System Serial Name": data.system_serial_name,
            "System Owner": data.system_owner,
            "Név": data.user_name,
            "Feladatkör (szerepkörök)": data.work_task,
            "Tsz.": data.user_number,
            "Login Name": data.login_name,
            "Gép Üzemrésze\n (NH, H, \nNH-H)": data.organization_unit,
            "Phone Number": data.phone_number,
            "Date of Education": data.date_of_education,
            "Igénylőlap azonosító száma (kiadás)": data.education_serial_number,
            "Server Administrator": data.server_administrator,
        }
        input_series = pd.Series(input_data)
        
        # Új adat hozzáadása a DataFrame-hez
        df = pd.concat([df, input_series.to_frame().T], ignore_index=True)
        
        # Excel fájl frissítése
        print(df)
        with pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        QMessageBox.information(self, "Info", "Az adatokat sikeresen hozzáadtuk az Excel táblához!")


    """
    Ez itt a kereső alkalmazás amely  választható feltételekkel ez fog a pandának át dobni egy listát vagy egy hashmappet
    hogy abból keressen ezt még végig kéne azért gondolni.

    """

    def perform_search(self):
        # Ez lesz a return a feltételeket fogja tartalmazni.
        #z egy üres hashmap amelyet feltöltünk feltétekkel.
        search_criteria = {}

        # Itt adod hozzá az egyes feltételeket, if-ként ad hozzá a többit különben kilép.
        if self.user_number_checkbox.isChecked():
            search_criteria["torzsszam"] = self.user_number_input.text()

        if self.user_name_checkbox.isChecked():
            search_criteria["nev"] = self.user_name_input.text()

        if self.organization_unit_checkbox.isChecked():
            search_criteria["gepuzemreszere"] = self.organisation_unit_input.text()

        if self.system_serial_name_checkbox.isChecked():
            search_criteria["SYSID"] = self.system_serial_name_checkbox.text()

        if self.system_name_checkbox.isChecked():
            search_criteria["rendszermegnevezese"] = self.system_name_input.text()

        if self.login_name_checkbox.isChecked():
            search_criteria["login_felhasznaloikor"] = self.login_name_input.text()

        if self.work_task_checkbox.isChecked():
            search_criteria["feladatkor"] = self.work_task_input.text()    

        if self.education_serial_number_checkbox.isChecked():
            search_criteria["igenylolap_azonositoszam_kiadas"] = self.education_serial_number_input.text()

        if self.education_serial_number_checkbox.isChecked():
            search_criteria["igenylolap_azonositoszam_kiadas"] = self.education_serial_number_input.text()

        if self.job_status_checkbox.isChecked():
            search_criteria["statusz"] = self.job_status_input.text()
        
        if self.clearance_level_checkbox.isChecked():
            search_criteria["gepfelhasznaloi_szint"] = self.clearance_level_input.text()

        print(f"A keresési feltételek: {search_criteria}")
        
        # Kereséi feltétel majd a későbbiekben alakítsd át.
        results = self.mock_search_results(search_criteria)
        print("mock")
        
        # Itt töltöm fel a keresési eredményket a listába, előtte ha bent ragadt volna valami tisztitom.
        self.result_list.clear()
        for item in results:
            self.result_list.addItem(item)
        print("finish")

        # Váltás az eredményekre:
        self.show_page5()
        print("megnyittotam az 5-ös oldalt (EREDMÉNYEKET)")

        # Mock search funkció  amely az adott kritériák által  kiválasztott eredményket.
    def mock_search_results(self, criteria):
        # Ezt változtasd meg és kösd be a pandát.
        return ["Teszt adat 1", "Teszt adat 2", "Teszt adat 3"] if criteria else []
    """
    Ezeket  az funkciókat bekell kötni a  pandasba.
    """
    def print_selected_item(self):
        selected_item = self.result_list.currentItem()
        if selected_item:
            print(f"Kiválasztott elem: {selected_item.text()}")
        else:
            QMessageBox.warning(self, "Nincs kiválasztott elem", "Kérlek válasz egy elemet vagy módosíts a feltételeken.")
    
    def delete_selected_item(self):
        selected_item = self.result_list.currentItem()
        if selected_item:
            self.result_list.takeItem(self.result_list.row(selected_item))
            QMessageBox.information(self, "Az elem törölve", "A kiválasztott elem kilett törölve.")
        else:
            QMessageBox.warning(self, "Nincs kiválaszott elem", "Kérlek válaszd melyik elemet szertnéd tölteni.")
