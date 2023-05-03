"""Job 2
À l'aide de votre terminal SQL, créez les tables suivantes :
- “etage” ayant comme champs :
● id, int, clé primaire et Auto Incrément
● nom, varchar de taille 255 ● numero, int
● superficie, int
- “salles” ayant comme champs :
● id, int, clé primaire et Auto Incrément
● nom, varchar de taille 255 ● id_etage, int
● capacite, int"""

"""CREATE TABLE etage(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    numero INT,
    superficie INT
);

CREATE TABLE salles(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR (255),
    id_etage INT,
    capacite INT
);"""

"""mysql> USE laplateforme
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> CREATE TABLE etage(
    ->     id INT PRIMARY KEY AUTO_INCREMENT,
    ->     nom VARCHAR(255),
    ->     numero INT,
    ->     superficie INT
    -> );

CREATE TABLE salles(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR (255),
    id_etage INT,
    capacite INT
);Query OK, 0 rows affected (0,13 sec)

mysql> 
mysql> CREATE TABLE salles(
    ->     id INT PRIMARY KEY AUTO_INCREMENT,
    ->     nom VARCHAR (255),
    ->     id_etage INT,
    ->     capacite INT
    -> );
Query OK, 0 rows affected (0,05 sec)"""