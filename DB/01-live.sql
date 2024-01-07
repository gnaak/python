-- SQLite

-- 한 줄 주석
/*
여러 줄 주석
...
*/

SELECT
    -- 조회할 필드(열)
    LastName
FROM -- ~로부터
    -- 테이블명
    employees;

SELECT
    -- 조회할 필드(열)
    FirstName,
    LastName
FROM -- ~로부터
    -- 테이블명
    employees;

SELECT
    *, -- 모든 열을 조회
    FirstName,
    *
FROM -- ~로부터
    -- 테이블명
    employees;

SELECT
    FirstName AS '이름'
FROM
    employees;

SELECT
    Name,
    Milliseconds / 60000 AS '재생 시간 (분)'
FROM
    tracks;

SELECT
    FirstName,
    LastName
FROM
    employees
ORDER BY
    -- FirstName ASC;
    -- FirstName;
    LastName DESC;
    -- 오름차순이 기본
    -- sorted?

SELECT
    Country,
    City
FROM
    customers
ORDER BY
    Country DESC,
    City;

-- NULL
-- Python : None

SELECT
    ReportsTo
FROM
    employees
ORDER BY
    ReportsTo DESC;

SELECT DISTINCT
    Country
FROM
    customers;

-- SELECT하고 난 결과물이 (record, tuple, row)
-- 중복되지 않은 결과물
SELECT DISTINCT
    Country,
    City
FROM
    customers;  

-- SELECT DISTINCT
--     *
-- FROM
--     customers;

-- WHERE
SELECT
    -- *
    LastName, FirstName, City
FROM
    customers
WHERE
    City = 'Prague'
    -- 비교연산자, 논리연산자
    -- OR City = 'New York';
    -- City = 'Prague';
    AND FirstName = 'Helena';

-- 비교 연산자가 안 먹히는 값
SELECT
    LastName, FirstName, Company, Country
FROM
    customers
WHERE
    -- Company != 'Google Inc.';
    -- Company = NULL;
    Company IS NOT NULL;
    -- NULL에 대한 비교 연산 시도시 False 취급

-- BETWEEN A and B
SELECT Name, Bytes
FROM tracks
WHERE
    -- Bytes >= 100000
    -- AND Bytes <= 500000; -- A < x < B 이거 안됨
    -- Bytes BETWEEN 100000 and 500000;
    Bytes BETWEEN 161266 and 387360;
    -- 시작점과 끝점 포함? => 시작점과 끝점 포함

-- IN -> 멤버십 연산자
SELECT
    LastName, FirstName, Country
FROM
    customers
WHERE
    Country IN ('Canada', 'Germany', 'France');

-- LIKE - 닮다, ~처럼

SELECT
    LastName, FirstName
FROM
    customers
WHERE
    -- LastName LIKE '%son';
    -- LastName LIKE 'J%son';
    -- LastName LIKE '%er%';
    -- LastName LIKE 'b%n%d';
    -- FirstName LIKE '___a';
    FirstName LIKE '____a';

-- LIMIT
SELECT
    TrackId, Name, Bytes
FROM
    tracks
-- WHERE
--     TrackId = 3224
ORDER BY Bytes DESC
-- LIMIT 7;
-- LIMIT 3, 4; -- M번째 데이터부터 N개
-- 오프셋이 되는 데이터 다음부터 N개 셈
LIMIT 4 OFFSET 3; -- LIMIT N OFFSET M;

SELECT
    Country,
    COUNT(*) AS '인원수'
    -- FirstName, LastName
FROM
    customers
GROUP BY
    Country;

SELECT
    Composer,
    -- AVG : Average
    AVG(Bytes) AS avgOfBytes
    -- 그룹핑한 이후 집계함수의 결과물은 ORDER BY도 사용 가능
FROM
    tracks
GROUP BY
    Composer
ORDER BY
    avgOfBytes DESC;

-- HAVING
SELECT
    Composer,
    AVG(Milliseconds / 60000) AS avgOfMinute
FROM
    tracks
-- WHERE
--     avgOfMinute < 10
-- FROM -> WHERE -> GROUP BY -> (HAVING) -> SELECT/집계함수
GROUP BY
    Composer
HAVING
    avgOfMinute < 10;