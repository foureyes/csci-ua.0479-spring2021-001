class11=# CREATE TABLE student (
class11(# netid varchar(100) PRIMARY KEY,
class11(# class text,
class11(# first varchar(255) NOT NULL,
class11(# last varchar(255) NOT NULL,
class11(# grad_date timestamptz DEFAULT NOW(),
class11(# debt money,
class11(# midtermscore numeric
class11(# ); -- creates a table called student
CREATE TABLE
class11=# select * from student;
 netid | class | first | last | grad_date | debt | midtermscore
-------+-------+-------+------+-----------+------+--------------
(0 rows)

class11=# -- describes the student table
class11=# \d student
                          Table "public.student"
    Column    |           Type           | Collation | Nullable | Default
--------------+--------------------------+-----------+----------+---------
 netid        | character varying(100)   |           | not null |
 class        | text                     |           |          |
 first        | character varying(255)   |           | not null |
 last         | character varying(255)   |           | not null |
 grad_date    | timestamp with time zone |           |          | now()
 debt         | money                    |           |          |
 midtermscore | numeric                  |           |          |
Indexes:
    "student_pkey" PRIMARY KEY, btree (netid)


class11=# insert into student (netid, class, first, last, midtermscore) values ('jjv222', 'database stuff', 'joe', 'v', 80); -- add a row to student table
INSERT 0 1
class11=# select netid, first from student;
 netid  | first
--------+-------
 jjv222 | joe
(1 row)


class11=# -- importing a file containing sql statements
class11=# \i /tmp/movies.sql.txt 
CREATE TABLE
INSERT 0 17
class11=# -- list all tables
class11=# \d 
              List of relations
 Schema |     Name     |   Type   |  Owner
--------+--------------+----------+----------
 public | movie        | table    | jversoza
 public | movie_id_seq | sequence | jversoza
 public | student      | table    | jversoza
(3 rows)


class11=# -- describe the movie table
class11=# \d movie 
                                      Table "public.movie"
  Column  |           Type           | Collation | Nullable |              Default
----------+--------------------------+-----------+----------+-----------------------------------
 id       | integer                  |           | not null | nextval('movie_id_seq'::regclass)
 title    | character varying(50)    |           |          |
 director | character varying(100)   |           |          |
 year     | timestamp with time zone |           |          |
 runtime  | integer                  |           |          |
 genre    | character varying(255)   |           |          |
 budget   | money                    |           |          |
 gross    | money                    |           |          |
Indexes:
    "movie_pkey" PRIMARY KEY, btree (id)

class11=# -- show all movies
class11=# select * from movie;
 id |                  title                   |      director      |          year          | runtime |            genre            |     budget      |      gross
----+------------------------------------------+--------------------+------------------------+---------+-----------------------------+-----------------+-----------------
  1 | Blue Velvet                              | David Lynch        | 1986-01-01 00:00:00-05 |     120 | Neo Noir Mystery Thriller   |   $6,000,000.00 |   $8,600,000.00
  2 | Dune                                     | David Lynch        | 1984-01-01 00:00:00-05 |     136 | Science Fiction             |  $40,000,000.00 |  $30,900,000.00
  3 | Strange Days                             | Kathryn Bigelow    | 1995-01-01 00:00:00-05 |     145 | Science Fiction             |  $42,000,000.00 |   $8,000,000.00
  4 | Point Break                              | Kathryn Bigelow    | 1991-01-01 00:00:00-05 |     122 | Crime Thriller              |  $24,000,000.00 |  $83,500,000.00
  5 | Zero Dark Thirty                         | Kathryn Bigelow    | 2012-01-01 00:00:00-05 |     157 | Political Thriller          |  $40,000,000.00 | $132,800,000.00
  6 | Blade Runner                             | Ridley Scott       | 1982-01-01 00:00:00-05 |     117 | Sci-Fi                      |  $28,000,000.00 |  $33,800,000.00
  7 | Blade Runner 2049                        | Denis Villeneuve   | 2017-01-01 00:00:00-05 |     163 | Science Fiction             | $185,000,000.00 | $259,200,000.00
  8 | Alien                                    | Ridley Scott       | 1979-01-01 00:00:00-05 |     117 | Sci-Fi                      |  $11,000,000.00 | $203,600,000.00
  9 | Alien Covenant                           | Ridley Scott       | 1982-01-01 00:00:00-05 |     122 | Science Fiction             | $111,000,000.00 | $240,900,000.00
 10 | 2046                                     | Wong Kar-wai       | 1982-01-01 00:00:00-05 |     122 | Drama                       |  $12,000,000.00 |  $19,500,000.00
 11 | Wonder Woman                             | Wong Kar-wai       | 2017-01-01 00:00:00-05 |     141 | Super Hero                  | $150,000,000.00 | $821,000,000.00
 12 | La Piel Que Habito (The Skin I Live In)  | Pedro Almodóvar    | 2011-01-01 00:00:00-05 |     120 | Horror                      |  $13,500,000.00 |  $30,800,000.00
 13 | Los Abrazos Rotos (Broken Embraces)      | Pedro Almodóvar    | 2009-01-01 00:00:00-05 |     128 | Romantic Thriller           |  $18,000,000.00 |  $31,000,000.00
 14 | El Laberinto del Fauno (Pan's Labyrinth) | Guillermo del Toro | 2006-01-01 00:00:00-05 |     119 | Dark Fantasy Horror         |  $19,000,000.00 |  $83,300,000.00
 15 | Shape of Water                           | Guillermo del Toro | 2017-01-01 00:00:00-05 |     123 | Romantic Dark Fantasy Drama |  $20,000,000.00 | $195,200,000.00
class11=# -- only show title, director and gross
class11=# select title, director, gross from movie;
                  title                   |      director      |      gross
------------------------------------------+--------------------+-----------------
 Blue Velvet                              | David Lynch        |   $8,600,000.00
 Dune                                     | David Lynch        |  $30,900,000.00
 Strange Days                             | Kathryn Bigelow    |   $8,000,000.00
 Point Break                              | Kathryn Bigelow    |  $83,500,000.00
 Zero Dark Thirty                         | Kathryn Bigelow    | $132,800,000.00
 Blade Runner                             | Ridley Scott       |  $33,800,000.00
 Blade Runner 2049                        | Denis Villeneuve   | $259,200,000.00
 Alien                                    | Ridley Scott       | $203,600,000.00
 Alien Covenant                           | Ridley Scott       | $240,900,000.00
 2046                                     | Wong Kar-wai       |  $19,500,000.00
 Wonder Woman                             | Wong Kar-wai       | $821,000,000.00
 La Piel Que Habito (The Skin I Live In)  | Pedro Almodóvar    |  $30,800,000.00
 Los Abrazos Rotos (Broken Embraces)      | Pedro Almodóvar    |  $31,000,000.00
 El Laberinto del Fauno (Pan's Labyrinth) | Guillermo del Toro |  $83,300,000.00
 Shape of Water                           | Guillermo del Toro | $195,200,000.00

class11=# -- order rows by gross ascending
class11=# select title, director, gross from movie order by gross;
                  title                   |      director      |      gross
------------------------------------------+--------------------+-----------------
 Strange Days                             | Kathryn Bigelow    |   $8,000,000.00
 Blue Velvet                              | David Lynch        |   $8,600,000.00
 2046                                     | Wong Kar-wai       |  $19,500,000.00
 La Piel Que Habito (The Skin I Live In)  | Pedro Almodóvar    |  $30,800,000.00
 Dune                                     | David Lynch        |  $30,900,000.00
 Los Abrazos Rotos (Broken Embraces)      | Pedro Almodóvar    |  $31,000,000.00
 Blade Runner                             | Ridley Scott       |  $33,800,000.00
 El Laberinto del Fauno (Pan's Labyrinth) | Guillermo del Toro |  $83,300,000.00
 Point Break                              | Kathryn Bigelow    |  $83,500,000.00
 Hellboy                                  | Guillermo del Toro |  $99,300,000.00
 Zero Dark Thirty                         | Kathryn Bigelow    | $132,800,000.00
 Shape of Water                           | Guillermo del Toro | $195,200,000.00
 Alien                                    | Ridley Scott       | $203,600,000.00
 Alien Covenant                           | Ridley Scott       | $240,900,000.00
 Blade Runner 2049                        | Denis Villeneuve   | $259,200,000.00
 Pacific Rim                              | Guillermo del Toro | $411,000,000.00
 Wonder Woman                             | Wong Kar-wai       | $821,000,000.00
(17 rows)

class11=# -- order rows by gross descending
class11=# select title, director, gross from movie order by gross desc;
                  title                   |      director      |      gross
------------------------------------------+--------------------+-----------------
 Wonder Woman                             | Wong Kar-wai       | $821,000,000.00
 Pacific Rim                              | Guillermo del Toro | $411,000,000.00
 Blade Runner 2049                        | Denis Villeneuve   | $259,200,000.00
 Alien Covenant                           | Ridley Scott       | $240,900,000.00
 Alien                                    | Ridley Scott       | $203,600,000.00
 Shape of Water                           | Guillermo del Toro | $195,200,000.00
 Zero Dark Thirty                         | Kathryn Bigelow    | $132,800,000.00
 Hellboy                                  | Guillermo del Toro |  $99,300,000.00
 Point Break                              | Kathryn Bigelow    |  $83,500,000.00
 El Laberinto del Fauno (Pan's Labyrinth) | Guillermo del Toro |  $83,300,000.00
 Blade Runner                             | Ridley Scott       |  $33,800,000.00
 Los Abrazos Rotos (Broken Embraces)      | Pedro Almodóvar    |  $31,000,000.00
 Dune                                     | David Lynch        |  $30,900,000.00
 La Piel Que Habito (The Skin I Live In)  | Pedro Almodóvar    |  $30,800,000.00
 2046                                     | Wong Kar-wai       |  $19,500,000.00

class11=# -- try ordering by director ascending
class11=# select title, director, gross from movie order by director;
                  title                   |      director      |      gross
------------------------------------------+--------------------+-----------------
 Dune                                     | David Lynch        |  $30,900,000.00
 Blue Velvet                              | David Lynch        |   $8,600,000.00
 Blade Runner 2049                        | Denis Villeneuve   | $259,200,000.00
 Hellboy                                  | Guillermo del Toro |  $99,300,000.00
 El Laberinto del Fauno (Pan's Labyrinth) | Guillermo del Toro |  $83,300,000.00
 Shape of Water                           | Guillermo del Toro | $195,200,000.00
 Pacific Rim                              | Guillermo del Toro | $411,000,000.00
 Strange Days                             | Kathryn Bigelow    |   $8,000,000.00
 Point Break                              | Kathryn Bigelow    |  $83,500,000.00
 Zero Dark Thirty                         | Kathryn Bigelow    | $132,800,000.00
 Los Abrazos Rotos (Broken Embraces)      | Pedro Almodóvar    |  $31,000,000.00
 La Piel Que Habito (The Skin I Live In)  | Pedro Almodóvar    |  $30,800,000.00
 Alien                                    | Ridley Scott       | $203,600,000.00
 Blade Runner                             | Ridley Scott       |  $33,800,000.00
 Alien Covenant                           | Ridley Scott       | $240,900,000.00

class11=# -- use both director and gross to order rows
class11=# select title, director, gross from movie order by director, gross
;
                  title                   |      director      |      gross
------------------------------------------+--------------------+-----------------
 Blue Velvet                              | David Lynch        |   $8,600,000.00
 Dune                                     | David Lynch        |  $30,900,000.00
 Blade Runner 2049                        | Denis Villeneuve   | $259,200,000.00
 El Laberinto del Fauno (Pan's Labyrinth) | Guillermo del Toro |  $83,300,000.00
 Hellboy                                  | Guillermo del Toro |  $99,300,000.00
 Shape of Water                           | Guillermo del Toro | $195,200,000.00
 Pacific Rim                              | Guillermo del Toro | $411,000,000.00
 Strange Days                             | Kathryn Bigelow    |   $8,000,000.00
 Point Break                              | Kathryn Bigelow    |  $83,500,000.00
 Zero Dark Thirty                         | Kathryn Bigelow    | $132,800,000.00
 La Piel Que Habito (The Skin I Live In)  | Pedro Almodóvar    |  $30,800,000.00
 Los Abrazos Rotos (Broken Embraces)      | Pedro Almodóvar    |  $31,000,000.00
 Blade Runner                             | Ridley Scott       |  $33,800,000.00
 Alien                                    | Ridley Scott       | $203,600,000.00
 Alien Covenant                           | Ridley Scott       | $240,900,000.00

class11=# -- query all movies again...
class11=# select title, director, genre, gross from movie ;
                  title                   |      director      |            genre            |      gross
------------------------------------------+--------------------+-----------------------------+-----------------
 Blue Velvet                              | David Lynch        | Neo Noir Mystery Thriller   |   $8,600,000.00
 Dune                                     | David Lynch        | Science Fiction             |  $30,900,000.00
 Strange Days                             | Kathryn Bigelow    | Science Fiction             |   $8,000,000.00
 Point Break                              | Kathryn Bigelow    | Crime Thriller              |  $83,500,000.00
 Zero Dark Thirty                         | Kathryn Bigelow    | Political Thriller          | $132,800,000.00
 Blade Runner                             | Ridley Scott       | Sci-Fi                      |  $33,800,000.00
 Blade Runner 2049                        | Denis Villeneuve   | Science Fiction             | $259,200,000.00

class11=# -- now only show distinct genres
class11=# select distinct genre from movie;
            genre
-----------------------------
 Horror
 Drama
 Sci-Fi
 Romantic Thriller
 Super Hero
 Political Thriller
 Romantic Dark Fantasy Drama
 Crime Thriller
 Neo Noir Mystery Thriller
 Science Fiction
 Dark Fantasy Horror
(11 rows)

class11=# -- only show rows that have a genre of Science Fiction
class11=# select title, director, genre from movie where genre = 'Science Fiction';
       title       |     director     |      genre
-------------------+------------------+-----------------
 Dune              | David Lynch      | Science Fiction
 Strange Days      | Kathryn Bigelow  | Science Fiction
 Blade Runner 2049 | Denis Villeneuve | Science Fiction
 Alien Covenant    | Ridley Scott     | Science Fiction
(4 rows)

class11=# -- only show rows that have a genre that's not Science Fiction
class11=# select title, director, genre from movie where genre <> 'Science Fiction';
                  title                   |      director      |            genre
------------------------------------------+--------------------+-----------------------------
 Blue Velvet                              | David Lynch        | Neo Noir Mystery Thriller
 Point Break                              | Kathryn Bigelow    | Crime Thriller
 Zero Dark Thirty                         | Kathryn Bigelow    | Political Thriller
 Blade Runner                             | Ridley Scott       | Sci-Fi
 Alien                                    | Ridley Scott       | Sci-Fi
 2046                                     | Wong Kar-wai       | Drama
 Wonder Woman                             | Wong Kar-wai       | Super Hero
 La Piel Que Habito (The Skin I Live In)  | Pedro Almodóvar    | Horror
 Los Abrazos Rotos (Broken Embraces)      | Pedro Almodóvar    | Romantic Thriller
 El Laberinto del Fauno (Pan's Labyrinth) | Guillermo del Toro | Dark Fantasy Horror
 Shape of Water                           | Guillermo del Toro | Romantic Dark Fantasy Drama
 Pacific Rim                              | Guillermo del Toro | Sci-Fi
 Hellboy                                  | Guillermo del Toro | Super Hero
(13 rows)

class11=# -- only show rows that have a genre has thriller in it (ignore case)
class11=# select title, director, genre from movie where genre ilike '%thriller%';
                title                |    director     |           genre
-------------------------------------+-----------------+---------------------------
 Blue Velvet                         | David Lynch     | Neo Noir Mystery Thriller
 Point Break                         | Kathryn Bigelow | Crime Thriller
 Zero Dark Thirty                    | Kathryn Bigelow | Political Thriller
 Los Abrazos Rotos (Broken Embraces) | Pedro Almodóvar | Romantic Thriller
(4 rows)

class11=# -- use and to put together two conditions
class11=# select title, director, genre from movie where genre ilike '%thriller%' and director <> 'Kathryn Bigelow';
                title                |    director     |           genre
-------------------------------------+-----------------+---------------------------
 Blue Velvet                         | David Lynch     | Neo Noir Mystery Thriller
 Los Abrazos Rotos (Broken Embraces) | Pedro Almodóvar | Romantic Thriller
(2 rows)

class11=# -- show budget and gross
class11=# select title, budget, gross from movie;
                  title                   |     budget      |      gross
------------------------------------------+-----------------+-----------------
 Blue Velvet                              |   $6,000,000.00 |   $8,600,000.00
 Dune                                     |  $40,000,000.00 |  $30,900,000.00
 Strange Days                             |  $42,000,000.00 |   $8,000,000.00
 Point Break                              |  $24,000,000.00 |  $83,500,000.00
 Zero Dark Thirty                         |  $40,000,000.00 | $132,800,000.00
 Blade Runner                             |  $28,000,000.00 |  $33,800,000.00
 Blade Runner 2049                        | $185,000,000.00 | $259,200,000.00
 Alien                                    |  $11,000,000.00 | $203,600,000.00
 Alien Covenant                           | $111,000,000.00 | $240,900,000.00
 2046                                     |  $12,000,000.00 |  $19,500,000.00
 Wonder Woman                             | $150,000,000.00 | $821,000,000.00
 La Piel Que Habito (The Skin I Live In)  |  $13,500,000.00 |  $30,800,000.00
 Los Abrazos Rotos (Broken Embraces)      |  $18,000,000.00 |  $31,000,000.00
 El Laberinto del Fauno (Pan's Labyrinth) |  $19,000,000.00 |  $83,300,000.00
 Shape of Water                           |  $20,000,000.00 | $195,200,000.00
 Pacific Rim                              | $200,000,000.00 | $411,000,000.00

class11=# -- calculate return on investment (include expression in list of columns)
class11=# select title, budget, gross, (gross - budget) / budget as roi from movie;
                  title                   |     budget      |      gross      |        roi
------------------------------------------+-----------------+-----------------+-------------------
 Blue Velvet                              |   $6,000,000.00 |   $8,600,000.00 | 0.433333333333333
 Dune                                     |  $40,000,000.00 |  $30,900,000.00 |           -0.2275
 Strange Days                             |  $42,000,000.00 |   $8,000,000.00 | -0.80952380952381
 Point Break                              |  $24,000,000.00 |  $83,500,000.00 |  2.47916666666667
 Zero Dark Thirty                         |  $40,000,000.00 | $132,800,000.00 |              2.32
 Blade Runner                             |  $28,000,000.00 |  $33,800,000.00 | 0.207142857142857
 Blade Runner 2049                        | $185,000,000.00 | $259,200,000.00 | 0.401081081081081
 Alien                                    |  $11,000,000.00 | $203,600,000.00 |  17.5090909090909
 Alien Covenant                           | $111,000,000.00 | $240,900,000.00 |  1.17027027027027
 2046                                     |  $12,000,000.00 |  $19,500,000.00 |             0.625
 Wonder Woman                             | $150,000,000.00 | $821,000,000.00 |  4.47333333333333
 La Piel Que Habito (The Skin I Live In)  |  $13,500,000.00 |  $30,800,000.00 |  1.28148148148148
 Los Abrazos Rotos (Broken Embraces)      |  $18,000,000.00 |  $31,000,000.00 | 0.722222222222222
 El Laberinto del Fauno (Pan's Labyrinth) |  $19,000,000.00 |  $83,300,000.00 |  3.38421052631579
 Shape of Water                           |  $20,000,000.00 | $195,200,000.00 |              8.76
 Pacific Rim                              | $200,000,000.00 | $411,000,000.00 |             1.055

class11=# -- you can even order by a calculated column (which we've named roi)
class11=# select title, budget, gross, (gross - budget) / budget as roi from movie order by roi desc;
                  title                   |     budget      |      gross      |        roi
------------------------------------------+-----------------+-----------------+-------------------
 Alien                                    |  $11,000,000.00 | $203,600,000.00 |  17.5090909090909
 Shape of Water                           |  $20,000,000.00 | $195,200,000.00 |              8.76
 Wonder Woman                             | $150,000,000.00 | $821,000,000.00 |  4.47333333333333
 El Laberinto del Fauno (Pan's Labyrinth) |  $19,000,000.00 |  $83,300,000.00 |  3.38421052631579
 Point Break                              |  $24,000,000.00 |  $83,500,000.00 |  2.47916666666667
 Zero Dark Thirty                         |  $40,000,000.00 | $132,800,000.00 |              2.32
 La Piel Que Habito (The Skin I Live In)  |  $13,500,000.00 |  $30,800,000.00 |  1.28148148148148
 Alien Covenant                           | $111,000,000.00 | $240,900,000.00 |  1.17027027027027
 Pacific Rim                              | $200,000,000.00 | $411,000,000.00 |             1.055
 Los Abrazos Rotos (Broken Embraces)      |  $18,000,000.00 |  $31,000,000.00 | 0.722222222222222
 2046                                     |  $12,000,000.00 |  $19,500,000.00 |             0.625
 Hellboy                                  |  $66,000,000.00 |  $99,300,000.00 | 0.504545454545455
 Blue Velvet                              |   $6,000,000.00 |   $8,600,000.00 | 0.433333333333333
 Blade Runner 2049                        | $185,000,000.00 | $259,200,000.00 | 0.401081081081081
 Blade Runner                             |  $28,000,000.00 |  $33,800,000.00 | 0.207142857142857
 Dune                                     |  $40,000,000.00 |  $30,900,000.00 |           -0.2275

class11=# -- an example of casting to numeric
class11=# select title, budget, gross, ((gross - budget) / budget)::numeric as roi from movie order by roi desc;
                  title                   |     budget      |      gross      |        roi
------------------------------------------+-----------------+-----------------+-------------------
 Alien                                    |  $11,000,000.00 | $203,600,000.00 |  17.5090909090909
 Shape of Water                           |  $20,000,000.00 | $195,200,000.00 |              8.76
 Wonder Woman                             | $150,000,000.00 | $821,000,000.00 |  4.47333333333333
 El Laberinto del Fauno (Pan's Labyrinth) |  $19,000,000.00 |  $83,300,000.00 |  3.38421052631579
 Point Break                              |  $24,000,000.00 |  $83,500,000.00 |  2.47916666666667
 Zero Dark Thirty                         |  $40,000,000.00 | $132,800,000.00 |              2.32
 La Piel Que Habito (The Skin I Live In)  |  $13,500,000.00 |  $30,800,000.00 |  1.28148148148148
 Alien Covenant                           | $111,000,000.00 | $240,900,000.00 |  1.17027027027027
 Pacific Rim                              | $200,000,000.00 | $411,000,000.00 |             1.055
 Los Abrazos Rotos (Broken Embraces)      |  $18,000,000.00 |  $31,000,000.00 | 0.722222222222222
 2046                                     |  $12,000,000.00 |  $19,500,000.00 |             0.625
 Hellboy                                  |  $66,000,000.00 |  $99,300,000.00 | 0.504545454545455
 Blue Velvet                              |   $6,000,000.00 |   $8,600,000.00 | 0.433333333333333
 Blade Runner 2049                        | $185,000,000.00 | $259,200,000.00 | 0.401081081081081
 Blade Runner                             |  $28,000,000.00 |  $33,800,000.00 | 0.207142857142857
 Dune                                     |  $40,000,000.00 |  $30,900,000.00 |           -0.2275

class11=# -- using round (two argument version of round only works on numeric values)
class11=# -- btw, pg_typeof returns type of column
class11=# select title, budget, gross, round(((gross - budget) / budget)::numeric, 2) as roi from movie order by roi desc;
                  title                   |     budget      |      gross      |  roi
------------------------------------------+-----------------+-----------------+-------
 Alien                                    |  $11,000,000.00 | $203,600,000.00 | 17.51
 Shape of Water                           |  $20,000,000.00 | $195,200,000.00 |  8.76
 Wonder Woman                             | $150,000,000.00 | $821,000,000.00 |  4.47
 El Laberinto del Fauno (Pan's Labyrinth) |  $19,000,000.00 |  $83,300,000.00 |  3.38
 Point Break                              |  $24,000,000.00 |  $83,500,000.00 |  2.48
 Zero Dark Thirty                         |  $40,000,000.00 | $132,800,000.00 |  2.32
 La Piel Que Habito (The Skin I Live In)  |  $13,500,000.00 |  $30,800,000.00 |  1.28
 Alien Covenant                           | $111,000,000.00 | $240,900,000.00 |  1.17
 Pacific Rim                              | $200,000,000.00 | $411,000,000.00 |  1.06
 Los Abrazos Rotos (Broken Embraces)      |  $18,000,000.00 |  $31,000,000.00 |  0.72
 2046                                     |  $12,000,000.00 |  $19,500,000.00 |  0.63
 Hellboy                                  |  $66,000,000.00 |  $99,300,000.00 |  0.50
 Blue Velvet                              |   $6,000,000.00 |   $8,600,000.00 |  0.43
 Blade Runner 2049                        | $185,000,000.00 | $259,200,000.00 |  0.40
 Blade Runner                             |  $28,000,000.00 |  $33,800,000.00 |  0.21
 Dune                                     |  $40,000,000.00 |  $30,900,000.00 | -0.23

class11=# -- note that an aliased column cannot be used in where clause... wat
class11=# select title, budget, gross, round(((gross - budget) / budget)::numeric, 2) as roi from movie where roi < 0 order by roi desc;
ERROR:  column "roi" does not exist
LINE 1: ...t) / budget)::numeric, 2) as roi from movie where roi < 0 or...
                                                             ^
class11=# -- so, use calculation in where clause
class11=# select title, budget, gross, round(((gross - budget) / budget)::numeric, 2) as roi from movie where round(((gross - budget) / budget)::numeric, 2) < 0 order by roi desc;
    title     |     budget     |     gross      |  roi
--------------+----------------+----------------+-------
 Dune         | $40,000,000.00 | $30,900,000.00 | -0.23
 Strange Days | $42,000,000.00 |  $8,000,000.00 | -0.81
(2 rows)

class11=# -- add an roi column to movie so we can permanently have that field
class11=# alter table movie add column roi numeric;
ALTER TABLE

class11=# -- notice the new column!
class11=# \d movie
                                      Table "public.movie"
  Column  |           Type           | Collation | Nullable |              Default
----------+--------------------------+-----------+----------+-----------------------------------
 id       | integer                  |           | not null | nextval('movie_id_seq'::regclass)
 title    | character varying(50)    |           |          |
 director | character varying(100)   |           |          |
 year     | timestamp with time zone |           |          |
 runtime  | integer                  |           |          |
 genre    | character varying(255)   |           |          |
 budget   | money                    |           |          |
 gross    | money                    |           |          |
 roi      | numeric                  |           |          |
Indexes:
    "movie_pkey" PRIMARY KEY, btree (id)

class11=# --currently, new column has null values
class11=# select title, roi from movie;
                  title                   | roi
------------------------------------------+-----
 Blue Velvet                              |
 Dune                                     |
 Strange Days                             |
 Point Break                              |
 Zero Dark Thirty                         |
 Blade Runner                             |
 Blade Runner 2049                        |
 Alien                                    |
 Alien Covenant                           |
 2046                                     |
 Wonder Woman                             |
 La Piel Que Habito (The Skin I Live In)  |
 Los Abrazos Rotos (Broken Embraces)      |
 El Laberinto del Fauno (Pan's Labyrinth) |
 Shape of Water                           |
 Pacific Rim                              |

class11=# -- update all rows so that roi is set to a value based on other columns
class11=# update movie set roi = ((gross - budget) / budget)::numeric;
UPDATE 17
class11=# select title, roi from movie;
                  title                   |        roi
------------------------------------------+-------------------
 Blue Velvet                              | 0.433333333333333
 Dune                                     |           -0.2275
 Strange Days                             | -0.80952380952381
 Point Break                              |  2.47916666666667
 Zero Dark Thirty                         |              2.32
 Blade Runner                             | 0.207142857142857
 Blade Runner 2049                        | 0.401081081081081
 Alien                                    |  17.5090909090909
 Alien Covenant                           |  1.17027027027027
 2046                                     |             0.625
 Wonder Woman                             |  4.47333333333333
 La Piel Que Habito (The Skin I Live In)  |  1.28148148148148
 Los Abrazos Rotos (Broken Embraces)      | 0.722222222222222
 El Laberinto del Fauno (Pan's Labyrinth) |  3.38421052631579
 Shape of Water                           |              8.76
 Pacific Rim                              |             1.055

class11=# -- fix duplicate genre
class11=# update movie set genre = 'Science Fiction' where genre = 'Sci-Fi';
UPDATE 3

class11=# -- see... now Sci-Fi is folded into Science Fiction
class11=# select distinct genre from movie;
            genre
-----------------------------
 Horror
 Drama
 Romantic Thriller
 Super Hero
 Political Thriller
 Romantic Dark Fantasy Drama
 Crime Thriller
 Neo Noir Mystery Thriller
 Science Fiction
 Dark Fantasy Horror
(10 rows)

class11=# -- group all rows that have same genre and count them
class11=# select genre, count(*) from movie group by genre;
            genre            | count
-----------------------------+-------
 Horror                      |     1
 Drama                       |     1
 Romantic Thriller           |     1
 Super Hero                  |     2
 Political Thriller          |     1
 Romantic Dark Fantasy Drama |     1
 Crime Thriller              |     1
 Neo Noir Mystery Thriller   |     1
 Science Fiction             |     7
 Dark Fantasy Horror         |     1
(10 rows)

class11=# -- use having to filter groups
class11=# select genre, count(*) from movie group by genre having count(*) > 1;
      genre      | count
-----------------+-------
 Super Hero      |     2
 Science Fiction |     7
(2 rows)

class11=# -- oh, btw, you can get file locations of your configs with this query
class11=# SELECT name, setting FROM pg_settings WHERE category = 'File Locations';
       name        |                 setting
-------------------+-----------------------------------------
 config_file       | /usr/local/var/postgres/postgresql.conf
 data_directory    | /usr/local/var/postgres
 external_pid_file |
 hba_file          | /usr/local/var/postgres/pg_hba.conf
 ident_file        | /usr/local/var/postgres/pg_ident.conf
(5 rows)

