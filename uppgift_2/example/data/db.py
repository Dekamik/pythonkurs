"""

"""


import logging
import sqlite3


logger = logging.getLogger(__name__)


_create_channels_table = """CREATE TABLE IF NOT EXISTS channels (
id integer PRIMARY KEY,
name text NOT NULL,
ext_id integer NOT NULL,
type text NOT NULL,
url text NOT NULL
);"""

_insert_into_channels = """INSERT INTO channels (name, ext_id, type, url) VALUES (?, ?, ?, ?);"""

_select_all_from_channels = """SELECT * FROM channels;"""


class SverigesRadioDAO:
    def __init__(self, db_file: str):
        self.db_file = db_file

    def __enter__(self):
        self.conn: sqlite3.Connection = self._create_connection(self.db_file)
        return self

    def __exit__(self, *args):
        self.conn.close()

    def _create_connection(self, db_file) -> sqlite3.Connection:
        logger.debug("connecting to db at %s...", db_file)
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            logger.debug("connected")

            c = conn.cursor()
            c.execute(_create_channels_table)

            return conn

        except sqlite3.Error:
            logger.error("error when connecting to db at %s", db_file)
            if conn:
                conn.close()
            raise

    def get_all_channels(self) -> list:
        try:
            c = self.conn.cursor()
            c.execute(_select_all_from_channels)
            return c.fetchall()
        except sqlite3.Error:
            logger.error("error selecting all people from db")
            raise

    def add_channel(self, name: str, ext_id: int, type: str, url: str):
        try:
            c = self.conn.cursor()
            c.execute(_insert_into_channels, (name, ext_id, type, url))
            self.conn.commit()
        except sqlite3.Error:
            logger.error("error inserting channel into db")
            raise
