


## 2010 Census Data

Geography, by school district

School Districts Unified

https://www.census.gov/geo/maps-data/data/gazetteer2010.html


## What's in There

Read about fields:

https://www.census.gov/geo/maps-data/data/gazetteer2010.html



## What Are Some Questions we Can Answer?


* which state has the most school districts
* which school district is the most densely populated
* which school district is the least populated
* which school district probably has the _best sailing team_
* population density on state level?g

## Single Table Design

Which types to use?


## Aside on Primary Keys

Can also be tacked on at end as:

PRIMARY KEY(fips)

Ooh... composite primary key

PRIMARY KEY(question_id, tag_id)

## How about this?

DROP TABLE IF EXISTS sd;
CREATE TABLE school_districts (
	state text,
	fips text,
	name text,
	low_grade text,
	high_grade text,
	population integer,
	housing_units integer,
	land_area_meters real,
	water_area_meters real,
	land_area_miles real,
	water_area_miles real,
	lat real,
	lon real,
	PRIMARY KEY(fips)
);


## Import

How?

COPY table FROM '/file/name';
* format?
* has header?
* delimiter?
* null value?


COPY sd FROM '/tmp/sd-utf-8.txt' csv HEADER DELIMITER AS E'\t';

-- uh oh!

##  Uh Now What?

file Gaz_unsd_national.txt
man iconv
iconv -t UTF-8 Gaz_unsd_national.txt
iconv -f ISO-8859-1 -t UTF-8 Gaz_unsd_national.txt

whew!

## Cleaning

* remove some columns (some could be calculated maybe?)
* distinct values / counts - for example sd_name?
* strange to have population 0
* delete - no WAIT

## Add deleted column?

common columns:

* deleted
* modified
* created

## How Would That Look?

Transactions:

* BEGIN
* COMMIT
* ROLLBACK



## Views

CREATE VIEW sd_active AS SELECT * FROM school_districts WHERE deleted = FALSE;
