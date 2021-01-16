-- row_id,product_type,product_name,metal,concentration,units,manufacturer,made_in_country,collection_date,deleted
-- 659,Religious powder,Gulal powder,Lead,10,ppm,UNKNOWN OR NOT STATED,INDIA,12/03/2012 12:00:00 AM,No
-- https://data.cityofnewyork.us/Health/Metal-Content-of-Consumer-Products-Tested-by-the-N/da9u-wz3r

create table product (
	row_id bigint primary key,
	product_type text,
	product_name text,
	metal text,
	concentration numeric,
	units text,
	manufacturer text,
	made_in_country text,
	collection_date date,
	deleted text
);

