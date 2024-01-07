CREATE TABLE animals(
  pk INTEGER PRIMARY KEY AUTOINCREMENT,
  animal_name TEXT NOT NULL,
  height INTEGER NOT NULL,
  weight INTEGER NOT NULL,
  age INTEGER
);


PRAGMA table_info('animals');