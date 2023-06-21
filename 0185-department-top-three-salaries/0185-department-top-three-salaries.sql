# Write your MySQL query statement below



WITH cte AS(
    SELECT e.name AS Employee, e.salary AS Salary, d.name AS Department , 
        DENSE_RANK() OVER (PARTITION BY d.name ORDER BY salary DESC) AS RANKK
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
)
SELECT Department, Employee, Salary
FROM cte
WHERE RANKK <= 3