create table 
if not exists Products ( product_id as INT
                       , low_fats   as ENUM('Y', 'N')
                       , recyclable as ENUM('Y', 'N'))
;

truncate table Products
;

insert into Products (product_id, low_fats, recyclable)
values ('0', 'Y', 'N')
     , ('1', 'Y', 'Y')
     , ('2', 'N', 'Y')
     , ('3', 'Y', 'Y')
     , ('4', 'N', 'N')
;

select * 
  from Products
;
