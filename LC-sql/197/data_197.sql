create table
if not exists Weather ( id int
                      , recordDate date
                      , temperature int)
;

truncate table Weather
;

insert into Weather (id, recordDate, temperature)
values ('1', '2015-01-01', '10')
     , ('2', '2015-01-02', '25')
     , ('3', '2015-01-03', '20')
     , ('4', '2015-01-04', '30')
;

select *
  from Weather
;