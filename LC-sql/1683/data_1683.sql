create table
if not exists Tweets ( tweet_id int
                     , content varchar(50))
;

truncate table Tweets
;

insert into Tweets (tweet_id, content)
values ('1', 'Vote for Biden')
     , ('2', 'Let us make America great again!')
;

select *
  from Tweets
;