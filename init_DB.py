import bot.db as db
from bot.util import update_db

"""

```lua
print('Hello, World!')```

gives this (note that the language must be on the same line as the 3 initial backticks, with no other characters following it [including whitespace]).
"""   
from bot.config import auth , BASE_DIR

            

"""
db.c.execute("DROP TABLE githubfiles;")
"""
db.c.execute("""
CREATE TABLE IF NOT EXISTS githubfiles (
    id integer primary key,
    name text,
    path text,
    path_to_raw text
)
""")

update_db(BASE_DIR , auth , db.c)

db.conn.commit()

db.conn.close()

