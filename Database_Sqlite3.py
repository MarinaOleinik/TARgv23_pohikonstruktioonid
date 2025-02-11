import select
from sqlite3 import *
from sqlite3 import Error
#---------------Funktioonide kirjeldus-----------
def create_connection(path:str):
    """Ühendus andmebaasiga
    """
    connection=None
    try:
        connection=connect(path)
        print("Ühendus on edukalt tehtud")
    except Error as e:
        print(f"Tekkis viga: '{e}'")
    return connection
def execute_query(connection,query:str):
    """Tabeli loomine
    """
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud või andmed on lisatud")
    except Error as e:
        print(f"Viga '{e}' tabeli loomisega")
def execute_read_query(connection,query:str):
    """Tabeli andmete vaatamine
    """
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        print(f"Viga '{e}'")
def execute_delete_query(connection,query:str):
    """Tabeli/andmete eemaldamine
    """   
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel/andmed on kustutatud")
    except Error as e:
        print(f"Viga '{e}'")
#---------------SQL laused----------------------
create_users_table="""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
gender TEXT,
student BOOLEAN
);
"""
create_users="""
INSERT INTO
    users(name,age,gender,student)
VALUES
    ('Mati',45,'mees',false),
    ('Kadri',18,'naide',true),
    ('Andres',25,'mees',true),
    ('Mari',65,'naine',true),
    ('Anna',97,'naine',false);
"""
select_users="SELECT * FROM users"
delete_data_from_users="DELETE FROM users WHERE student=true"
delete_tabel_users="DROP TABLE users"
#---------------Kasutame------------------------
conn=create_connection("C:/Users/marina.oleinik/source/repos/TARgv23_pohikonstruktioonid/AppData/data.db")
execute_query(conn,create_users_table)
execute_query(conn,create_users)
users=execute_read_query(conn,select_users)
print("Kasutajate andmed:")
for user in users:
    print(user)
execute_delete_query(conn,delete_data_from_users)
users=execute_read_query(conn,select_users)
print("Kustutatud tudengid, on jäänud neid kellel student=0:")
for user in users:
    print(user)
execute_delete_query(conn,delete_tabel_users)
