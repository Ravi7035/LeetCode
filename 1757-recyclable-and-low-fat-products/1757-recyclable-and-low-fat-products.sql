# Write your MySQL query statement below
select pp.product_id 
From Products as pp
where pp.low_fats="Y" and pp.recyclable="Y"