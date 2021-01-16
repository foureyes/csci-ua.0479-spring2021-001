create table country (
  country_id serial,
  name varchar(50) not null,
  primary key(country_id)
);

create table filming_location (
  filming_location_id serial,
  name varchar(255),
  country_id integer references country(country_id) on delete restrict not null,
  primary key(filming_location_id)
);

create table person (
  person_id serial,
  given varchar(255),
  surname varchar(255),
  unique (given, surname),
  primary key(person_id)
);

create table genre (
  genre_id serial,
  name varchar(80),
  primary key(genre_id)
);

create table language (
  genre_id serial,
  name varchar(80) not null,
  primary key(genre_id)
);

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

create table movie_genre (
  movie_id integer references movie(movie_id) not null,
  genre_id integer references genre(genre_id) not null
);

create table movie_director (
  movie_id integer references movie(movie_id) not null,
  person_id integer references person(person_id) not null
);

create table movie_actor (
  movie_id integer references movie(movie_id) not null,
  person_id integer references person(person_id) not null
);



insert into country (name)
    (select distinct release_country from staging.movie);

select * from country;

select regexp_split_to_array(filming_locations, ',') as locations from staging.movie;


select trim(location)
from (select regexp_split_to_table(filming_locations, ',') as location from staging.movie) as temp;


select  array_to_string(loc[1:array_length(loc, 1)-1], ',') as loc_name,
    loc[array_length(loc, 1)] as country_name from
  (select regexp_split_to_array(filming_locations, ',') as loc from staging.movie) as loc;

with loc_temp as (
    select  trim(array_to_string(loc[1:array_length(loc, 1)-1], ',')) as loc_name,
            trim(loc[array_length(loc, 1)]) as country_name
    from
         (select regexp_split_to_array(filming_locations, ',') as loc
          from staging.movie) as loc
)
select distinct country_name, country.country_id, country.name
from loc_temp left join country on country.name = loc_temp.country_name;

with loc_temp as (
    select  trim(array_to_string(loc[1:array_length(loc, 1)-1], ',')) as loc_name,
            trim(loc[array_length(loc, 1)]) as country_name
    from
         (select regexp_split_to_array(filming_locations, ',') as loc
          from staging.movie) as loc
)
insert into filming_location (name, country_id)
select distinct loc_name, country.country_id
from loc_temp left join country on country.name = loc_temp.country_name
where country.country_id is not null;

select filming_location.name, country.name
from filming_location
       inner join country on filming_location.country_id = country.country_id;






















