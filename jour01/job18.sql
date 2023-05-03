DELETE FROM etudiants WHERE nom='Doe' AND prenom='John';
Query OK, 1 row affected (0,01 sec)

mysql> SELECT * FROM etudiants WHERE nom LIKE 'D%';
+----+--------+----------+-----+---------------------------------+
| id | nom    | prenom   | age | email                           |
+----+--------+----------+-----+---------------------------------+
|  5 | Dupuis | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis | Martin   |  18 | martin.dupuis@laplateforme.io   |
|  7 | Dupuis | Martin   |  18 | martin.dupuis@laplateforme.io   |
+----+--------+----------+-----+---------------------------------+
3 rows in set (0,01 sec)