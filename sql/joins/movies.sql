CREATE TABLE genre (
	genre_id integer,
	name varchar(20),
	description text,
	PRIMARY KEY (genre_id)
);

CREATE TABLE movie (
	movie_id serial,
	title varchar(50) NOT NULL,
	year smallint NOT NULL,
	runtime smallint NOT NULL, 
	genre_id integer REFERENCES genre (genre_id),
	PRIMARY KEY (movie_id)
);

INSERT INTO genre 
	VALUES
		(1, 'Comedy', 'LOL'),
		(2, 'Drama', 'Such feels.'),
		(3, 'Fantasy', 'Swords. And maybe fairies too.'),
		(4, 'Horror', 'Ghosts, goblins, and other spooky things.'),
		(5, 'Science Fiction', 'Robots and stuff.'),
		(6, 'Super Hero', 'Mostly capes.'),
		(7, 'Thriller', 'Close. Your. Eyes.');

INSERT INTO movie (title, year, runtime, genre_id)
	VALUES
		('Alphaville', 1965, 99, null),
		('La Montaña Sagrada (The Holy Mountain)', 1973, 99, null),
		('Dune', 1984, 136, 5),
		('Point Break',  1991, 122, 7),
		('Strange Days', 1995, 145, 5),
		('2046', 2004, 122, 2),
		('Hellboy', 2004, 122, 6),
		('Los Abrazos Rotos (Broken Embraces)', 2009, 128, 7),
		('Blade Runner 2049', 2017, 163, 5),
		('Wonder Woman', 2017, 141, 6),
		('Shape of Water', 2018, 123, 3);

	
