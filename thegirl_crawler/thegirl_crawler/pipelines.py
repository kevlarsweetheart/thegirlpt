# -*- coding: utf-8 -*-

import sqlite3

from data_paths import THEGIRL_DB

from db_queries import (
    CREATE_TABLE,
    SELECT_URL,
    INSERT_INTO_TITLES,
)


class ThegirlCrawlerPipeline(object):
    def __init__(self):
        self.connection = sqlite3.connect(THEGIRL_DB)
        self.cursor = self.connection.cursor()

        self.cursor.execute(CREATE_TABLE)

    def process_item(self, item, spider):
        self.cursor.execute(SELECT_URL.format(item_url=item["url"]))
        (result, ) = self.cursor.fetchone()
        if result == 0:
            self.cursor.execute(INSERT_INTO_TITLES, (item["_id"], item["url"], item["title"], item["tags"]))
            self.connection.commit()
        return item
