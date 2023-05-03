"""À l’aide d’une requête, calculer la somme des capacités des salles et afficher le résultat en console."""

#SLECT SUM(capacite) AS total_capacite FROM salles
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="velvet",
    database="laplateforme",
)

print(db)

cursor = db.cursor()

cursor.execute("SELECT SUM(capacite) AS total_capacite FROM salles")
resultats = cursor.fetchall()
total_capacite = resultats[0]
for resultat in resultats:
    print("La capacite des salles de La Plateforme est de:", resultat[0],"m")