drop table if exists first_name;
create table first_name
(
    name varchar(50) primary key
);
copy first_name from  '/tmp/first-names.csv' csv;
select * from first_name;

drop table if exists last_name;
create table last_name
(
    name varchar(50) primary key
);
copy last_name from '/tmp/last-names.csv' csv;
select * from last_name;

drop table if exists company_name_part;
create table company_name_part
(
   grp smallint default 0,
   name varchar(50) primary key
);
copy company_name_part(name) from '/tmp/words.txt' csv;

select * from company_name_part;

select 0 as label,
       unnest(array['foo', 'bar', 'baz', 'qux', 'corge']) as syllable
create or replace function generate_domain() returns varchar as $$
declare
  tlds varchar[] := array['com', 'com', 'com','net','me','org', 'com','net','me','org','com','net','me','org', 'es', 'us', 'uk', 'ru', 'jp', 'cn', 'eu'];
  domain varchar;
begin
  with syllables as (
      select 0 as label,
             unnest(array['foo', 'bar', 'baz', 'qux', 'corge']) as syllable
      )
  select string_agg(syllable, '') into domain
  from
      (select * from syllables order by random() limit (1 + floor(random() * 4)::int)) as foo
  group by label;
  return domain || '.' || tlds[1 + floor(random() * array_length(tlds, 1))];
end;
$$
language plpgsql;

select generate_domain();

create or replace function generate_domain() returns varchar as $$
declare
    tlds varchar[] := array['com', 'com', 'com','net','me','org', 'com','net','me','org','com','net','me','org', 'es', 'us', 'uk', 'ru', 'jp', 'cn', 'eu'];
    domain varchar;
begin
    select string_agg(name, '') from
        (select name from company_name_part
         order by random()
         limit (1 + floor(random() * 4):: int)) name_temp
    into domain;
    return domain || '.' || tlds[1 + floor(random() * array_length(tlds, 1))];
end
$$
language plpgsql;

select generate_domain()

create or replace function generate_name() returns varchar[] as $$
declare
    first varchar;
    last varchar;
begin
    select name from first_name order by random() limit 1 into first;
    select name from last_name order by random() limit 1 into last;
    return array[first, last];
end;
$$
language plpgsql;
select generate_name()


drop table if exists web_user;
create table web_user (
  user_id integer primary key,
  first varchar(255) not null,
  last varchar(255) not null,
  active boolean not null default FALSE,
  email varchar(255) not null,
  password varchar(255) not null
);
drop table if exists session;
create table session (
  session_number integer,
  session_id varchar(255) primary key,
  user_id integer references web_user(user_id) on delete cascade
);

select generate_series(1, 100) as user_id, generate_name() as name;

insert into web_user
select user_id,
       name[1] as first,
       name[2] as last,
       case when random() > 0.5 then TRUE else FALSE end as active,
       substring(name[1], '^.') || name[2] || '@' || generate_domain() as email,
       md5(random()::text) as password
from
     (select generate_series(1, 250000) as user_id, generate_name() as name) as name_temp;


select * from web_user limit 2;



insert into session (session_number, session_id, user_id)
  (select generate_series(1, 2000000), 
          md5(random()::text), 
		  1 + floor(random() * 250000))
on conflict do nothing;


select * from web_user where first = 'Ivy'
explain
explain analyze select * from web_user where first = 'tegan';
