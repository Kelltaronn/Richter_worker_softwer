"""
A szükséges könyvtár betöltések és egyéb futás előtti  műveletek helyei
"""

#Import's:
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
                             QCheckBox
                             )

"""
Ez A szoftver GUI-ja itt változtathatóak az oldalak számai funkciói a rajtuk lévő elemek mennyisége és minősége.

A MainWindow class foglalja magába mind ezt.
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        

        # Alap funkciók és méretek a software-hez.
        
        self.setWindowTitle("Main Window with Navigation")
        self.setGeometry(200, 200, 400, 300)

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
        self.main_page = QWidget()
        layout = QVBoxLayout()

        # Gombok a kezdő lapon.
        page1_button = QPushButton("Hozzáadás")
        page2_button = QPushButton("Keresés")

        # Ezek kötik össze a gombokat a funkciókkal ha hibába futsz nézd meg lejjebb hogy a funkció jó-e vagy van.
        page1_button.clicked.connect(self.show_page1)
        page2_button.clicked.connect(self.show_page2)

        layout.addWidget(page1_button)
        layout.addWidget(page2_button)

        self.main_page.setLayout(layout)


    """
    Ez itt a hozzáadási oldal:
    """
    def create_page1(self):
        self.page1 = QWidget()
        layout = QVBoxLayout()

        # Itt csinálom meg az egymás alatt lévő input dobozokat.
        form_layout = QVBoxLayout()

        #Input doboz a névhez:
        name_layout = QHBoxLayout()
        name_label = QLabel("Név:")
        self.name_input = QLineEdit()

        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)

        #Input doboz a korhoz.
        age_layout = QHBoxLayout()
        age_label = QLabel("Kor:")
        self.age_input = QLineEdit()

        #Ráteszem az age inputokat az oldalra
        age_layout.addWidget(age_label)
        age_layout.addWidget(self.age_input)

        #Input doboz a foglalkozáshoz.
        profession_layout = QHBoxLayout()
        profession_label = QLabel("Beosztás:")
        self.profession_input = QLineEdit()

        profession_layout.addWidget(profession_label)
        profession_layout.addWidget(self.profession_input)

        # Az előző inputokat hozzá kell adnom egy input Layout form-hoz!
        form_layout.addLayout(name_layout)
        form_layout.addLayout(age_layout)
        form_layout.addLayout(profession_layout)

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