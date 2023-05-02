CREATE DATABASE La Plateforme;

show databases;
USE LaPlateforme;

CREATE TABLE  etudiants(
    id (int),
    nom (varchar 255),
    prenom (varchar 25),
    age (int),
    email (varchar 255),
);

DESCRIBE etudiants;

SHOW COLUMNS FROM etudiants;
