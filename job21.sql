À l’aide d’une requête SQL, compter le nombre d’étudiants dont l’age est compris entre 18 et 25 ans présents en base de données.

SELECT COUNT(*) FROM etudiants WHERE age BETWEEN 18 AND 25;
+----------+
| COUNT(*) |
+----------+
|        4 |
+----------+
1 row in set (0,00 sec)