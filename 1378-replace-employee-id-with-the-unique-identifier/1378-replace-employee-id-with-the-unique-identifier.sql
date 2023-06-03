# Write your MySQL query statement below
select EN.unique_id,E.name 
from Employees as E
left join EmployeeUNI as EN
on E.id=EN.id;