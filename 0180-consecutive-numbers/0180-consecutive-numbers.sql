WITH cte AS (
    SELECT
        num,
        LEAD(num, 1) OVER (ORDER BY id) AS num1,
        LEAD(num, 2) OVER (ORDER BY id) AS num2
    FROM logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM cte
WHERE num = num1
  AND num = num2;