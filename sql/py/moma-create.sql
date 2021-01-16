drop table if exists artist cascade;
create table artist (
	artist_id integer,
	name varchar(255),
	bio text,
	nationality varchar(255),
	gender varchar(20),
	begin_date varchar(20),
	end_date varchar(20),
	wiki_qid varchar(20),
	ulan varchar(20),
	primary key(artist_id)
);

drop table if exists artwork;
create table artwork (
	title text,
	--artist_id integer references artist(artist_id),
	constituent_ids text,  
	artwork_date varchar(255),
	medium text,
	dimensions text,
	credit_line	text,
	accession_number varchar(255),
	classification varchar(255),
	department varchar(255),
	date_acquired varchar(255),
	cataloged character,
	artwork_id integer,
	url varchar(255),
	thumbnail_url varchar(255),
	circumference decimal,
	depth decimal,
	diameter decimal,
	height decimal,
	length decimal,	
	weight decimal,
	width decimal,
	seat_height decimal,
	duration decimal,
	primary key(artwork_id)
);

drop table if exists artist_artwork;
create table artist_artwork (
	artist_id integer references artist(artist_id),
	artwork_id integer references artwork(artwork_id)
);
