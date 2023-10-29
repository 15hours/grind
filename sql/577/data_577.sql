create table
if not exists Employee ( empId int
                     , name varchar(255)
                     , supervisor int
                     , salary int)
;

create table
if not exists Bonus ( empId int
                  , bonus int)
;

truncate table Employee
;

insert into Employee (empId, name, supervisor, salary)
values ('3', 'Brad', null, '4000')
     , ('1', 'John', '3', '1000')
     , ('2', 'Dan', '3', '2000')
     , ('4', 'Thomas', '3', '4000')
;

truncate table Bonus
;

insert into Bonus (empId, bonus)
values ('2', '500')
     , ('4', '2000')
;

select *
  from Employee
;

select *
  from Bonus
;