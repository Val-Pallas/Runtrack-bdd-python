À l’aide d’une requête SQL, compter le nombre d’étudiants présent en base de données.
SELECT COUNT(*) FROM etudiants;
+----------+
| COUNT(*) |
+----------+
|        6 |
+----------+
1 row in set (0,01 sec)

 SELECT * FROM etudiants;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  1 | Spaghetti | Betty    |  20 | betty.Spaghetti@laplateforme.io |
|  2 | Steak     | Chuck    |  45 | chuck.steak@laplateforme.io     |
|  4 | Barnes    | Binkie   |  16 | binkie.barnes@laplateforme.io   |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   |
|  7 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   |
+----+-----------+----------+-----+---------------------------------+