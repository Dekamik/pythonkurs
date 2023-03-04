"""

"""


import logging
import sqlite3


logger = logging.getLogger(__name__)


_create_data_table = """CREATE TABLE IF NOT EXISTS people (
id integer PRIMARY KEY,
name text NOT NULL,
email text NOT NULL,
phone text
);"""

_insert_into_people = """INSERT INTO people (name, email, phone) VALUES (?, ?, ?);"""

_select_all_from_people = """SELECT * FROM people;"""


class ViatiDAO:
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
            c.execute(_create_data_table)

            return conn

        except sqlite3.Error as e:
            logger.error("error when connecting to db at %s", db_file)
            if conn:
                conn.close()
            raise e

    def get_all_people(self) -> list:
        try:
            c = self.conn.cursor()
            c.execute(_select_all_from_people)
            return c.fetchall()
        except sqlite3.Error as e:
            logger.error("error selecting all people from db")
            raise e

    def add_person(self, name, email, phone=None):
        try:
            c = self.conn.cursor()
            c.execute(_insert_into_people, (name, email, phone))
            self.conn.commit()
        except sqlite3.Error as e:
            logger.error("error inserting people to db")
            raise e
