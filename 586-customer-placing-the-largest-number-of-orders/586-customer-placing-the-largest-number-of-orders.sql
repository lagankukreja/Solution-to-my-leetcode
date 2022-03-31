# select o1.customer_number from orders o1,orders o2 where 
select customer_number from orders group by customer_number order by count(order_number) desc limit 1