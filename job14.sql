Pour faciliter le travail de l’administration , écrire une requête permettant de récupérer les élèves dont l’age est compris entre 18 et 25 ans en triant par l’âge des étudiants par ordre croissant.

SELECT * FROM etudiants WHERE age BETWEEN 18 AND 25 ORDER BY age ASC;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  3 | Doe       | John     |  18 | john.doe@laplateforme.io        |
|  6 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   |
|  7 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  1 | Spaghetti | Betty    |  23 | betty.Spaghetti@laplateforme.io |
+----+-----------+----------+-----+---------------------------------+
5 rows in set (0,00 sec)