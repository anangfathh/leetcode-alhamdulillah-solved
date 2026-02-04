# Write your MySQL query statement below
SELECT C.name AS Customers
FROM Customers C
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders O
    WHERE O.customerId = C.id
)