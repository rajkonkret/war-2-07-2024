import sqlite3

try:
    sql_conetion = sqlite3.connect('sqlite_db.db')
    cursor = sql_conetion.cursor()
    print("Baza danych zostałą podłączona")
except sqlite3.Error as e:
    print("Bład podczas podłączania bazy danych", e)
finally:
    if sql_conetion:
        sql_conetion.close()
        print("Baza danych zostałą zamknięta")
