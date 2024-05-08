create table if Not exists Customer ( id int
                                    , name varchar(25)
                                    , referee_id int)
;

truncate table Customer
;

insert into Customer (id, name, referee_id)
values ('1', 'Will', 'None')
     , ('2', 'Jane', 'None')
     , ('3', 'Alex', '2')
     , ('4', 'Bill', 'None')
     , ('5', 'Zack', '1')
     , ('6', 'Mark', '2')
;

select *
  from Customer
;