import sqlite3

try:
    sql_conection = sqlite3.connect('sqlite_db.db')
    cursor = sql_conection.cursor()
    print("Baza danych zostałą podłączona")
except sqlite3.Error as e:
    print("Bład podczas podłączania bazy danych", e)
finally:
    if sql_conection:
        sql_conection.close()
        print("Baza danych zostałą zamknięta")
