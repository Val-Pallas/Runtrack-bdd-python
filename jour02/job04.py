"""Écrire un programme qui récupère tous les noms et les capacités de la table “salles” et afficher le résultat en console."""
# SELECT nom, capacite FROM salles
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="velvet",
    database="laplateforme",
)

print(db)
    
cursor = db.cursor()

cursor.execute("SELECT nom, capacite FROM salles;")
resultats = cursor.fetchall()
for resultat in resultats:
    print(resultat[0], resultat[1])