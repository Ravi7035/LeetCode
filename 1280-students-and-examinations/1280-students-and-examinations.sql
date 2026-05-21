# Write your MySQL query statement below
select st.student_id,st.student_name,s.subject_name,count(ex.subject_name) as attended_exams
from Students as st
cross join Subjects as s
left join Examinations  as ex
on st.student_id=ex.student_id
and s.subject_name = ex.subject_name
group by  st.student_id,st.student_name,s.subject_name
order by st.student_id,s.subject_name


