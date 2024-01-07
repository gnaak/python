CREATE TABLE user (
    FisrtName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Age INTEGER NOT NULL,
    Address VARCHAR(50) NOT NULL,
    PhoneNumber VARCHAR(50) NOT NULL,
    Salary INTEGER
);


SELECT 
    FisrtName,
    Address
FROM
    user
WHERE 
    FisrtName = '건우' AND
    Address = '경기도';

SELECT
    *
FROM
    user
WHERE
    Address NOT IN ('경기도','강원도')
    AND Age BETWEEN 20 AND 30
ORDER BY
    Age; 
