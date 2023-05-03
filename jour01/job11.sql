Vous souhaitez récupérer les informations de Gertrude Dupuis. Écrire une requête SQL permettant la récupération de ces informations.
SELECT * FROM etudiants WHERE nom = 'Dupuis' AND prenom = 'Gertrude';
+----+--------+----------+-----+---------------------------------+
| id | nom    | prenom   | age | email                           |
+----+--------+----------+-----+---------------------------------+
|  5 | Dupuis | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
+----+--------+----------+-----+---------------------------------+
1 row in set (0,00 sec)
