CREATE TABLE user (
    FisrtName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Age INTEGER NOT NULL,
    Address VARCHAR(50) NOT NULL,
    PhoneNumber VARCHAR(50) NOT NULL,
    Salary INTEGER
);

DROP TABLE user;

SELECT * FROM user;

SELECT 
    FisrtName,
    Age,
    Salary
FROM
    user
ORDER BY
    Age,
    Salary DESC;