# Write your MySQL query statement below
with cte as(
select *, sum(weight) over(order by turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as total
    from Queue
)

select person_name from cte where total<=1000
order by total desc limit 1;