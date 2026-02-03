/* Write your T-SQL query statement below */
SELECT E1.[name] AS Employee
FROM Employee E1, Employee E2
WHERE E1.salary > E2.salary AND E1.[managerID] = E2.[id]