À l’aide d’une requête SQL, récupérer les informations de l’étudiant le plus âgé.

SELECT * FROM etudiants ORDER BY age DESC LIMIT 1;
+----+-------+--------+-----+-----------------------------+
| id | nom   | prenom | age | email                       |
+----+-------+--------+-----+-----------------------------+
|  2 | Steak | Chuck  |  45 | chuck.steak@laplateforme.io |
+----+-------+--------+-----+-----------------------------+
1 row in set (0,00 sec)