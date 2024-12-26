First steps.
Second steps.
The GUI has been made.
The Word_generator is under progress.
Gitignore for doc files added.

Data Format:
            "SYSID": data.system_serial_name,
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

Az adat feldolgozásnál járok meg van írva hogy a hozzáadás megcsinálja a dataframe-et
A hozzáadásnál standardizálni kell a jelenlegi rendszert.
Word_serializer.py = A Word_generátor