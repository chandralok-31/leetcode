# Write your MySQL query statement below
select p.product_id,ROUND(SUM(p.price*u.units)/SUM(u.units),2) as average_price 
from Prices p
inner join UnitsSold u
on p.product_id=u.product_id
where u.purchase_date between p.start_date and p.end_date
group by p.product_id;






# SELECT 
#     p.product_id,
#     ROUND(SUM(u.units * p.price)/SUM(u.units), 2) AS average_price
# FROM 
#     Prices p 
#     INNER JOIN UnitsSold u ON p.product_id = u.product_id
# WHERE
#     u.purchase_date >= p.start_date AND u.purchase_date <= p.end_date
# GROUP BY 
#     p.product_id;
    
    
    
#     SELECT a.product_id,ROUND(SUM(b.units*a.price)/SUM(b.units),2) as average_price
# FROM Prices as a
# JOIN UnitsSold as b
# ON a.product_id=b.product_id AND (b.purchase_date BETWEEN a.start_date AND a.end_date)
# GROUP BY product_id;