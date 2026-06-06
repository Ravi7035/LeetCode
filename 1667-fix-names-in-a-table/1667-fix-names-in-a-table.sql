select user_id,Concat((upper(left(name,1))),lower(substring(name,2))) as name
from Users order by user_id