CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL default 0,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 5, 180, 210);

alter table zoo
add column rowid integer;

INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(10, 'alligator', 'carnivore', 250, 50);

INSERT INTO zoo (name, eat, age) VALUES
('dolphin', 'carnivore', 3);

PRAGMA table_info('zoo');
select * from zoo;


