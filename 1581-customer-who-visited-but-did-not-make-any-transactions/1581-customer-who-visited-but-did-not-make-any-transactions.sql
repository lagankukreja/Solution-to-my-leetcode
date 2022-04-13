# Write your MySQL query statement below

with cte as (

select visit_id  from Transactions
group by visit_id)

select customer_id , count(customer_id) as count_no_trans 
from Visits
where visit_id not in 
(select * from cte)
group by customer_id 