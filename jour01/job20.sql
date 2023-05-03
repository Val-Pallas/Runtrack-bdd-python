À l’aide d’une requête SQL, compter le nombre d’étudiants mineur présent en base de données.

SELECT COUNT(*) FROM etudiants WHERE age < 18;
+----------+
| COUNT(*) |
+----------+
|        1 |
+----------+
1 row in set (0,00 sec)