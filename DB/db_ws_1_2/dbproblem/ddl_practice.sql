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
    Age
FROM
    user
ORDER BY
    FisrtName,
    Age DESC;