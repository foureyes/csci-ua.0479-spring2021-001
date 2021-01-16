import psycopg2
conn = psycopg2.connect(dbname="scratch", user="joe", password="data0480")
cur = conn.cursor()
cur.execute("select * from artist where name ilike  '%cory arcangel%'")
# our query as a string...
q = """
SELECT *
FROM artist
WHERE nationality = 'American'
	AND gender = 'Female'
	AND name ilike 'Z%';
"""
"""
cur.execute(q)
result = cur.fetchall()
"""

q = "insert into artist (artist_id, name, bio) values (123456, 'joe v', 'i am not an artist')"

cur.execute(q)

q = "select * from artist where artist_id = 123456"

conn.commit()

cur.execute(q)
result = cur.fetchall()
print(result)
"""
for a in  cur:
    print(a)
"""









