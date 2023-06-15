# Write your MySQL query statement below
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans 
from Visits v 
LEFT JOIN Transactions t 
ON v.visit_id = t.visit_id  
WHERE t.amount IS NULL 
GROUP BY v.customer_id;

# Select customer_id, count(v.visit_id) as 'count_no_trans' 
# from Visits v 
# where v.visit_id not in (select t.visit_id from Transactions t)
# group by customer_id;