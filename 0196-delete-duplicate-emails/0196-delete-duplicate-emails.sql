# Write your MySQL query statement below
delete e1 
from Person as e1
join Person as e2
on e1.email=e2.email
and e1.id > e2.id
