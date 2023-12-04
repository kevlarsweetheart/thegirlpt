CREATE_TABLE = """CREATE TABLE IF NOT EXISTS titles (_id text PRIMARY KEY,
                                                     url text,
                                                     title text,
                                                     tags text);"""

SELECT_URL = "SELECT COUNT(*) FROM titles WHERE url = '{item_url}';"

INSERT_INTO_TITLES = """INSERT INTO titles (_id, url, title, tags) VALUES (?, ?, ?, ?);"""
