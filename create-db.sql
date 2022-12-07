/* Lage selve databasen */
Create database fingerfrenzy;

/* Lage tabellen */
Create table highscores (
    name VARCHAR(30),
    score DECIMAL(7,5)
);

/* Sette inn litt test-data i tabellen */
insert into highscores (name,score) values('Arvid','3.12345');
insert into highscores (name,score) values('Marie','2.22445');


/* Opprette en bruker som har full tilgang til denne databasen (og bare denne!) */
CREATE USER 'fingerfrenzy'@'localhost' IDENTIFIED BY 'Arvid123';
GRANT ALL PRIVILEGES ON fingerfrenzy.* TO 'fingerfrenzy'@'localhost';
FLUSH PRIVILEGES;
