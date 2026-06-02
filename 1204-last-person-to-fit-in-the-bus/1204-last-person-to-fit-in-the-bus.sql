# Write your MySQL query statement below
with running as (
    select turn,person_name,sum(weight) over (order by turn) as Total_Weight
    from Queue
)
select person_name 
from running
where Total_Weight <=1000
order by turn desc
limit 1