with Hotels as (
select * from Hotel_2018
union
select * from Hotel_2019
union
select * from Hotel_2020)


select *
from hotels
left join Hotel_market_segment
on Hotels.market_segment = Hotel_market_segment.market_segment
left join Hotel_meal_cost
on hotels.meal = Hotel_meal_cost.meal
