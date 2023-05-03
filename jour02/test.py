import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="velvet",
    database="laplateforme",
)

# Execute the query and fetch the result
mycursor = db.cursor()
mycursor.execute("SELECT SUM(superficie) FROM etage")
result = mycursor.fetchone()

# Print the result
superficie_totale = result[0]
print("La superficie de La Plateforme est de", superficie_totale, "m2")
