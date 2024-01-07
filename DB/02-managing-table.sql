CREATE TABLE examples (
  ExampleID INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

-- 테이블 스키마(구조) 확인
PRAGMA table_info('new_examples');

-- ALTER : Change.
SELECT sqlite_version();

ALTER TABLE
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL,

ALTER TABLE
  examples
ADD COLUMN
  Age INTEGER NOT NULL;
  
ALTER TABLE
  examples
ADD COLUMN
  Address VARCHAR(100) NOT NULL;

ALTER TABLE examples
RENAME COLUMN Address TO PostCode;

ALTER TABLE examples
DROP COLUMN PostCode;

DROP TABLE new_examples;

ALTER TABLE examples
RENAME TO new_examples;

-- 실습용 테이블
CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt Date NOT NULL
);

PRAGMA table_info('articles');

SELECT * FROM articles;

INSERT INTO
  articles(title, content, createdAt)
VALUES
  ('hello','world','2000-01-01');

UPDATE articles
SET 
  title = 'T1',
  content = 'C1'
WHERE 
  id = 2;

DELETE FROM articles
WHERE id = 1;

-- DROP TABLE users;
-- DROP TABLE articles;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(100) NOT NULL,
    userId INTEGER NOT NULL,
    FOREIGN KEY (userId)
    REFERENCES users(id)
);

INSERT INTO
    users (name)
VALUES
    ('하석주'),
    ('송윤미'),
    ('유하선');
INSERT INTO
    articles (title, content, userId)
VALUES
    ('제목1', '내용1', 1),
    ('제목2', '내용2', 2),
    ('제목3', '내용3', 1),
    ('제목4', '내용4', 4),
    ('제목5', '내용5', 1);

SELECT * FROM users;
SELECT * FROM articles;

SELECT * FROM articles JOIN USER;
-- 카테시안 곱 -> 모든 경우의 수를 다 조합

SELECT * 
  FROM articles
  -- JOIN users
  INNER JOIN users
  ON articles.userId = users.id;


SELECT * 
  FROM articles
  -- JOIN users
  INNER JOIN users
  ON articles.userId = users.id
  WHERE userS.id = 1;

SELECT * 
  FROM articles
  LEFT JOIN users
  ON articles.userId = users.id;

SELECT * 
  FROM articles
  RIGHT JOIN users
  ON articles.userId = users.id;

SELECT * 
  FROM articles
  FULL JOIN users
  ON articles.userId = users.id;