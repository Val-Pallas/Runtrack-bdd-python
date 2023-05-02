"""À l’aide d’une requête SQL, ajouter les étudiants suivants :
- Betty Spaghetti, 23 ans, betty.Spaghetti@laplateforme.io
- Chuck Steak, 45 ans, chuck.steak@laplateforme.io
- John Doe, 18 ans, john.doe@laplateforme.io
- Binkie Barnes, 16 ans, binkie.barnes@laplateforme.io
- Gertrude Dupuis, 20 ans, gertrude.dupuis@laplateforme.io"""

INSERT INTO etudiants (nom, prenom, age, email)
VALUES
('Spaghetti', 'Betty', 23, 'betty.Spaghetti@laplateforme.io'),
('Steak', 'Chuck', 45, 'chuck.steak@laplateforme.io'),
('Doe', 'John', 18, 'john.doe@laplateforme.io'),
('Barnes', 'Binkie', 16, 'binkie.barnes@laplateforme.io'),
('Dupuis', 'Gertrude', 20, 'gertrude.dupuis@laplateforme.io');
