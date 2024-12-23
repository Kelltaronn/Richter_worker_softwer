#Import's:
import pandas as pd

"""
Ez a hozzáadás fülön lévő adat grabber amely az egyes adatokat  megfogja és átadja a funkciónak.
"""

def grab_data(self):
    data = {
        "Rendszer Azonosítója és Megnevezése": self.system_serial_name_input.text(),
        "Rendszer Tulajdonos": self.system_owner_input.text(),
        "Felhasználó Neve": self.user_name_input.text(),
        "Felhasználó Feladatköre a rendszerben": self.work_task_input.text(),
        "Törzs száma": self.user_number_input.text(),
        "Login Név": self.login_name_input.text(),
        "Szervezeti egység": self.organization_unit_input.text(),
        "Telefonszám": self.phone_number_input.text(),
        "Oktatás Dátuma": self.date_of_education_input.text(),
        "Oktatási Azonosító": self.education_serial_number_input.text(),
        "Rendszer Adminisztrátor": self.server_administrator_input.text(),
    }

    selected_action_id = self.user_action_group.checkedId()
    action_mapping = {1: "Új Felhasználó", 2: "Módosítás", 3: "Visszavonás"}
    selected_action = action_mapping.get(selected_action_id, "Nincs kiválasztva")

    data["Felhasználói művelet"] = selected_action

    # Create a pandas DataFrame
    df = pd.DataFrame([data])
    print(df)


"""
Az adat feldolgozó egység a beolvasott adat és az excell között.
"""

def process_data(data):
     # Ez majd át kell írni itt hogy behívja az excell fájl beolvassa egy dataframeként és egy seriesé alakitva,
        #Ide kell egy open file funció lehet több funkció is használja majd ezt.
        df = pd.read_excel("Névsor-jogigénylő_v4.252.xlsm","új stuktúra")
        input_data = pd.DataFrame([data])
        print(input_data)
        updated_df = pd.concat([df,input_data],ignore_index=True)


        print(updated_df)