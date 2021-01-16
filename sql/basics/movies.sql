--CREATE TABLE IF NOT EXISTS movie
--CREATE OR REPLACE TABLE
CREATE TABLE movie (
	id serial PRIMARY KEY,
	title varchar(50),
	director varchar(100),
	year timestamptz,
	runtime integer,
	genre varchar(255),
	budget money,
	gross money
);

INSERT INTO movie (title, director, year, runtime, genre, budget, gross)
	VALUES
		('Blue Velvet', 'David Lynch', '1986-01-01', 120, 'Neo Noir Mystery Thriller', 6000000, 8600000),
		('Dune', 'David Lynch', '1984-01-01', 136, 'Science Fiction', 40000000, 30900000),
		('Strange Days', 'Kathryn Bigelow', '1995-01-01', 145, 'Science Fiction', 42000000, 8000000),
		('Point Break', 'Kathryn Bigelow', '1991-01-01', 122, 'Crime Thriller', 24000000, 83500000),
		('Zero Dark Thirty', 'Kathryn Bigelow', '2012-01-01', 157, 'Political Thriller', 40000000, 132800000),
		('Blade Runner', 'Ridley Scott', '1982-01-01', 117, 'Sci-Fi', 28000000, 33800000),
		('Blade Runner 2049', 'Denis Villeneuve', '2017-01-01', 163, 'Science Fiction', 185000000, 259200000),
		('Alien', 'Ridley Scott', '1979-01-01', 117, 'Sci-Fi', 11000000, 203600000),
		('Alien Covenant', 'Ridley Scott', '1982-01-01', 122, 'Science Fiction', 111000000, 240900000),
		('2046', 'Wong Kar-wai', '1982-01-01', 122, 'Drama', 12000000, 19500000),
		('Wonder Woman', 'Patty Jenkins', '2017-01-01', 141, 'Super Hero', 150000000, 821000000),
		('La Piel Que Habito (The Skin I Live In)', 'Pedro Almodóvar', '2011-01-01', 120, 'Horror', 13500000, 30800000),
		('Los Abrazos Rotos (Broken Embraces)', 'Pedro Almodóvar', '2009-01-01', 128, 'Romantic Thriller', 18000000, 31000000),
		('El Laberinto del Fauno (Pan''s Labyrinth)', 'Guillermo del Toro', '2006-01-01', 119, 'Dark Fantasy Horror', 19000000, 83300000),
		('Shape of Water', 'Guillermo del Toro', '2017-01-01', 123, 'Romantic Dark Fantasy Drama', 20000000, 195200000),
		('Pacific Rim', 'Guillermo del Toro', '2013-01-01', 132, 'Sci-Fi', 200000000, 411000000),
		('Hellboy', 'Guillermo del Toro', '2004-01-01', 122, 'Super Hero', 66000000, 99300000);

	

-- TRY THE FOLLOWING!
---------------------
-- import this file (a file containing sql statements)
-- list all tables
-- describe the movie table
-- show all movies
-- only show the name of the movie, who directed it, and how much money it made!
-- order rows by gross ascending
-- order rows by gross descending
-- try ordering by director ascending
-- use both director and gross to order rows
-- query all movies again...
-- now only genres, but without duplicates
-- only show rows that have a genre of Science Fiction
-- only show rows that have a genre that's not Science Fiction
-- only show rows that have a genre has thriller in it (ignore case)
-- use and to put together two condition (thrillers by Katheryn Bigelow)
-- show budget and gross
-- calculate return on investment (gross minus budget over budget; include expression in list of columns)
-- that's a mess of a column name; give it an alias, roi
-- now let's show the movies sorted based on roi
-- that's a lot of numbers after the decimal point... let's get it to just 2 places
-- using round ... btw, pg_typeof returns type of column
-- an example of casting to numeric... convert roi to numeric type!
-- try to find movies with negative roi ... wat!?
-- add an roi column to movie so we can permanently have that field: alter table [table_name] add column [column_name] [type]
-- select some movies to see the new column!  currently, new column has null values (blank in psql)
-- update all rows so that roi is set to a value based on other columns: update [table_name] set [assignment] where [cond]
-- fix duplicate genre
-- see... now Sci-Fi is folded into Science Fiction
-- group all rows that have same genre and count them
-- use having to filter groups
