



select customer_number
from (
select customer_number, rank() over (order by count(1) desc) rank_val
from orders
group by customer_number
) a where rank_val = 1

#normal query
#nested query
#window function
#joins