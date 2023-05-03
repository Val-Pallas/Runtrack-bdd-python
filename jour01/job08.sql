"""À l’aide d’une requête SQL, récupérer la liste des étudiants de moins de 18 ans.
Liste des etudiants de moins de 18 ans.
Créer un fichier nommé “job8.sql” et écrire la requête exécutée."""

SELECT * FROM etudiants WHERE age < 18;
Database changed
mysql> SELECT * FROM etudiants WHERE age < 18;
+----+--------+--------+-----+-------------------------------+
| id | nom    | prenom | age | email                         |
+----+--------+--------+-----+-------------------------------+
|  4 | Barnes | Binkie |  16 | binkie.barnes@laplateforme.io |
+----+--------+--------+-----+-------------------------------+
1 row in set (0,00 sec)