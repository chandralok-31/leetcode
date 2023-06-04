# Write your MySQL query statement below
# select v.customer_id,count(v.customer_id) as count_no_trans
# from Visits as v
# inner join Transactions as t
# on v.visit_id=t.visit_id
# where t.amount=0
# group by v.customer_id;


SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans 
from Visits v 
LEFT JOIN Transactions t 
ON v.visit_id = t.visit_id  
WHERE t.amount IS NULL 
GROUP BY v.customer_id;