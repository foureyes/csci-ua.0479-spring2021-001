DROP TABLE IF EXISTS song;
CREATE TABLE song (
	id serial PRIMARY KEY,
	title varchar(100),
	artist varchar(100),
	dancability numeric
);

INSERT INTO song (title, artist, dancability)
	VALUES
		('Heartbeats', 'Jose Gonzalez', 0.01),
		('Heartbeats', 'The Knife', 0.9),
		('Lucid Dreams', 'Juice WRLD', 0.9);
