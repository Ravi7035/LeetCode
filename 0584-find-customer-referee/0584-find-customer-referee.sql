# Write your MySQL query statement below
SELECT cus.name
FROM Customer as cus
where cus.referee_id != 2 or cus.referee_id is NULL