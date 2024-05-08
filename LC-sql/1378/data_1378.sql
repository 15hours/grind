create table
if not exists Employees ( id int
                        , name varchar(20))
;

create table
if not exists EmployeeUNI ( id int
                          , unique_id int)
;

truncate table Employees
;

insert into Employees (id, name)
values ('1', 'Alice')
     , ('7', 'Bob')
     , ('11', 'Meir')
     , ('90', 'Winston')
     , ('3', 'Jonathan')
;

truncate table EmployeeUNI
;

insert into EmployeeUNI (id, unique_id)
values ('3', '1')
     , ('11', '2')
     , ('90', '3')
;

select *
  from Employees
;

select *
  from EmployeeUNI
;