create table
if not exists Students ( student_id int
                       , student_name varchar(20))
;

create table
if not exists Subjects ( subject_name varchar(20))
;

create table
if not exists Examinations ( student_id int
                           , subject_name varchar(20))
;

truncate table Students
;

insert into Students (student_id, student_name)
values ('1', 'Alice')
     , ('2', 'Bob')
     , ('13', 'John')
     , ('6', 'Alex')
;

truncate table Subjects
;

insert into Subjects (subject_name)
values ('Math')
     , ('Physics')
     , ('Programming')
;

truncate table Examinations
;

insert into Examinations (student_id, subject_name)
values ('1', 'Math')
     , ('1', 'Physics')
     , ('1', 'Programming')
     , ('2', 'Programming')
     , ('1', 'Physics')
     , ('1', 'Math')
     , ('13', 'Math')
     , ('13', 'Programming')
     , ('13', 'Physics')
     , ('2', 'Math')
     , ('1', 'Math')
;

select *
  from Students
;

select *
  from Subjects
;

select *
  from Examinations
;