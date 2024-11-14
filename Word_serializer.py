#Az kapott adatott itt konvertáljuk át egy word alapú fájlba.
from docx import Document
from docx.shared import Cm
#Kezdeti teszt adatok később figyelni kell a serializálásra hogy  jól adjuk vissza lehet hogy
# jobb lenne nem kulcs indexek alapján pharsolnám be.
#ERRE MINDENKÉPPEN FIGYLEJ ODA A PANDAS BEKÖTÉSNÉL.
test_data = {
        #Egy oszlopos cellák:
        "rendszer_azonositoja_es_megnevezese":6578,
        "rendszer_tulajdonos":"Tulajdonos",
        "munkahelyi_vezeto": "Vezető",
        "felhasznalo_neve":"Kis Pista",
        "felhasznalo_feladatkore a rendszerben": "Operátor",

        "torzs_szama":23456,
        "login_nev":"Felhasznalónév",
        "szervezeti_egyseg":"RGK",

        "uj_felhasznalo":False,
        "modositas":False,
        "visszavonas":False,
        "elektronikus_felelosseg":False,

        "telefon": 36_20_345_67_89,
        "oktatas_datuma": 2020_05_06,
        "oktatasi_azonosito": "TGK-340",
        "rendszer_adminisztrator":"Rendszeradminisztrátor_Név",
        }

#Létrehozom a dokumentumot:
document = Document()

table = document.add_table(rows=15,cols=3,style='TableGrid')
#Beállítom a betű típust:
style = document.styles["Normal"]
style.font.name = "Calibri"

#Az első hatot kell  mergelem:
for row in range(0,6):
    cell = table.cell(row,0)
    for col in range(1,3):
        cell.merge(table.cell(row,col))

#Fejléc megadása:
table.cell(0,0).text = "Felhasználói jogok igénylése"


# Adat feltöltés első hatnál:
for row_count in range(1,6):
    table.cell(row_count,0).text = list(test_data.keys())[int(row_count)-1]

#2 oszlopos cellák:
cell = table.cell(6,0)
cell.merge(table.cell(6,1))

cell = table.cell(7,0)
cell.merge(table.cell(7,1))
       


  



#Fájl mentése:
document.save(str("Kérvény")+ '_' + str(test_data["torzs_szama"])+ '_' + test_data["felhasznalo"]+ '.docx')
#Funckió: