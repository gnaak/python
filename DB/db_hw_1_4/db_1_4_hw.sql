CREATE TABLE users (
    pk INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    phoneNumber TEXT NOT NULL,
    gender INTEGER,
    address TEXT NOT NULL DEFAULT 'no address'
);

ALTER TABLE users
RENAME COLUMN phoneNumber TO Number;

PRAGMA table_info('users');

DROP TABLE users;