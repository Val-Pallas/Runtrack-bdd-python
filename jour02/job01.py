"""Récupérer votre base de données “LaPlateforme” créée hier. À l’aide du module “mysql-python-connector”, connectez-vous à votre base de données “LaPlateforme”.
Récupérer l’ensemble des étudiants et afficher le résultat de la requête en console."""
import mysql.connector

#Connect to the laplateforme database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="velvet",
    database="laplateforme",
)

print(db)
# Query all the students
mycursor = db.cursor()
mycursor.execute("SELECT * FROM etudiants")
students = mycursor.fetchall()

# Print the results
for student in students:
  print(student)
