--CREATE TABLE first, then copy....
--CREATE TABLE school_district (
--	state varchar(255),
--	geoid varchar(100),
--	name varchar(255),
--	low_grade varchar(10),
--	high_grade varchar(10),
--	population real,
--	housing_units real,
--	land_area_meters real,
--	water_area_meters real,
--	land_area_miles real, 
--	water_area_miles real,
--	lat numeric,
--	lon numeric
--);
--
--COPY school_district
--FROM '/tmp/Gaz_unsd_national.txt'
--csv HEADER DELIMITER AS E'\t' ENCODING 'LATIN1';

class12=# select distinct low_grade from school_district ;
 low_grade
-----------
 PK
 KG
 01
(3 rows)

class12=# select distinct hig from school_district ;

class12=# select distinct high_grade from school_district ;
 high_grade
------------
 12
(1 row)

class12=# KG
class12-#
class12-# ^C
class12=# select low_grade, count(*) from school_district group by low_grade;
 low_grade | count
-----------+-------
 PK        |  7505
 KG        |  3386
 01        |     1
(3 rows)

class12=# select * from school_district where low_grade = '01';
 state |  geoid  |            name             | low_grade | high_grade | population | housing_units | land_area_meters | water_area_meters | land_area_miles | water_area_miles |    lat    |     lon
-------+---------+-----------------------------+-----------+------------+------------+---------------+------------------+-------------------+-----------------+------------------+-----------+-------------
 WA    | 5307860 | Shaw Island School District | 01        | 12         |        240 |           245 |      1.99643e+07 |       2.40753e+07 |           7.708 |            9.296 | 48.568814 | -122.957539
(1 row)

class12=# select * from school_district limit 10;
 state |  geoid  |                name                 | low_grade | high_grade | population | housing_units | land_area_meters | water_area_meters | land_area_miles | water_area_miles |    lat    |    lon
-------+---------+-------------------------------------+-----------+------------+------------+---------------+------------------+-------------------+-----------------+------------------+-----------+------------
 AL    | 0100001 | Fort Rucker School District         | KG        | 12         |       4647 |          1459 |      2.33067e+08 |       2.73522e+06 |          89.988 |            1.056 | 31.405967 | -85.744807
 AL    | 0100003 | Maxwell AFB School District         | KG        | 12         |       2514 |           393 |      8.47678e+06 |            566857 |           3.273 |            0.219 | 32.382440 | -86.363389
 AL    | 0100005 | Albertville City School District    | KG        | 12         |      21160 |          8128 |      6.87807e+07 |            258708 |          26.556 |              0.1 | 34.263130 | -86.210660
 AL    | 0100006 | Marshall County School District     | KG        | 12         |      47197 |         21108 |      1.26779e+09 |       1.03648e+08 |         489.498 |           40.019 | 34.369332 | -class12=# select * from school_district where population is null;
 state | geoid | name | low_grade | high_grade | population | housing_units | land_area_meters | water_area_meters | land_area_miles | water_area_miles | lat | lon
-------+-------+------+-----------+------------+------------+---------------+------------------+-------------------+-----------------+------------------+-----+-----
(0 rows)

class12=# select count(*) from school_district where population <= 0;
 count
-------
    22
(1 row)

class12=# select * from school_district where population <= 0;
 state |  geoid  |                name                 | low_grade | high_grade | population | housing_units | land_area_meters | water_area_meters | land_area_miles | water_area_miles |    lat    |     lon
-------+---------+-------------------------------------+-----------+------------+------------+---------------+------------------+-------------------+-----------------+------------------+-----------+-------------
 CA    | 0699998 | School District Not Defined (Water) | PK        | 12         |          0 |             0 |            95190 |       2.32513e+09 |           0.037 |          897.737 | 40.438566 | -124.413693
 CT    | 0999998 | School District Not Defined (Water) | PK        | 12         |          0 |             0 |                0 |       1.09533e+09 |               0 |           422.91 | 41.166607 |  -72.842465
 IL    | 1799998 | School District Not Defined (Water) | PK        | 12         |          0 |             0 |                0 |        4.0714e+09 |               0 |          1571.98 | 42.175365 |  -87.422510
 IN    | 1899998 | School District Not Defined (Water) | PK        | 12         |          0 |             0 |                0 |        5.4003e+08 |               0 |          208.507 | 41.707153 |  class12=# select popul from school_district where population <= 0;

class12=# select name, population from school_district where population <= 0;
                name                 | population
-------------------------------------+------------
 School District Not Defined (Water) |          0
 School District Not Defined (Water) |          0
 School District Not Defined (Water) |          0
 School District Not Defined (Water) |          0
 Sagadahoc Unorganized Territory     |          0
 Louds Island Unorganized Territory  |          0
 School District Not Defined (Water) |          0
 School District Not Defined (Water) |          0
 School District Not Defined (Water) |          0
 School District Not Defined         |          0
 School District Not Defined (Water) |          0
 School District Not Defined (Water) |          0
 School District Not Defined (Water) |          0
 North Bass Local School District    |          0
 School District Not Defined         |          0
class12=# BEGIN;
BEGIN
class12=# DELETE FROM school_district WHERE population <= 0;
DELETE 22
class12=# select state, name, population from school_district where population <= 0;
 state | name | population
-------+------+------------
(0 rows)

class12=# ROLLBACK;
ROLLBACK
class12=# select state, name, population from school_district where population <= 0;
 state |                name                 | population
-------+-------------------------------------+------------
 CA    | School District Not Defined (Water) |          0
 CT    | School District Not Defined (Water) |          0
 IL    | School District Not Defined (Water) |          0
 IN    | School District Not Defined (Water) |          0
 ME    | Sagadahoc Unorganized Territory     |          0
 ME    | Louds Island Unorganized Territory  |          0
 ME    | School District Not Defined (Water) |          0
 MA    | School District Not Defined (Water) |          0
 MN    | School District Not Defined (Water) |          0
 NE    | School District Not Defined         |          0
 NH    | School District Not Defined (Water) |          0
 NJ    | School District Not Defined (Water) |          0
 NY    | School District Not Defined (Water) |          0
 OH    | North Bass Local School District    |          0
 OR    | School District Not Defined         |          0
 PA    | School District Not Defined (Water) |          0
 RI    | School District Not Defined (Water) |          0
 VT    | Avery's Gore School District        |          0
 VT    | Lewis School District               |          0
 VT    | Warner's Grant School District      |          0
 WI    | School District Not Defined         |          0
 WI    | School District Not Defined (Water) |          0
(22 rows)
