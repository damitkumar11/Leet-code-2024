# Write your MySQL query statement below
# Write your MySQL query statement below
Select name,bonus
From employee e left join bonus b
on e.empid = b.empid
where ifnull(bonus,0) < 1000;