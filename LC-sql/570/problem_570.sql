/*
Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.
 

Example 1:

Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | None      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+
*/


select m.name
  from Employee as e
 inner join Employee as m
    on m.id = e.managerId
 group by e.managerId
having count(e.managerId) >= 5
;
