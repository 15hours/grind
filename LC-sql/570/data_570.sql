drop table
if exists Employee
;

create table
if not exists Employee ( id int
                       , name varchar(255)
                       , department varchar(255)
                       , managerId int)
;

truncate table Employee
;

insert into Employee (id, name, department, managerId)
values ('101', 'John', 'A', null)
     , ('102', 'Dan', 'A', '101')
     , ('103', 'James', 'A', '101')
     , ('104', 'Amy', 'A', '101')
     , ('105', 'Anne', 'A', '101')
     , ('106', 'Ron', 'B', '101')
;

select *
  from Employee
;