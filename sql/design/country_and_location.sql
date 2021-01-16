drop table if exists staging_movie;
create table staging_movie (
  movie_id serial primary key,
  title text,
  genres text,
  release_date text,
  release_country text,
  movie_rating varchar(20),
  review_rating numeric,
  movie_runtime	varchar(20),
  plot text,
  movie_cast text,
  movie_language text,
  filming_locations	text,
  budget varchar(100)
);

-- copy everything, but leave out primary key from column list
-- so that pk is auto generated
copy staging_movie (title, genres, release_date, release_country, movie_rating, review_rating, movie_runtime, plot, movie_cast, movie_language, filming_locations, budget)
from '/tmp/class18/practice/IMDB Horror movies.csv'
header csv;

-- take a look at what we have
select * from staging_movie limit 10;


-----------------------------------------------------
-- country
-----------------------------------------------------
-- 1. if we make a name column in our new table, how big should
--    the varchar be?
select max(char_length(release_country)) from staging_movie;


-- 2. create country table
create table country (
   country_id serial,
   name varchar(50) not null,
   primary key(country_id)
);

-- 3. what are the possible country values?
select distinct release_country from staging_movie;


-- 4. populate country table using staging data
-- use subquery to do this:
-- INSERT INTO table_name ( column_name [, ...] )
--    query
--  see:
--  https://www.postgresql.org/docs/current/static/sql-insert.html
-- subquery returns table! value from table inserted...
insert into country (name)
    (select distinct release_country from staging_movie);
-- subquery can result in:
-- 1. multiple rows (like another table)
-- 2. a scalar value (a single value)

-- 5. let's check our results... do we have any countries?
select * from country limit 15;

-- 6. do number of countries match?
--    subqueries return single value

-- individual queries first
select count(*) from country;
select count(distinct release_country) from staging_movie;

-- how about both side-by-side?
select
       (select count(*) from country) as count_country,
       (select count(distinct release_country) from staging_movie) as count_staging;

-- these are just single values, so we can actually compare!
select
        (select count(*) from country) =
        (select count(distinct release_country) from staging_movie)
        as counts_match;

-- all together
select
    (select count(*) from country) as count_country,
    (select count(distinct release_country) from staging_movie) as count_staging,
    (select count(*) from country) =
    (select count(distinct release_country) from staging_movie)
        as counts_match;

-----------------------------------------------------
-- filming_location
-----------------------------------------------------
-- 1. check out the filming locations from staging
select distinct filming_locations from staging_movie;


-- 2. create a filming_location table
drop table if exists filming_location;
create table filming_location (
  filming_location_id serial,
  name varchar(255) not null,
  country_id integer references country(country_id),
  primary key(filming_location_id)
);
  -- immediately raise an error if an attempt to delete the referenced
  -- country is made
  -- country_id integer references country(country_id) on delete restrict not null,

-- 3. try breaking up filming location:
-- use a subquery to split filming_locations into an array
-- note that subquery in from must have alias
-- ... display the entire array, its length, and the last element

-- breaking into an Array
select string_to_array(filming_locations, ',') as loc from staging_movie limit 10;

-- use result as table and query into it! ... get some info about arrays
select loc, array_length(loc, 1), loc[array_length(loc, 1)]
    from (select string_to_array(filming_locations, ',') as loc from staging_movie limit 10) location;

-- do we mostly have countries?
select  distinct(loc[array_length(loc, 1)])
from (select string_to_array(filming_locations, ',') as loc from staging_movie) location;

--  uh... whitespace?
select  distinct(trim(loc[array_length(loc, 1)]))
from (select string_to_array(filming_locations, ',') as loc from staging_movie) location;

-- it WORKS!

-- 4. now that we know we can break it up, let's see if we can get the
-- the last part as the country, and everything before it as a "location"

select array_to_string(loc[1:array_length(loc, 1) - 1], ',') as loc_name,
       trim(loc[array_length(loc, 1)]) as country_name
from
    (select string_to_array(filming_locations, ',') as loc from staging_movie) as location;

-- 5. let's see if we have any country matches with our country
-- table; use a common table expression (CTE) / SELECT in WITH ... to save
-- the previous query as a one-time use "temporary table"
-- trim the values to remove white space surrounding string
-- cte can be self referencing, subqueries cannot ... let's try one out
-- perf should be the same
with loc_temp as (
    select array_to_string(loc[1:array_length(loc, 1) - 1], ',') as loc_name,
           trim(loc[array_length(loc, 1)]) as country_name
    from
        (select string_to_array(filming_locations, ',') as loc from staging_movie) as location
)
select distinct country_name, country.country_id, country.name
from loc_temp left join country on country.name = loc_temp.country_name;

-- 6. fill in any additional countries that need to be added using cte
-- and left outer join (this will show us all locations that don't have
-- a corresponding country in the country table... we'll exclude places
-- that are not title case
with loc_temp as (
    select  trim(array_to_string(loc[1:array_length(loc, 1)-1], ',')) as loc_name,
            trim(loc[array_length(loc, 1)]) as country_name
    from
         (select regexp_split_to_array(filming_locations, ',') as loc
          from staging_movie) as loc
)
insert into country (name)
select distinct country_name
from loc_temp left outer join country on country.name = loc_temp.country_name
where country_id is null
and country_name is not null
and initcap(country_name) <> country_name;

-- 7. finally insert locations
with loc_temp as (
    select  trim(array_to_string(loc[1:array_length(loc, 1)-1], ',')) as loc_name,
            trim(loc[array_length(loc, 1)]) as country_name
    from
         (select regexp_split_to_array(filming_locations, ',') as loc
          from staging_movie) as loc
)
insert into filming_location (name, country_id)
select distinct loc_name, country_id
from loc_temp inner join country on country.name = loc_temp.country_name;

-- 8. run checks to see results; we can see that there's a difference
-- in counts due to some locations not being added (spacing, last
-- element not title case, etc.)
select * from filming_location;
select count(*) from filming_location;
select count(distinct filming_locations) from staging_movie;

select filming_location.name, country.name
from filming_location
inner join country
    on country.country_id = filming_location.country_id;



-----------------------------------------------------
-- person (from actors)
-----------------------------------------------------
-- 1. create a person table
-- what's the longest possible name?
select max(char_length(movie_cast)) from  staging_movie;

create table person (
  person_id serial,
  given varchar(255),
  surname varchar(255),
  unique (given, surname),
  primary key(person_id)
);
--drop function parse_name(varchar);

-- 2. create a parse name function...
create or replace function parse_name(
    s varchar
  )
  returns varchar[] as $$
declare
  result varchar[];
begin
  select
         array[trim(array_to_string(parts[1:array_length(parts, 1) - 1], ' '))::varchar,
         trim(parts[array_length(parts, 1)])::varchar]
  into result
  from (select string_to_array(s, ' ') as parts) as name_parts;
  return result;
end;
$$ language 'plpgsql';
select * from staging_movie;
select parse_name('Ray Lovelock');
select parse_name('Anna Maria Rizzoli');


-- 3. insert into person table ...
insert into person (given, surname)
select parts[1] as given, parts[2] as surname
-- split actor name into last name (part after comma) and given name
from (select parse_name(full_name) as parts
  -- split cast field into individual actors' names
  -- note that we're assuming that actors with the same name are the same person
  -- the data set does not offer anyway of differentiating between people with the
  -- same name, sooo for the sake of having a separate person table, we'll assume
  -- (this is a bad assumption, of course), that actors with the same name are the
  -- same person
  from (select distinct regexp_split_to_table(movie_cast, E'\\|') as full_name from staging_movie) as person) as name_parts;
-- 3. run some checks; these two selects should be the same!
select count(*) from person;

select * from person


create table movie (
  movie_id serial,
  title text,
  release_date date,
  release_country integer references country(country_id),
  mpaa_rating varchar(20),
  imdb_rating numeric,
  runtime smallint,
  plot text,
  language varchar(255),
  budget money,
  primary key (movie_id)
);

insert into movie
(movie_id, title, mpaa_rating, imdb_rating, plot, runtime, budget)
select
    movie_id,
    title as title,
    movie_rating as mpaa_rating,
    review_rating as imdb_rating,
    plot,
    -- use regexp to get rid of minutes (did not check for 1hr, etc.)
    substring(staging_movie.movie_runtime, E'\\d+')::smallint as runtime,
    case
        when budget like '$%' then cast(budget as money)
        else null
        end as budget
from staging_movie;


-----------------------------------------------------
-- movie_actor
-----------------------------------------------------
-- 1. create the table
create table movie_actor (
  movie_id integer references movie(movie_id) not null,
  person_id integer references person(person_id) not null
);

-- 2. insert movie / actor pairs
-- can we get individual actors from the staging version of movie?
select movie_id, regexp_split_to_table(movie_cast, E'\\|') as actor from staging_movie;

-- can we match those people with a person id?
select person.person_id, movie_id, actor
from
    -- get movie and its actors from original staging.movie first...
     (select staging_movie.movie_id,
            regexp_split_to_table(movie_cast, E'\\|') as actor
     from staging_movie) as actor_temp
inner join person
on (case when person.given = '' then '' else person.given || ' ' end) || person.surname = actor;

-- select (case when (2 > 1) then 'a' else 'b' end);

-- ok, now let's try adding movie and actor pairs
-- take advantage of the fact that movie ids match...

insert into movie_actor (person_id, movie_id)
select person.person_id, movie_id
from
    -- get movie and its actors from original staging.movie first...
     (select staging_movie.movie_id,
            regexp_split_to_table(movie_cast, E'\\|') as actor
     from staging_movie) as actor_temp
    -- match up genre by using genre name
inner join person
on (case when person.given = '' then '' else person.given || ' ' end) || person.surname = actor;

-- 3. check our work...
select movie.title, string_agg(person.given || ' ' || person.surname, ',') from movie
inner join movie_actor on movie.movie_id = movie_actor.movie_id
inner join person on person.person_id = movie_actor.person_id
group by movie.movie_id;

