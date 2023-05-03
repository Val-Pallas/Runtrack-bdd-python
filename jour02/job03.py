"""Ajouter les données suivantes a la table “etage” : - RDC, 0, 500
- R+1, 1, 500
Ajouter les données suivantes a la table “salles” :
  - - - - - -
Lounge, 1, 100 Studio Son, 1, 5
Broadcasting, 2, 50
Bocal Peda, 2, 4 Coworking, 2, 80 Studio Video, 2, 5
 Exporter votre base de données."""
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="velvet",
    database="laplateforme",
)

print(db)
# Query all the students
mycursor = db.cursor()
mycursor.execute("INSERT INTO etage(nom,numero, superficie) VALUES ('RDC', 0, 500)")
mycursor.execute("INSERT INTO etage (nom, numero, superficie) VALUE ('R+1',1, 500)")                 
#insert data into the table "salle"
mycursor.execute("INSERT INTO salles(nom, id_etage, capacite) VALUE ('Lounge', 1, 100)")
mycursor.execute("INSERT INTO salles(nom, id_etage, capacite) VALUE ('Studio Son', 1, 5)")
mycursor.execute("INSERT INTO salles(nom, id_etage, capacite) VALUE ('Broadcasting', 2, 50)")
mycursor.execute("INSERT INTO salles(nom, id_etage, capacite) VALUE ('Bocal Peda', 2, 4)")                
mycursor.execute("INSERT INTO salles(nom, id_etage, capacite) VALUE ('Coworking', 2, 80 )")
mycursor.execute("INSERT INTO salles(nom, id_etage, capacite) VALUE ('Studio Video', 2, 5)")



#Commit the changes
db.commit()
#print les results
mycursor.execute("SELECT * FROM etage")
etages = mycursor.fetchall()
# Print the results
for etage in etages:
  print(etage)
  
mycursor.execute("SELECT * FROM salles")
salles = mycursor.fetchall()
# Print the results
for salle in salles:
  print(salle)