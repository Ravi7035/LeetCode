# Write your MySQL query statement below
select session_id,user_id,Timestampdiff(Minute,min(event_timestamp),max(event_timestamp)) as session_duration_minutes,sum(event_type="scroll") as scroll_count
from app_events

group by session_id

having Timestampdiff(Minute,min(event_timestamp),max(event_timestamp)) > 30 and sum(event_type="scroll") >=5 and  sum(event_type="click") / sum(event_type="scroll") < 0.2 and sum(event_type="purchase") = 0

order by scroll_count desc, session_id asc
