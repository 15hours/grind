create table
if not exists Visits( visit_id int
                    , customer_id int)
;

create table
if not exists Transactions( transaction_id int
                          , visit_id int
                          , amount int)
;

truncate table Visits
;

insert into Visits (visit_id, customer_id)
values ('1', '23')
     , ('2', '9')
     , ('4', '30')
     , ('5', '54')
     , ('6', '96')
     , ('7', '54')
     , ('8', '54')
;

truncate table Transactions
;

insert into Transactions (transaction_id, visit_id, amount)
values ('2', '5', '310')
     , ('3', '5', '300')
     , ('9', '5', '200')
     , ('12', '1', '910')
     , ('13', '2', '970')
;

select *
  from Visits
;

select *
  from Transactions
;