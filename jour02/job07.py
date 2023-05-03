"""Créer une base de données SQL avec une table nommée “employes” contenant les champs suivants :
- id, int, primary key, auto-incrémente
- nom, varchar
- prenom, varchar
- salaire, decimal
- id_service, int
      
 Écrire une requête SQL pour récupérer tout les employées dont le salaire est supérieur à 3 000 €. Exécuter la requête et afficher le résultat.
Ajouter la table “services” contenant les champs suivants :
- id, int, primary key, auto-incrémente
- nom, varchar
Insérer des services dans votre table.
Récupérer tous les employés et leur service respectif. Afficher le résultat en console.
Créer une classe qui permet d’effectuer différentes opérations (CRUD) sur la table salariée. Vérifier que tout fonctionne correctement.
"""

#CREATE DATABASE usine;
#Query OK, 1 row affected (0,06 sec)
#SHOW usine;
#USE usine;
"""CREATE TABLE employes (
    ->   id int primary key auto_increment,
    ->   nom varchar(255),
    ->   prenom varchar(255),
    ->   salaire decimal(10, 2),
    ->   id_service int
    -> );
Query OK, 0 rows affected (0,23 sec)"""

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="velvet",
    database="usine",
)

print(db)
#Insérer des employées dans la table “employes”.
mycursor = db.cursor()
mycursor.execute("INSERT INTO employes(nom, prenom, salaire, id_service) VALUES ('Spaghetti', 'Betty', 2300, 1)")
mycursor.execute("INSERT INTO employes(nom, prenom, salaire, id_service) VALUES ('Steak', 'Chuck', 4500, 2)")
mycursor.execute("INSERT INTO employes(nom, prenom, salaire, id_service) VALUES ('Doe', 'John', 1800, 1)")
mycursor.execute("INSERT INTO employes(nom, prenom, salaire, id_service) VALUES ('Barnes', 'Binkie', 1600, 1)")
mycursor.execute("INSERT INTO employes(nom, prenom, salaire, id_service) VALUES ('Dupuis', 'Gertrude', 4200, 1)")

#Commit the changes
db.commit()
#print les results
mycursor.execute("SELECT * FROM employes")
employes = mycursor.fetchall()
# Print the results
for employe in employes:
  print(employe)

#Écrire une requête SQL pour récupérer tout les employées dont le salaire est supérieur à 3 000 €. Exécuter la requête et afficher le résultat.

mycursor.execute("SELECT salaire FROM employes ")
employes = mycursor.fetchall()
# Print the results
for employe in employes:
  print(employe)
  
  """Ajouter la table “services” contenant les champs suivants :
- id, int, primary key, auto-incrémente
- nom, varchar
CREATE TABLE services (
  id int primary key auto_increment,
  nom varchar(255)
);
Query OK, 0 rows affected (0,07 sec)
"""

#inserer des services dans la table


mycursor.execute("SELECT employes.nom, employes.prenom, services.nom FROM employes INNER JOIN services ON employes.id_service = services.id")

result = mycursor.fetchall()

for row in result:
    print(row)

import mysql.connector

class Salarie:
    
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="ma_base_de_donnees"
        )
        
        self.mycursor = self.db.cursor()
        
    def create(self, nom, prenom, salaire):
        sql = "INSERT INTO salarie (nom, prenom, salaire) VALUES (%s, %s, %s)"
        val = (nom, prenom, salaire)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "enregistrement inséré.")
        
    def read(self):
        self.mycursor.execute("SELECT * FROM salarie")
        result = self.mycursor.fetchall()
        for row in result:
            print(row)
            
    def update(self, id, nom, prenom, salaire):
        sql = "UPDATE salarie SET nom = %s, prenom = %s, salaire = %s WHERE id = %s"
        val = (nom, prenom, salaire, id)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "enregistrement(s) mis à jour.")
        
    def delete(self, id):
        sql = "DELETE FROM salarie WHERE id = %s"
        val = (id,)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "enregistrement(s) supprimé(s).")
