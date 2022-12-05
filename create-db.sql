Create database fingerfrenzy;

Create table highscores (
    name VARCHAR(30),
    score DECIMAL(7,5)
);


insert into highscores (name,score) values('Arvid','3.12345');
insert into highscores (name,score) values('Marie','2.22445');



CREATE USER 'fingerfrenzy'@'localhost' IDENTIFIED BY 'Arvid123';
GRANT ALL PRIVILEGES ON fingerfrenzy.* TO 'fingerfrenzy'@'localhost';
FLUSH PRIVILEGES;