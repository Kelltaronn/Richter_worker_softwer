"""
A szükséges könyvtár betöltések és egyéb futás előtti  műveletek helyei
"""
from File_searching_module import open_file_system
from error_handling_messages import warning_error_message
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
                             QApplication
                             )
#Other Modules:
from Standardized_input_field import standardized_input_field


"""
Ez A szoftver GUI-ja itt változtathatóak az oldalak számai funkciói a rajtuk lévő elemek mennyisége és minősége.

A MainWindow class foglalja magába mind ezt.
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
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
        system_serial_name_layout = QHBoxLayout()

        system_serial_name_label = QLabel("Rendszer Azonosítója és Megnevezése:")
        system_serial_name_label.setFixedWidth(standardized_label_width)

        self.system_serial_name_input = QLineEdit()
        self.system_serial_name_input.setFixedWidth(standardized_input_width)

        system_serial_name_layout.addWidget(system_serial_name_label,alignment=Qt.AlignmentFlag.AlignRight)
        system_serial_name_layout.addWidget(self.system_serial_name_input,alignment=Qt.AlignmentFlag.AlignLeft)

        #Input 2:.
        system_owner_layout = QHBoxLayout()

        system_owner_label = QLabel("Rendszer Tulajdonos:")
        system_owner_label.setFixedWidth(standardized_label_width)

        self.system_owner_input= QLineEdit()
        self.system_owner_input.setFixedWidth(standardized_input_width)

        system_owner_layout.addWidget(system_owner_label,alignment=Qt.AlignmentFlag.AlignRight)
        system_owner_layout.addWidget(self.system_owner_input,alignment=Qt.AlignmentFlag.AlignLeft)

        #Input 3:
        user_name_layout = QHBoxLayout()

        user_name_label = QLabel("Felhasználó Neve:")
        user_name_label.setFixedWidth(standardized_label_width)
        
        self.user_name_input = QLineEdit()
        self.user_name_input.setFixedWidth(standardized_input_width)

        user_name_layout.addWidget(user_name_label,alignment=Qt.AlignmentFlag.AlignRight)
        user_name_layout.addWidget(self.user_name_input,alignment=Qt.AlignmentFlag.AlignLeft)

        #Input 4:
        work_task_layout = QHBoxLayout()

        work_task_label = QLabel("Felhasználó Feladatköre a rendszerben:")
        work_task_label.setFixedWidth(standardized_label_width)

        self.work_task_input = QLineEdit()
        self.work_task_input.setFixedWidth(standardized_input_width)
        
        work_task_layout.addWidget(work_task_label,alignment=Qt.AlignmentFlag.AlignRight)
        work_task_layout.addWidget(self.work_task_input,alignment=Qt.AlignmentFlag.AlignLeft)

        #Input 5:
        user_number_layout = QHBoxLayout()

        user_number_label = QLabel("Törzs száma:")
        user_number_label.setFixedWidth(standardized_label_width)

        self.user_number_input = QLineEdit()
        self.user_number_input.setFixedWidth(standardized_input_width)

        user_number_layout.addWidget(user_number_label,alignment=Qt.AlignmentFlag.AlignRight)
        user_number_layout.addWidget(self.user_number_input,alignment=Qt.AlignmentFlag.AlignLeft)


        #Input 6:
        login_name_layout = QHBoxLayout()

        login_name_label = QLabel("Login Név:")
        login_name_label.setFixedWidth(standardized_label_width)

        self.login_name_input = QLineEdit()
        self.login_name_input.setFixedWidth(standardized_input_width)

        login_name_layout.addWidget(login_name_label,alignment=Qt.AlignmentFlag.AlignRight)
        login_name_layout.addWidget(self.login_name_input,alignment=Qt.AlignmentFlag.AlignLeft)


        #Input 7:
        organisation_unit_layout = QHBoxLayout()

        organisation_unit_label = QLabel("Szervezeti egység:")
        organisation_unit_label.setFixedWidth(standardized_label_width)

        self.organization_unit_input = QLineEdit()
        self.organization_unit_input.setFixedWidth(standardized_input_width)

        organisation_unit_layout.addWidget(organisation_unit_label,alignment=Qt.AlignmentFlag.AlignRight)
        organisation_unit_layout.addWidget(self.organization_unit_input,alignment=Qt.AlignmentFlag.AlignLeft)


        #Input 8:
        phone_number_layout = QHBoxLayout()

        phone_number_label = QLabel("Telefonszám:")
        phone_number_label.setFixedWidth(standardized_label_width)

        self.phone_number_input = QLineEdit()
        self.phone_number_input .setFixedWidth(standardized_input_width)

        phone_number_layout.addWidget(phone_number_label,alignment=Qt.AlignmentFlag.AlignRight)
        phone_number_layout.addWidget(self.phone_number_input,alignment=Qt.AlignmentFlag.AlignLeft)


        #Input 9:
        date_of_education_layout = QHBoxLayout()

        date_of_education_label = QLabel("Oktatás Dátuma:")
        date_of_education_label.setFixedWidth(standardized_label_width)

        self.date_of_education_input = QLineEdit()
        self.date_of_education_input.setFixedWidth(standardized_input_width)

        date_of_education_layout.addWidget(date_of_education_label,alignment=Qt.AlignmentFlag.AlignRight)
        date_of_education_layout.addWidget(self.date_of_education_input,alignment=Qt.AlignmentFlag.AlignLeft)


        #Input 10:
        education_serial_number_layout = QHBoxLayout()

        education_serial_number_label = QLabel("Oktatási Azonosító:")
        education_serial_number_label.setFixedWidth(standardized_label_width)

        self.education_serial_number_input = QLineEdit()
        self.education_serial_number_input.setFixedWidth(standardized_input_width)

        education_serial_number_layout.addWidget(education_serial_number_label,alignment=Qt.AlignmentFlag.AlignRight)
        education_serial_number_layout.addWidget(self.education_serial_number_input,alignment=Qt.AlignmentFlag.AlignLeft)


        #Input 11:
        server_administrator_layout = QHBoxLayout()

        server_administrator_label = QLabel("Rendszer Adminisztrátor:")
        server_administrator_label.setFixedWidth(standardized_label_width)

        self.server_administrator_input = QLineEdit()
        self.server_administrator_input.setFixedWidth(standardized_input_width)

        server_administrator_layout.addWidget(server_administrator_label,alignment=Qt.AlignmentFlag.AlignRight)
        server_administrator_layout.addWidget(self.server_administrator_input,alignment=Qt.AlignmentFlag.AlignLeft)

        """
        #Checkbox items:
        """
        #Checkbox 1:
        checkbox_widget = QWidget()
        checkbox_user_layout = QHBoxLayout()

        new_user_label = QRadioButton("Új Felhasználó:")
        change_user_label = QRadioButton("Módosítás:")
        cancel_user_label = QRadioButton("Visszavonás:")

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

        # Ez itt az adatbevétel gombja
        grab_data_button = QPushButton("Adatbevitel")
        grab_data_button.clicked.connect(self.grab_data) #Ha ezt itt lenyomom itt az adat később panda bekötése a funkcióba.
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

        # Ez a kikapcsolható  név alapú kereső mező:
        self.name_checkbox = QCheckBox("Keresés Név alapján:")
        self.name_input = QLineEdit()
        self.name_input.setEnabled(False)  # Ezek a sorok meglesznek ismételve alapból kilesz kapcsolva az összes.

        # Ez a kikapcsolható  kor alapú kereső mező:
        self.age_checkbox = QCheckBox("Keresés Kor alapján")
        self.age_input = QLineEdit()
        self.age_input.setEnabled(False)  # Ezek a sorok meglesznek ismételve alapból kilesz kapcsolva az összes.

        # Ez a kikapcsolható  beosztás alapú kereső mező:
        self.profession_checkbox = QCheckBox("Keresés beosztás alapján:")
        self.profession_input = QLineEdit()
        self.profession_input.setEnabled(False)  # Ezek a sorok meglesznek ismételve alapból kilesz kapcsolva az összes.

        # Itt kel bekotni a  ki-be kapcsoló gombokat a mezőkhöz.
        self.name_checkbox.stateChanged.connect(lambda: self.name_input.setEnabled(self.name_checkbox.isChecked()))
        self.age_checkbox.stateChanged.connect(lambda: self.age_input.setEnabled(self.age_checkbox.isChecked()))
        self.profession_checkbox.stateChanged.connect(lambda: self.profession_input.setEnabled(self.profession_checkbox.isChecked()))

        # Ez betölti  az egyes már előzőleg meghatárott gombokat mezőket.
        #FONTOS A SORREND SZÁMÍT!!!!!!!!!!!!!!!!
        layout.addWidget(self.name_checkbox)
        layout.addWidget(self.name_input)
        layout.addWidget(self.age_checkbox)
        layout.addWidget(self.age_input)
        layout.addWidget(self.profession_checkbox)
        layout.addWidget(self.profession_input)

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
        # Ez a funkció kiveszi az adato és meghívja a feldolgozás funkciót.
        # Lehet később összekéne olvasztani ha nem szükséges máshonnan adatot mozgatni!!!!
        name = self.name_input.text()
        age = self.age_input.text()
        profession = self.profession_input.text()
        self.process_data(name, age, profession)
        print("I grabbed data")


    """
    Az adat feldolgozó egység a beolvasott adat és az excell között.
    """

    def process_data(self, name, age, profession):
        # Ez majd át kell írni itt hogy behívja az excell fájl beolvassa egy dataframeként és egy seriesé alakitva,
        # hozzá rakja  majd a további adatot.
        print(f"Feldolgozott adat:\nNév: {name}\nKor: {age}\nBeosztás: {profession}")


    """
    Ez itt a kereső alkalmazás amely  választható feltételekkel ez fog a pandának át dobni egy listát vagy egy hashmappet
    hogy abból keressen ezt még végig kéne azért gondolni.
    """

    def perform_search(self):
        # Ez lesz a return a feltételeket fogja tartalmazni.
        search_criteria = {}

        # Itt adod hozzá az egyes feltételeket, if-ként ad hozzá a többit különben kilép.
        if self.name_checkbox.isChecked():
            search_criteria["Név"] = self.name_input.text()
        if self.age_checkbox.isChecked():
            search_criteria["Kor"] = self.age_input.text()
        if self.profession_checkbox.isChecked():
            search_criteria["Beosztás"] = self.profession_input.text()

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
        print("show")

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
    

    """
    A Fájl tallózás rendszer megírása:
    """
"""
    def open_file_system(self):
        file_dialog = QFileDialog()
        file_path = file_dialog.getOpenFileName(self,"Fájl Keresése","",filter="*.txt")

        if file_path:
            print(f"Selected file: {file_path}")  # Do something with the selected file path
"""