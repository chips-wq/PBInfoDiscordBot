import bot.db as db
from bot.util import update_db
 
from bot.config import auth , BASE_DIR

db.c.execute("""DROP TABLE IF EXISTS githubfiles""")
db.c.execute("""
CREATE TABLE githubfiles (
    id integer primary key,
    name text,
    path text,
    path_to_raw text
)
""")

update_db(BASE_DIR , auth , db.c)

db.conn.commit()

db.conn.close()

