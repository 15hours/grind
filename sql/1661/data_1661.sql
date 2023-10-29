create table
if not exists Activity ( machine_id int
                       , process_id int
                       , activity_type ENUM('start', 'end')
                       , timestamp float)
;

truncate table Activity
;

insert into Activity (machine_id, process_id, activity_type, timestamp)
values ('0', '0', 'start', '0.712')
     , ('0', '0', 'end', '1.52')
     , ('0', '1', 'start', '3.14')
     , ('0', '1', 'end', '4.12')
     , ('1', '0', 'start', '0.55')
     , ('1', '0', 'end', '1.55')
     , ('1', '1', 'start', '0.43')
     , ('1', '1', 'end', '1.42')
     , ('2', '0', 'start', '4.1')
     , ('2', '0', 'end', '4.512')
     , ('2', '1', 'start', '2.5')
     , ('2', '1', 'end', '5')
;

select *
  from Activity
;