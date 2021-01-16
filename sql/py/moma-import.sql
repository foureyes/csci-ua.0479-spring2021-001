-- \copy artist from Artists.csv header csv
-- \copy artwork from Artworks-No-Artist.csv csv header

insert into artist_artwork
	(select trim(regexp_split_to_table(constituent_ids, ','))::integer, artwork_id from artwork);
