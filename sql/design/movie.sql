--select distinct release_country from staging.movie;
select * from staging.movie;
-----------------------------------------------------
-- country
-----------------------------------------------------
-- 1. get num characters of largest country string
select max(char_length(release_country)) from staging.movie;

-- 2. create country table
create table country (
  country_id serial,
  name varchar(50) not null,
  primary key(country_id)
);

-- 3. populate country table using staging data
-- use subquery to do this:
-- INSERT INTO table_name ( column_name [, ...] )
--    query
--  see:
--  https://www.postgresql.org/docs/current/static/sql-insert.html
insert into country (name)
    (select distinct release_country from staging.movie);

-- 4. examine a few countries
select * from country limit 15;

-- 5. do number of countries match?
select
       (select count(*) from country) =
       (select count(distinct release_country) from staging.movie)
        as counts_match;

-----------------------------------------------------
-- filming_location
-----------------------------------------------------
-- 1. check out the filming locations from staging
select distinct filming_locations from staging.movie;

-- 2. create a filming_location table
create table filming_location (
  filming_location_id serial,
  name varchar(255) not null,
  -- immediately raise an error if an attempt to delete the referenced
  -- country is made
  country_id integer references country(country_id) on delete restrict not null,
  primary key(filming_location_id)
);

-- 3. try breaking up filming location:
-- use a subquery to split filming_locations into an array
-- ... display the entire array, its length, and the last element
select loc, array_length(loc, 1), loc[array_length(loc, 1)] from
  (select regexp_split_to_array(filming_locations, ',') as loc from staging.movie limit 10) as location;

-- 4. now that we know we can break it up, let's see if we can get the
-- the last part as the country, and everything before it as a "location"
select  array_to_string(loc[1:array_length(loc, 1)-1], ',') as loc_name,
    loc[array_length(loc, 1)] as country_name from
  (select regexp_split_to_array(filming_locations, ',') as loc from staging.movie) as loc;

-- 5. use a common table expression (CTE) / SELECT in WITH ... to save
-- the previous query as a one-time use "temporary table"
-- trim the values to remove white space surrounding string
with loc_temp as (
    select  trim(array_to_string(loc[1:array_length(loc, 1)-1], ',')) as loc_name,
            trim(loc[array_length(loc, 1)]) as country_name
    from
         (select regexp_split_to_array(filming_locations, ',') as loc
          from staging.movie) as loc
)
select distinct country_name, country.country_id, country.name
from loc_temp left join country on country.name = loc_temp.country_name
;

-- 6. fill in any additional countries that need to be added using cte
-- and left outer join (this will show us all locations that don't have
-- a corresponding country in the country table... we'll exclude places
-- that are not title case
with loc_temp as (
    select  trim(array_to_string(loc[1:array_length(loc, 1)-1], ',')) as loc_name,
            trim(loc[array_length(loc, 1)]) as country_name
    from
         (select regexp_split_to_array(filming_locations, ',') as loc
          from staging.movie) as loc
)
insert into country (name)
select distinct country_name
from loc_temp left outer join country on country.name = loc_temp.country_name
where country_id is null
and country_name is not null
and initcap(country_name) = country_name;

-- 7. finally insert locations
with loc_temp as (
    select  trim(array_to_string(loc[1:array_length(loc, 1)-1], ',')) as loc_name,
            trim(loc[array_length(loc, 1)]) as country_name
    from
         (select regexp_split_to_array(filming_locations, ',') as loc
          from staging.movie) as loc
)
insert into filming_location (name, country_id)
select distinct loc_name, country_id
from loc_temp inner join country on country.name = loc_temp.country_name;

-- 8. run checks to see results; we can see that there's a difference
-- in counts due to some locations not being added (spacing, last
-- element not title case, etc.)
select * from filming_location;
select count(*) from filming_location;
select count(distinct filming_locations) from staging.movie;

select filming_location.name, country.name
from filming_location
inner join country
    on country.country_id = filming_location.country_id;

-----------------------------------------------------
-- person (from actors)
-----------------------------------------------------
-- 1. create a person table
-- what's the longest possible name?
select max(char_length(movie_cast)) from  staging.movie;

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
select * from staging.movie;
select parse_name('Ray Lovelock');
select parse_name('Anna Maria Rizzoli');
select parse_name('Elias');


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
  from (select distinct regexp_split_to_table(movie_cast, E'\\|') as full_name from staging.movie) as person) as name_parts;
-- 3. run some checks; these two selects should be the same!
select count(*) from person;

select  regexp_split_to_table(movie_cast, E'\\|') from staging.movie;

select count(distinct full_name)
from (select regexp_split_to_table(movie_cast, E'\\|') as full_name from staging.movie) as actors;

-- want people from directors as well?

-- 4. make a function to get some directors!
-- how do we get director?
select plot from staging.movie;
select count(plot) from staging.movie;
select count(plot) from staging.movie where plot like 'Directed by';

-- looks like format is kind of like:Directed by name1, name2, nameN. With ...


-- a few attempts at writing a regex to do extract this...
-- with all bells and whistles... lazy + positive lookahead
select substring('Directed by Joe V,My Name is With Bar. With Baz Qux. A Test!', E'Directed by (.+?)(?=\\. With)');

-- we don't really need positive look ahead since we can just group
-- do we need lazy, though?
-- not in this case...
select substring('Directed by Joe V,My Name is With Bar. With Baz Qux. A Test!', E'Directed by (.+)\\. With');

-- but yes where multiple ". With" ...
select substring('Directed by Joe V. With some actors. With more!... A Test!', E'Directed by (.+)\\. With');

select substring('Directed by Joe V. With some actors. With more!... A Test!', E'Directed by (.+?)\\. With');
select substring('Directed by Joe V,My Name is With Bar. With Baz Qux. A Test!', E'Directed by (.+?)\\. With');


-- let's check if it works...
select movie_id, trim(director_name)
from (select movie_id, regexp_split_to_table(substring(plot, E'Directed by (.+?)\\. With'), ',') as director_name
      from staging.movie) as director_temp;

-- there's another problem, though... no ". With"
select substring('Directed by Joe V.', E'Directed by (.+?(?=\\. With))');
select substring('Directed by Joe V,My Name is With Bar. With Baz Qux. A Test!', E'Directed by (.+?(?=\\. With))');

-- and a potential fix
select substring('Directed by Joe V.', E'Directed by (.+?)\\.(?=( With|$))');
select substring('Directed by Joe V,My Name is With Bar. With Baz Qux. A Test!', E'Directed by (.+?)\\.(?=( With|$))');

-- ...or is it? maybe just farm this out into another sweep
select substring('Directed by Joe V. This is the rest of the plot.', E'Directed by (.+?)\\.(?=( With|$))');

-- let's go ahead and create the function with most simple regexp out of the bunch
create or replace function extract_director_names(
  s text
)
returns table(name text) as $$
begin
  -- return query select distinct regexp_split_to_table(substring(s, E'Directed by ([^With]*)\. With'), ',');
  -- return query select movie_id, regexp_split_to_table(substring(plot, E'Directed by (.+?(?=\. With))'), ',') from staging.movie;
  return query select trim(director_name)
  from (select distinct regexp_split_to_table(substring(s, E'Directed by (.+?)\\. With'), ',') as director_name
        from staging.movie) as director_temp;
end;
$$ language 'plpgsql';

select extract_director_names('Directed by Joe V,My Name is With Bar. With Baz Qux. A Test!');
select extract_director_names('Directed by Joe V.'); -- won't work for this, though!


-- 5. insert directors into people

-- let's see if we can get all the directors's names parsed
select parts[1], parts[2]
-- break up each name into parts
from (select parse_name(director_name) as parts
      -- regexp out and isolate each director name in plot
     from (select distinct extract_director_names(plot) as director_name from staging.movie)
           as director_names)
      as directors_name_parts;

--select director_name, max(length(director_name))
--from
--     (select distinct extract_director_names(plot) as director_name from staging.movie) as foo
--group by director_name;
--select * from staging.movie where plot ilike '%jerica%';

-- which directors already appear as actors?
select parts[1], parts[2]
from (select parse_name(director_name) as parts
     from (select distinct extract_director_names(plot) as director_name from staging.movie)
           as director_names)
      as directors_name_parts
inner join person on parts[1] = person.given and parts[2] = person.surname;

-- finally, insert or no action into person using on conflict to do nothing
insert into person (given, surname)
select parts[1] as given, parts[2] as surname
from (select parse_name(director_name) as parts
     from (select distinct extract_director_names(plot) as director_name from staging.movie)
           as director_names)
      as directors_name_parts
on conflict (given, surname) do nothing;

-----------------------------------------------------
-- genre
-----------------------------------------------------
-- 1. create genre table!
select max(char_length(genres)) from staging.movie;

create table genre (
  genre_id serial,
  name varchar(80),
  primary key(genre_id)
);
-- 2. insert genres
insert into genre (name)
    (select distinct regexp_split_to_table(genres, E'\\|') as genre from staging.movie);

select * from genre;

-----------------------------------------------------
-- language
-----------------------------------------------------
-- 1. create language table!
select max(char_length(language)) from staging.movie;

create table language (
  genre_id serial,
  name varchar(80) not null,
  primary key(genre_id)
);
-- 2. insert languages
insert into language (name)
    (select distinct regexp_split_to_table(language, E'\\|') as name from staging.movie);

select * from language;

-----------------------------------------------------
-- movie
-----------------------------------------------------
-- 1. create movie table
-- what's the max length of movie rating?
select max(char_length(movie_rating)) from staging.movie;

-- create it!
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

-- 2. bring in movies
insert into movie
    (movie_id, title, mpaa_rating, imdb_rating, plot, runtime, budget)
select
       movie_id,
       title as title,
       movie_rating as mpaa_rating,
       review_rating as imdb_rating,
       plot,
       -- use regexp to get rid of minutes (did not check for 1hr, etc.)
       substring(movie_run_time, E'\\d+')::smallint as runtime,
       case
         when budget like '$%' then cast(budget as money)
         else null
       end as budget
from staging.movie;

-- 3. check the worx
select * from movie;
select count(*) from movie;
select count(*) from staging.movie;

-----------------------------------------------------
-- movie_genre (associate movies and genres)
-----------------------------------------------------
-- 1. create the table that joins movies and genres
create table movie_genre (
  movie_id integer references movie(movie_id),
  genre_id integer references genre(genre_id)
);

-- 2. insert movie / genre pairs
-- can we get individual genres from the staging version of movie?
select movie_id, regexp_split_to_table(genres, E'\\|') as genre_name from staging.movie;

-- can we match those genres with a genre id?
select movie_genre.movie_id, genre_id
from
     (select movie_id, regexp_split_to_table(genres, E'\\|') as genre_name from staging.movie) as movie_genre
    -- match up genre by using genre name
    inner join genre
    on genre.name = genre_name;

-- ok, now let's try adding movie and genre pairs
-- take advantage of the fact that movie ids match...
insert into movie_genre (movie_id, genre_id)
select movie_genre.movie_id, genre_id
from
    -- get movie and its genres from original staging.movie first...
     (select movie_id, regexp_split_to_table(genres, E'\\|') as genre_name from staging.movie) as movie_genre
    -- match up genre by using genre name
    inner join genre
    on genre.name = genre_name;

-- did we get anything in the table?
select * from movie_genre;

-- 3. check our work...
-- can movie and genre be joined using movie_genre?
select * from movie_genre
inner join movie on movie.movie_id = movie_genre.movie_id
inner join genre on genre.genre_id = movie_genre.genre_id;

-- now, show only title and genres by grouping and using a string aggregate function
-- to stitch together all of the genres
select movie.title, string_agg(genre.name, ',') from movie_genre
inner join movie on movie.movie_id = movie_genre.movie_id
inner join genre on genre.genre_id = movie_genre.genre_id
group by movie.movie_id;

-----------------------------------------------------
-- associate movie with a country for release_country
-----------------------------------------------------
-- 1. translate release country to id by using update from syntax
update public.movie set release_country = country.country_id
from staging.movie
inner join country
    on country.name = staging.movie.release_country
    where public.movie.movie_id = staging.movie.movie_id;

-- 2. did it work?
select distinct release_country from movie;

-- where were most of the horror movies released?
select country.name, count(movie_id) as counts from movie
  inner join country
  on release_country = country.country_id
  group by country.name
  order by counts desc;

-----------------------------------------------------
-- movie_director
-----------------------------------------------------
-- 1. explore the data a little bit...
-- how many directors do we actually have (show all rows... or add a count)
select staging.movie.movie_id,
       extract_director_names(plot) as director_name
from staging.movie
order by director_name;

-- maybe let's narrow it down to movies with plot that contains Directed by
select extract_director_names(plot) as director_name
from staging.movie
where staging.movie.plot like 'Directed by%';

-- let's find one that has more than 1 director
select staging.movie.movie_id,
       extract_director_names(plot) as director_name
from staging.movie
where staging.movie.movie_id = 30
order by staging.movie.movie_id;

select * from movie where movie_id=1760;

select plot from staging.movie where staging.movie.movie_id = 30;

select plot from staging.movie where movie_id = 30;
select * from person where surname = 'Hulbert';
select * from person where given = 'Randy' and surname = 'Kent';

select director_name, count(movie_id)
from (select staging.movie.movie_id, extract_director_names(plot) as director_name
      from staging.movie) as director
group by director_name
having count(movie_id) > 1
order by count(movie_id) desc;

select director_name
from (select staging.movie.movie_id,
             extract_director_names(plot) as director_name
     from staging.movie) as director_temp
inner join person
on person.given || ' ' || person.surname = director_name;


-- why are we getting double movies....????
select * from
     (select plot, staging.movie.movie_id,
             extract_director_names(plot) as director_name
     from staging.movie) as temp
where director_name ilike '%roland sanchez%';


create table movie_director (
  movie_id integer references movie(movie_id) not null,
  person_id integer references person(person_id) not null
);

-- 2. insert directors
insert into movie_director (person_id, movie_id)
select person.person_id, movie_id
from
    -- get directors staging.movie first...
     (select staging.movie.movie_id,
             extract_director_names(plot) as director_name
     from staging.movie) as director_temp
-- match to person
inner join person
on person.given || ' ' || person.surname = director_name;

-- 3. check our work
select * from movie_director;

-- how's it look?
select movie.movie_id, title, string_agg(person.given || ' ' || person.surname, ',') as directors
from movie
inner join movie_director on movie_director.movie_id = movie.movie_id
inner join person on movie_director.person_id = person.person_id
group by movie.movie_id
order by movie.movie_id;

-- do we have any movies with no director?
select movie.movie_id, title
from movie
left join movie_director on movie_director.movie_id = movie.movie_id
where movie_director.movie_id is null
order by movie.movie_id;

select * from staging.movie where movie_id in (1, 10, 35, 44);


select person.person_id, movie_id, director_name, person.given, person.surname, person.person_id
from
     (select staging.movie.movie_id,
             extract_director_names(plot) as director_name
     from staging.movie) as director_temp
inner join person
on person.surname = director_name
where person.given = '';



insert into movie_director (person_id, movie_id)
select person.person_id, movie_id
from
     (select staging.movie.movie_id,
             extract_director_names(plot) as director_name
     from staging.movie) as director_temp
inner join person
on person.surname = director_name
where person.given = '';

-- there are about 24 now... which looks like it's just an issue with rows that don't include a with
select * from staging.movie where movie_id in (44, 57, 213);



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
select movie_id, regexp_split_to_table(movie_cast, E'\\|') as actor from staging.movie;

-- can we match those people with a person id?
select person.person_id, movie_id, actor
from
    -- get movie and its actors from original staging.movie first...
     (select staging.movie.movie_id,
            regexp_split_to_table(movie_cast, E'\\|') as actor
     from staging.movie) as actor_temp
    -- match up genre by using genre name
inner join person
on (case when person.given = '' then '' else person.given || ' ' end) || person.surname = actor;

-- select (case when (2 > 1) then 'a' else 'b' end);

-- ok, now let's try adding movie and actor pairs
-- take advantage of the fact that movie ids match...

insert into movie_actor (person_id, movie_id)
select person.person_id, movie_id
from
    -- get movie and its actors from original staging.movie first...
     (select staging.movie.movie_id,
            regexp_split_to_table(movie_cast, E'\\|') as actor
     from staging.movie) as actor_temp
    -- match up genre by using genre name
inner join person
on (case when person.given = '' then '' else person.given || ' ' end) || person.surname = actor;

-- 3. check our work...
select movie.title, string_agg(person.given || ' ' || person.surname, ',') from movie
inner join movie_actor on movie.movie_id = movie_actor.movie_id
inner join person on person.person_id = movie_actor.person_id
group by movie.movie_id;

-----------------
-- rando queries!
-----------------

select * from movie;

select title, string_agg(genre.name, ',') from movie
inner join movie_genre on movie.movie_id = movie_genre.movie_id
inner join genre on genre.genre_id = movie_genre.genre_id
group by movie.movie_id;





-- actors in movies that have to do with aliens!
select movie.title, string_agg(person.given || ' ' || person.surname, ',') from movie
inner join movie_actor on movie.movie_id = movie_actor.movie_id
inner join person on person.person_id = movie_actor.person_id
where title ilike '%alien%'
group by movie.movie_id;



-- show all movies, each with their year, director(s), actor(s) and genre(s)
-- (kind of like recreating original!)
select movie.title,
       substring(movie.title, E'\\((\\d{4})\\)') as year,
       string_agg(distinct (director.given || ' ' || director.surname), ' | ') as directors,
       string_agg(actor.given || ' ' || actor.surname, ' | ') as actors,
       string_agg(distinct genre.name, ' | ')
from movie
inner join movie_actor on movie.movie_id = movie_actor.movie_id
inner join person as actor on actor.person_id = movie_actor.person_id
inner join movie_director on movie.movie_id = movie_director.movie_id
inner join person as director on director.person_id = movie_director.person_id
inner join movie_genre on movie.movie_id = movie_genre.movie_id
inner join genre on genre.genre_id = movie_genre.genre_id
group by movie.movie_id
order by substring(movie.title, E'\\((\\d{4})\\)');

select * from movie_director
where person_id = (select person_id from person where surname = 'Aronofsky' and given = 'Darren');


--most prolific horror film director
select array_to_string(array[person.given, person.surname], ' '),
       person.person_id,
       count(movie.movie_id) as count_movies,
       avg(imdb_rating) as score
from movie_director
inner join person on person.person_id = movie_director.person_id
inner join movie on movie.movie_id = movie_director.movie_id
where movie.imdb_rating is not null
group by person.person_id
having count(movie.movie_id) > 4
order by score desc;
--order by count_movies desc;

select * from movie_director where person_id = 36373;

create view movie_with_info as
select movie.title,
       substring(movie.title, E'\\((\\d{4})\\)') as year,
       max(country.name) as release_country,
       max(mpaa_rating) as mpaa_rating,
       max(imdb_rating) as imdb_rating,
       max(runtime) as runtime,
       string_agg(distinct (director.given || ' ' || director.surname), ' | ') as directors,
       string_agg(actor.given || ' ' || actor.surname, ' | ') as actors,
       string_agg(distinct genre.name, ' | ')
from movie
inner join movie_actor on movie.movie_id = movie_actor.movie_id
inner join person as actor on actor.person_id = movie_actor.person_id
inner join movie_director on movie.movie_id = movie_director.movie_id
inner join person as director on director.person_id = movie_director.person_id
inner join movie_genre on movie.movie_id = movie_genre.movie_id
inner join genre on genre.genre_id = movie_genre.genre_id
inner join country on country.country_id = release_country
group by movie.movie_id
order by substring(movie.title, E'\\((\\d{4})\\)');

select * from movie_with_info where directors ilike '%jason impey%';
select * from staging.movie where plot ilike '%roland sanchez%'; --? director twice
select * from movie_with_info where directors ilike '%takashi miike%';

create index title_index on movie(title);
select * from staging.movie where title = 'Evil Dead (2013)';