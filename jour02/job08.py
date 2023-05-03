import mysql.connector
"""mysql> CREATE DATABASE zoo;
Query OK, 1 row affected (0,07 sec)

mysql> USE zoo;
Database changed
mysql> CREATE TABLE animal (
    -> id int primary key auto_increment,
    -> nom varchar(255),
    -> race varchar(255),
    -> id_cage int,
    -> ne varchar(255),
    -> pays varchar(255)
    -> );
Query OK, 0 rows affected (0,14 sec)
mysql> CREATE TABLE cage (
    -> id int primary key auto_increment,
    -> sup int,
    -> capacite int
    -> );
Query OK, 0 rows affected (0,04 sec)"""

class Animal:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="velvet",
            database="zoo"
        )
        
        self.mycursor = self.db.cursor()
    
    def create(self, nom, race ,id_cage, ne, pays):
        sql = "INSERT INTO animal (nom, race, id_cage, ne, pays) VALUES (%s, %s, %s, %s, %s)"
        val = (nom, race, id_cage, ne, pays),
        self.mycursor.execute(sql, val),
        self.db.commit()
        print(self.mycursor.rowcount, "enregistrement inséré.")
        
    def read (self):
        self.mycursor.execute("SELECT * FROM Zoo")
        result = self.mycursor.fetchall()
        for row in result:
            print(row)
            
    def update(self, id, nom, race, id_cage, ne, pays):
        sql = "UPDATE animal SET nom = %s, race =%s, id_cage = %s, ne = %s, pays = %s WHERE id = %s"
        val = (nom, race, id_cage, ne, pays, id)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "enregistrement(s) mis a jour.")
    
    def delete(self, id):
        sql = "DELETE FROM Zoo WHERE id = %s"
        val = (id)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "enregistrement(s) supprimé(s).")

class Cage:
    def __init__(self, id, sup, capacite):
        self.id = id
        self.sup = sup
        self.capacite = capacite
        print()        
db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="velvet",
      database="zoo"
)
cursor = db.cursor()
cursor.execute("SELECT SUM(sup) FROM cage")
result = cursor.fetchone()
print("superficie totale des cages:", result[0])