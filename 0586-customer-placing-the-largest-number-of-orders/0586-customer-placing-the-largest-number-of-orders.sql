# Write your MySQL query statement below
SELECT customer_number 
from Orders
group by customer_number
order by count(*) desc limit 1;



# select customer_number from orders
# group by customer_number
# order by count(*) desc limit 1;