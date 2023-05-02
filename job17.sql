Suite à une erreur de saisie, l’age de Betty Spaghetti n’est pas correct. À l’aide d’une requête, modifier la valeur de l’age de Betty de 23 ans a 20 ans.
UPDATE etudiants SET age = 20 WHERE nom = 'Spaghetti' AND prenom = 'Betty';
Query OK, 1 row affected (0,01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

SELECT * FROM etudiants WHERE prenom LIKE 'b%';                         
+----+-----------+--------+-----+---------------------------------+
| id | nom       | prenom | age | email                           |
+----+-----------+--------+-----+---------------------------------+
|  1 | Spaghetti | Betty  |  20 | betty.Spaghetti@laplateforme.io |
|  4 | Barnes    | Binkie |  16 | binkie.barnes@laplateforme.io   |
+----+-----------+--------+-----+---------------------------------+
2 rows in set (0,00 sec)