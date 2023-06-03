# Write your MySQL query statement below
select EN.unique_id,E.name 
from EmployeeUNI as EN 
right join Employees as E
on E.id=EN.id;