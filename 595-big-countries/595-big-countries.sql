# Write your MySQL query statement below
with cte as
(select name, population, area from world where area>=3000000 or population>=25000000)
select * from cte