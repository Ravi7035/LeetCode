# Write your MySQL query statement below

SELECT pp.firstname,pp.lastname,ad.city,ad.state
From Person as PP
Left OUTER Join Address as ad
ON pp.personId=ad.personId