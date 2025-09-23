# Write your MySQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM employee e
LEFT JOIN department d on e.departmentId = d.id
WHERE e.salary = (
    select max(salary)
    from employee
    where departmentId = e.departmentId
)
