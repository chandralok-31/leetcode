# Write your MySQL query statement below
with cte as 
(select num,lead(num,1) over() as next1,
lead(num,2) over() as next2
from logs)

select distinct num as ConsecutiveNums from
cte where num=next1 and num=next2;
