import _sqlite3

bd = _sqlite3.connect("2048.sqlite")

cur = bd.cursor()
cur.execute("""
create table if not exists RECORDS  (
    name text,
    score integer
)""")
cur.execute("""
SELECT name gamer, max(score) score FROM RECORDS
GROUP by name
ORDER by score DESC
LIMIT 3
""")

result = cur.fetchall()
print(result)
cur.close()