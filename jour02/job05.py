"""À l’aide d’un requête calculer la superficie de l’ensemble des étages et afficher “La superficie de La Plateforme est de X m2”, X étant le résultat de la requête."""

#SLECT SUM(superficie) FROM etage
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="velvet",
    database="laplateforme",
)

print(db)

cursor = db.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage;")
resultats = cursor.fetchall()
for resultat in resultats:
    print(resultat)