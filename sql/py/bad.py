import psycopg2

conn = psycopg2.connect(dbname="class20", user="jversoza")
cur = conn.cursor()

artist_name = input('Give me an artist name to search for\n> ')
q = f"select * from artist where name ilike '%{artist_name}%'"

cur.execute(q)
for row in cur:
    print(row)
