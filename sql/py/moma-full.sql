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

--Title,Artist,ConstituentID,ArtistBio,Nationality,BeginDate,EndDate,Gender,Date,Medium,Dimensions,CreditLine,AccessionNumber,Classification,Department,DateAcquired,Cataloged,ObjectID,URL,ThumbnailURL,Circumference (cm),Depth (cm),Diameter (cm),Height (cm),Length (cm),Weight (kg),Width (cm),Seat Height (cm),Duration (sec.)

drop table if exists artwork;
create table artwork (
	title text,
	artist text, -- val > varchar(255):  "Various Artists, Paul Klee, Max Beckmann, Karl Caspar, Conrad Felixmüller, Erich Heckel, René Beeh..."
	constituent_ids text, -- val > varchar(255): 
	artist_bio text, -- val > varchar(255): "(German, born Switzerland. 1879–1940) (German, 1884–1950) (German, 1879–1956) (German, 1897–..."
	nationality text, -- val > varchar(255): "() (American) (American) (American) (American) (American) (American) (American) (American) (American..."
	begin_date text, -- val > varchar(255): "(0) (1943) (1947) (1922) (1927) (1951) (1940) (1945) (1943) (1947) (1950) (1946) (1952) (1945) (1948..."
	end_date varchar(255), -- val > varchar(255)
	gender text, -- val > varchar(255): "() (Male) (Female) (Male) (Male) (Male) (Female) (Female) (Male) (Male) (Male) (Male) (Female) (Male..."
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

--\copy artist from Artists.csv csv header
--\copy artwork from Artworks.csv csv header

--insert into artist_artwork 
--(select artist_id::integer, artwork_id from (select trim(regexp_split_to_table(constituent_ids, ',')) as artist_id, artwork_id from artwork) tmp  where artist_id != '')
;
