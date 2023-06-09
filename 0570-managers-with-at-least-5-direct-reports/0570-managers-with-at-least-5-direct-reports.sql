# Write your MySQL query statement below
# select name from Employee where id in
# (select managerId from Employee group by managerId having count(*)>=5);


SELECT e1.name
FROM Employee e1
INNER JOIN Employee e2
ON e1.id = e2.managerId
GROUP BY e1.name
HAVING COUNT(e1.name) >= 5;