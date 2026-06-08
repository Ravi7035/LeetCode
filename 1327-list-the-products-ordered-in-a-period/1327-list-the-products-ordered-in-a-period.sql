# Write your MySQL query statement below
select p.product_name,sum(unit) as unit
from Products as p join Orders as o
on p.product_id=o.product_id
where order_date like "%2020-02%"
group by p.product_id
having sum(unit) >=100



