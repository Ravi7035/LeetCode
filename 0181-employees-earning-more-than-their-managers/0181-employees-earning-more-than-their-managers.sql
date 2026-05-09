# Write your MySQL query statement 
select e.name as Employee
from employee as  e
join employee as m
on e.managerId=m.id 
Where e.salary > m.salary
