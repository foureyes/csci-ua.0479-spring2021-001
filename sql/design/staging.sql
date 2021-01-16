create schema staging;

create table staging.movie (
  movie_id serial,
	title text,
	genres text,
	release_date text,
	release_country	varchar(100),
	movie_rating varchar(100),
	review_rating numeric,
	movie_run_time varchar(10),
	plot text,
	movie_cast text,
	language varchar(100),
	filming_locations text,
	budget varchar(100),
  primary key(movie_id)
);


