# Write your MySQL query statement below
select round(sum(i.tiv_2016),2) tiv_2016
from Insurance i
where i.tiv_2015 in (select i2.tiv_2015 from Insurance i2 where i2.pid<>i.pid)
and (i.lat,i.lon) not in (select i3.lat,i3.lon from Insurance i3 where i3.pid<>i.pid);