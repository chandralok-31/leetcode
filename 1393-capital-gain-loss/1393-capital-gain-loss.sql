# Write your MySQL query statement below
with cte as(
select stock_name,
    case    
        when operation='Buy' then sum(price)*(-1)
        when operation='Sell' then sum(price)
        end as prices
from Stocks
group by stock_name,operation
order by stock_name)

select stock_name ,sum(prices) as capital_gain_loss
from cte
group by stock_name;
