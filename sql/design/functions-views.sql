-- Functions and Views, from our book -- Practical SQL by Anthony DeBarros
--
-- 0. create and import 2000 and 2010 data
--    queries sourced directly from chapter 4, 6, and 16 of our book...
--    see the associated github repo: https://github.com/anthonydb/practical-sql
--    download the following csvs:
--    https://github.com/anthonydb/practical-sql/blob/master/Chapter_04/us_counties_2010.csv
--    https://github.com/anthonydb/practical-sql/blob/master/Chapter_06/us_counties_2000.csv
CREATE TABLE us_counties_2010
(
    geo_name                       varchar(90),    -- Name of the geography
    state_us_abbreviation          varchar(2),     -- State/U.S. abbreviation
    summary_level                  varchar(3),     -- Summary Level
    region                         smallint,       -- Region
    division                       smallint,       -- Division
    state_fips                     varchar(2),     -- State FIPS code
    county_fips                    varchar(3),     -- County code
    area_land                      bigint,         -- Area (Land) in square meters
    area_water                     bigint,         -- Area (Water) in square meters
    population_count_100_percent   integer,        -- Population count (100%)
    housing_unit_count_100_percent integer,        -- Housing Unit count (100%)
    internal_point_lat             numeric(10, 7), -- Internal point (latitude)
    internal_point_lon             numeric(10, 7), -- Internal point (longitude)

    -- This section is referred to as P1. Race:
    p0010001                       integer,        -- Total population
    p0010002                       integer,        -- Population of one race:
    p0010003                       integer,        -- White Alone
    p0010004                       integer,        -- Black or African American alone
    p0010005                       integer,        -- American Indian and Alaska Native alone
    p0010006                       integer,        -- Asian alone
    p0010007                       integer,        -- Native Hawaiian and Other Pacific Islander alone
    p0010008                       integer,        -- Some Other Race alone
    p0010009                       integer,        -- Population of two or more races
    p0010010                       integer,        -- Population of two races:
    p0010011                       integer,        -- White; Black or African American
    p0010012                       integer,        -- White; American Indian and Alaska Native
    p0010013                       integer,        -- White; Asian
    p0010014                       integer,        -- White; Native Hawaiian and Other Pacific Islander
    p0010015                       integer,        -- White; Some Other Race
    p0010016                       integer,        -- Black or African American; American Indian and Alaska Native
    p0010017                       integer,        -- Black or African American; Asian
    p0010018                       integer,        -- Black or African American; Native Hawaiian and Other Pacific Islander
    p0010019                       integer,        -- Black or African American; Some Other Race
    p0010020                       integer,        -- American Indian and Alaska Native; Asian
    p0010021                       integer,        -- American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
    p0010022                       integer,        -- American Indian and Alaska Native; Some Other Race
    p0010023                       integer,        -- Asian; Native Hawaiian and Other Pacific Islander
    p0010024                       integer,        -- Asian; Some Other Race
    p0010025                       integer,        -- Native Hawaiian and Other Pacific Islander; Some Other Race
    p0010026                       integer,        -- Population of three races
    p0010047                       integer,        -- Population of four races
    p0010063                       integer,        -- Population of five races
    p0010070                       integer,        -- Population of six races

    -- This section is referred to as P2. HISPANIC OR LATINO, AND NOT HISPANIC OR LATINO BY RACE
    p0020001                       integer,        -- Total
    p0020002                       integer,        -- Hispanic or Latino
    p0020003                       integer,        -- Not Hispanic or Latino:
    p0020004                       integer,        -- Population of one race:
    p0020005                       integer,        -- White Alone
    p0020006                       integer,        -- Black or African American alone
    p0020007                       integer,        -- American Indian and Alaska Native alone
    p0020008                       integer,        -- Asian alone
    p0020009                       integer,        -- Native Hawaiian and Other Pacific Islander alone
    p0020010                       integer,        -- Some Other Race alone
    p0020011                       integer,        -- Two or More Races
    p0020012                       integer,        -- Population of two races
    p0020028                       integer,        -- Population of three races
    p0020049                       integer,        -- Population of four races
    p0020065                       integer,        -- Population of five races
    p0020072                       integer,        -- Population of six races

    -- This section is referred to as P3. RACE FOR THE POPULATION 18 YEARS AND OVER
    p0030001                       integer,        -- Total
    p0030002                       integer,        -- Population of one race:
    p0030003                       integer,        -- White alone
    p0030004                       integer,        -- Black or African American alone
    p0030005                       integer,        -- American Indian and Alaska Native alone
    p0030006                       integer,        -- Asian alone
    p0030007                       integer,        -- Native Hawaiian and Other Pacific Islander alone
    p0030008                       integer,        -- Some Other Race alone
    p0030009                       integer,        -- Two or More Races
    p0030010                       integer,        -- Population of two races
    p0030026                       integer,        -- Population of three races
    p0030047                       integer,        -- Population of four races
    p0030063                       integer,        -- Population of five races
    p0030070                       integer,        -- Population of six races

    -- This section is referred to as P4. HISPANIC OR LATINO, AND NOT HISPANIC OR LATINO BY RACE
    -- FOR THE POPULATION 18 YEARS AND OVER
    p0040001                       integer,        -- Total
    p0040002                       integer,        -- Hispanic or Latino
    p0040003                       integer,        -- Not Hispanic or Latino:
    p0040004                       integer,        -- Population of one race:
    p0040005                       integer,        -- White alone
    p0040006                       integer,        -- Black or African American alone
    p0040007                       integer,        -- American Indian and Alaska Native alone
    p0040008                       integer,        -- Asian alone
    p0040009                       integer,        -- Native Hawaiian and Other Pacific Islander alone
    p0040010                       integer,        -- Some Other Race alone
    p0040011                       integer,        -- Two or More Races
    p0040012                       integer,        -- Population of two races
    p0040028                       integer,        -- Population of three races
    p0040049                       integer,        -- Population of four races
    p0040065                       integer,        -- Population of five races
    p0040072                       integer,        -- Population of six races

    -- This section is referred to as H1. OCCUPANCY STATUS
    h0010001                       integer,        -- Total housing units
    h0010002                       integer,        -- Occupied
    h0010003                       integer         -- Vacant
);

-- replace w/ location of your file
COPY us_counties_2010
FROM '/tmp/us_counties_2010.csv'
WITH (FORMAT CSV, HEADER);

select * from us_counties_2010;
CREATE TABLE us_counties_2000 (
    geo_name varchar(90),              -- County/state name,
    state_us_abbreviation varchar(2),  -- State/U.S. abbreviation
    state_fips varchar(2),             -- State FIPS code
    county_fips varchar(3),            -- County code
    p0010001 integer,                  -- Total population
    p0010002 integer,                  -- Population of one race:
    p0010003 integer,                      -- White Alone
    p0010004 integer,                      -- Black or African American alone
    p0010005 integer,                      -- American Indian and Alaska Native alone
    p0010006 integer,                      -- Asian alone
    p0010007 integer,                      -- Native Hawaiian and Other Pacific Islander alone
    p0010008 integer,                      -- Some Other Race alone
    p0010009 integer,                  -- Population of two or more races
    p0010010 integer,                  -- Population of two races
    p0020002 integer,                  -- Hispanic or Latino
    p0020003 integer                   -- Not Hispanic or Latino:
);

-- replace w/ location of your file
COPY us_counties_2000
FROM '/tmp/us_counties_2000.csv'
WITH (FORMAT CSV, HEADER);

-- a quick test
select * from us_counties_2000 limit 50;
select * from us_counties_2010 limit 50;

-- 1. join census data first
--    use fips county and state to uniquely identify each row
select c2010.geo_name, c2010.state_us_abbreviation, c2000.p0010001 as pop2000, c2010.p0010001 as pop2010,
from us_counties_2000 c2000
inner join us_counties_2010 c2010
    on c2000.county_fips = c2010.county_fips
    and c2000.state_fips = c2010.state_fips;

-- 2. calculate pct_change and add to select list
--    to avoid integer division, cast one operand to decimal
select c2010.geo_name, c2010.state_us_abbreviation, c2000.p0010001 as pop2000, c2010.p0010001 as pop2010,
       round((c2010.p0010001 -  c2000.p0010001)::decimal / c2000.p0010001, 2) as pct_change
from us_counties_2000 c2000
inner join us_counties_2010 c2010
    on c2000.county_fips = c2010.county_fips
    and c2000.state_fips = c2010.state_fips;


-- 3. that was marginally annoying...
--    let's write a function to doooo this
--    functions can be written in plain SQL, plpgsql... and even Python, C, etc.
--    if using SQL, function body (a string) is a series of SQL statements ending with ;.
--    the result is either:
--    * all rows fo the last query (if returning setof tablename)
--    * the first row of the last query
--
--    ...let's try writing a function!
--    a. use create or replace function so that you can continually redefine your function
--    b. specify function signature:
--       function_name(param1 type1, param2 type2, ... paramN, typeN)
--    c. specify return value:
--       returns type as
--    d. add function body, a string literal... commonly delimited with $$ to allow string
--       literals in function body
--    e. specify what language is being used
--       language sql
create or replace function pct_change(old_val numeric, new_val numeric)
returns decimal as
    'select (new_val - old_val)::decimal / old_val;'
language sql
select pct_change(100, 150);
-- rewrite our query
select c2010.geo_name, c2010.state_us_abbreviation, c2000.p0010001 as pop2000, c2010.p0010001 as pop2010,
       pct_change(c2000.p0010001,c2010.p0010001) as pct_change
from us_counties_2000 c2000
         inner join us_counties_2010 c2010
                    on c2000.county_fips = c2010.county_fips
                        and c2000.state_fips = c2010.state_fips
-- 4. as an aside, it is possible to create a function that returns rows
--    let's create a function that gets all rows from a state abbreviation
--    make sure to use:
--    returns setof us_counties_2010 as
drop function get_by_state;
create or replace function get_by_state(state_abbreviation varchar(2)) returns setof us_counties_2010 as
'select * from us_counties_2010 where state_us_abbreviation = state_abbreviation;' language sql;
-- test our function
select * from get_by_state('NY');
-- 5. back to our original function, you can use another language, plpgsql... it allows things like
--    variables and loops (wat!? how are we so lucky?)
--    NOTE.. THIS IS IN PLPGSQL!!!
--    * declare variables in a declare block
--    * use var_name type
--    * uninitialized variables are set to null
--    * can initialize with colon and equals.. :=
--    * after declare, use transaction, begin end
--    * assignment works with :=
--    * alternative is query INTO var_name
--    * can be used to assign
--    * use return
create or replace function pct_change(old_val numeric, new_val numeric) returns decimal as $$
    declare
        ret decimal;
    begin
        --ret := (new_val - old_val)::decimal / old_val;
        select round((new_val - old_val)::decimal / old_val, 2) into ret;
        return ret;
    end;
$$
language plpgsql;
select pct_change(6, 8);
-- 6. ok, pct change works... back to our original query... if we want a table made out of it...
--    an aside on view syntax (create or replace view view_name as query)
create table webuser (
    username varchar(255),
    email varchar(255),
    deleted bool default FALSE
);
insert into webuser values
                           ('foo', 'foo@foo.foo'),
                           ('bar', 'bar@bar.bar'),
                           ('baz', 'baz@baz.baz'),
                            ('qux', 'qux@qux.qux');
update webuser set deleted = TRUE where username = 'foo';

select * from webuser;
select * from webuser where deleted = FALSE;

create or replace view active_webuser as
select * from webuser where deleted = FALSE;

select * from active_webuser;
--subquery one time use
--CTE one time use, readability
--function for procedures or calculations rather than subqueries
-- * a series of inserts, updates, deletes
-- * a query that is paramaterized - constrain funcionality
-- * "domain specific language"
-- views, multi use subquery has - still same as underlying table
-- other tables, takes up space! needs updating - not same as underlying tables, tho
create or replace view census_change as
select c2010.geo_name, c2010.state_us_abbreviation, c2000.p0010001 as pop2000, c2010.p0010001 as pop2010,
       pct_change(c2000.p0010001,c2010.p0010001) as pct_change
from us_counties_2000 c2000
         inner join us_counties_2010 c2010
                    on c2000.county_fips = c2010.county_fips
                        and c2000.state_fips = c2010.state_fips;
select * from census_change;
select * from census_change where state_us_abbreviation = 'NY';

select count(distinct county_fips)
from us_counties_2010 as c2010;

-- other function examples
create or replace function area_rect(length decimal, width decimal)
returns numeric as
'begin
return length * width;
end;'
language plpgsql;

create or replace function area_rect(length decimal, width decimal)
returns numeric as
'SELECT length * width;'
language sql;


create or replace function parse_name(
    s varchar
  )
  returns varchar[] as $$
declare
  result varchar[];
begin
  select
         array[trim(array_to_string(parts[1:array_length(parts, 1) - 1], ' '))::varchar,
         trim(parts[array_length(parts, 1)])::varchar]
  into result
  from (select string_to_array(s, ' ') as parts) as name_parts;
  return result;
end;
$$ language 'plpgsql';
select * from staging.movie;
select parse_name('Ray Lovelock');
select parse_name('Anna Maria Rizzoli');

