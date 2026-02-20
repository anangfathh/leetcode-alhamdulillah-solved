# Write your MySQL query statement below
SELECT T.id 
FROM Weather T
CROSS JOIN Weather Y
WHERE DATEDIFF(T.recordDate, Y.recordDate) = 1 AND T.temperature > Y.temperature 
