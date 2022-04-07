# Write your MySQL query statement below
with 
cte as(
select candidateId from vote group by candidateId order by count(id) desc limit 1
)
select name from candidate where id in (select * from cte)  ;