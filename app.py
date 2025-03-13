import pandas as pd
import mysql.connector
# Verbindung zur MySQL-Datenbank herstellen
conn = mysql.connector.connect(
 host="localhost",
 user="root",
 password="SeDlIc75NA!",
 database="mooncycle"
)
cursor = conn.cursor()
# Excel-Datei einlesen
#excel_data = pd.read_excel("./data/tbl_ingredient.xlsx")
# Überprüfen, wie die Excel-Daten aussehen
#print(excel_data.head())

# Insert data into INGREDIENT table
#sql = "INSERT INTO tbl_ingredient (ingr_ID, ingr_name, nutrient_ID, category_ID, effect, phase_ID) VALUES (%s, %s, %s, %s, %s,%s)"
#values = [
#    (194, "Apple", 3, 7, "unknown", 3),
#    (195, "Orange", 3, 7, "unknown", 3),
#    (196, "Banana", 3, 7, "unknown", 3),
#    (197, "Kiwi", 3, 7, "unknown", 3),
#    (198, "Pineapple", 3, 7, "unknown", 3),
#    (199, "Pear", 3, 7, "unknown", 3)
#]

# Insert data into USER table
sql = "INSERT INTO tbl_user (field, first_name, last_name, age, weight, email) VALUES (%s, %s, %s, %s, %s,%s)"
values = [
    (4, "Andrea", "Müller", 25, 60, "andrea@gmail.com"),
    (5, "Maria", "Schmidt", 35, 80, "maria@gmail.com"),
    (6, "Julia", "Meier", 45, 70, "julia@gmail.com"),
    (7, "Jana", "Koch", 55, 90, "jana@gmail.com"),
    (8, "Anna", "Bauer", 65, 75, "ana@gmail.com"),
    (9, "Lena", "Beck", 75, 65, "lena@gmail.com")
]
cursor.executemany(sql, values)  # Insert multiple rows at once

# Commit the changes
conn.commit()

print(f"{cursor.rowcount} records inserted.")