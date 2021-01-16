create table staging_movie (
  movie_id serial primary key,
  title text,
  genres	text,
  release_date text,
  release_country	text,
  movie_rating varchar(20),
  review_rating numeric,
  movie_runtime	varchar(20),
  plot text,
  movie_cast text,
  movie_language text,
  filming_locations	text,
  budget varchar(100)
);
select max(length(title)) from staging_movie;

insert into genre (name)
select distinct regexp_split_to_table(genres, E'\\|') from staging_movie;

create table country (
  country_id serial primary key,
  name varchar(255)
);
insert into country (name)
(select distinct release_country from staging_movie);
select * from country;

create table genre(
  genre_id serial primary key,
  name varchar(255)
);

create table movie_genre(
  genre_id integer references genre(genre_id),
  movie_id integer references movie(movie_id)
);

create table person(
  person_id serial primary key,
  name varchar(255)
);

create table movie_director(
  person_id integer references person(person_id),
  movie_id integer references movie(movie_id)
);
create table movie_actor(
  person_id integer references person(person_id),
  movie_id integer references movie(movie_id)
);


create table movie_language(
  movie_language_id serial primary_key,
  name varchar(255)
);

create table movie_location(
  movie_location_id serial primary key,
  name varchar(255),
  country_id integer references country(country_id)
);


create table movie(
  movie_id serial primary key,
  title varchar(100),
  genre_id integer references genre(genre_id),
  release_date date,
  release_country integer references country(country_id),
  movie_rating varchar(20),
  review_rating numeric,
  movie_runtime smallint,
  plot text,
  movie_language_id integer references movie_language(movie_language_id),
  budget money
);