# Write your MySQL query statement below
select e.employee_id,e.name,count(e2.reports_to) as reports_count,
round(avg(e2.age),0) as average_age from Employees as e
inner join Employees as e2
on e.employee_id=e2.reports_to
where e2.reports_to is not null
group by e.employee_id,e2.reports_to
order by e.employee_id
