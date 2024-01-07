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
    PhoneNumber,
    Address
FROM 
    user
WHERE
    PhoneNumber LIKE '%-51__-%'
    AND
    Address != '서울';
