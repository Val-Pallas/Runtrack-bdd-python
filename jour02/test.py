import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="velvet",
    database="laplateforme",
)

print(db)

# Insert data into the table "etage"
mycursor = db.cursor()
mycursor.execute("INSERT INTO etage(nom, numero, superficie) VALUES ('RDC', 0, 500)")
mycursor.execute("INSERT INTO etage (nom, numero, superficie) VALUE ('R+1',1, 500)")

# Insert data into the table "salle"
mycursor.execute("INSERT INTO salle(nom, id_etage, capacite) VALUES ('Lounge', 1, 100)")
mycursor.execute("INSERT INTO salle(nom, id_etage, capacite) VALUES ('Studio Son', 1, 5)")
mycursor.execute("INSERT INTO salle(nom, id_etage, capacite) VALUES ('Broadcasting', 2, 50)")
mycursor.execute("INSERT INTO salle(nom, id_etage, capacite) VALUES ('Bocal Peda', 2, 4)")
mycursor.execute("INSERT INTO salle(nom, id_etage, capacite) VALUES ('Coworking', 2, 80 )")
mycursor.execute("INSERT INTO salle(nom, id_etage, capacite) VALUES ('Studio Video', 2, 5)")

# Commit the changes
db.commit()

# Print the results for the table "etage"
mycursor.execute("SELECT * FROM etage")
etages = mycursor.fetchall()
for etage in etages:
  print(etage)

# Print the results for the table "salle"
mycursor.execute("SELECT * FROM salle")
salles = mycursor.fetchall()
for salle in salles:
  print(salle)
