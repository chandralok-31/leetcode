#Write your MySQL query statement below
select c.name as Customers
from Customers c
where id not in (select customerId from Orders);


# select c.name as Customers
# from Customers c
# where id not in (select c.Id from Customers c inner join Orders o on #c.id=o.customerId);

