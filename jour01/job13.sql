Afin de facilité le travail de l’administration , écrire une requête permettant de récupérer les élèves dont l’age est compris entre 18 et 25 ans.


mysql> SELECT * FROM etudiants WHERE age BETWEEN 18 AND 25;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  1 | Spaghetti | Betty    |  23 | betty.Spaghetti@laplateforme.io |
|  3 | Doe       | John     |  18 | john.doe@laplateforme.io        |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   |
|  7 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   |
+----+-----------+----------+-----+---------------------------------+
5 rows in set (0,00 sec)