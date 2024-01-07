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
    LastName,
    Age,
    Address,
    PhoneNumber,
    Salary
FROM 
    user
ORDER BY
    Age
LIMIT
    40, 20;
