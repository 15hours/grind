create table
if not exists Sales ( sale_id int
                    , product_id int
                    , year int
                    , quantity int
                    , price int)
;

create table
if not exists Product ( product_id int
                      , product_name varchar(10))
;

truncate table Sales
;

insert into Sales (sale_id, product_id, year, quantity, price)
values ('1', '100', '2008', '10', '5000')
     , ('2', '100', '2009', '12', '5000')
     , ('7', '200', '2011', '15', '9000')
;

truncate table Product
;

insert into Product (product_id, product_name)
values ('100', 'Nokia')
     , ('200', 'Apple')
     , ('300', 'Samsung')
;

select *
  from Sales
;

select *
  from Product
;