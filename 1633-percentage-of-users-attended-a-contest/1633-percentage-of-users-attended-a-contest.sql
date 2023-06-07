# Write your MySQL query statement below
SELECT r.contest_id,ROUND(count(r.user_id)*100/(SELECT COUNT(*) FROM Users),2) AS percentage
FROM Users u
RIGHT JOIN Register r
ON u.user_id=r.user_id
GROUP BY r.contest_id
ORDER BY percentage desc,r.contest_id;





# SELECT contest_id
#     , ROUND(COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(*) FROM Users), 2) AS percentage
# FROM Register 
# GROUP BY contest_id
#     ORDER BY percentage DESC, contest_id