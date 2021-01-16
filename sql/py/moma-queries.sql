select artwork.title, artwork.artwork_date 
from artist 
inner join artist_artwork on artist.artist_id = artist_artwork.artist_id 
inner join artwork on artist_artwork.artwork_id = artwork.artwork_id 
where artist.name ilike '%cory arcangel%';


select lower(gender), count(artwork.artwork_id)
from artist 
inner join artist_artwork on artist.artist_id = artist_artwork.artist_id 
inner join artwork on artist_artwork.artwork_id = artwork.artwork_id 
group by lower(gender);
