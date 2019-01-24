import psycopg2
from psycopg2.extras import RealDictCursor
import os

class DatabaseConnection:
    def __init__(self):

        if os.getenv('DB_NAME') == 'devdb':
            self.db_name = 'devdb'
        else:
            self.db_name = 'testdb'

        print(self.db_name)

        try:
            self.connection = psycopg2.connect(
                dbname=self.db_name, user='james', host='localhost', password='postgres', port=5432
            )
            self.connection.autocommit = True
            self.cur = self.connection.cursor(cursor_factory=RealDictCursor)

            print('Connected to the database successfully.')

            create_tables =   """
                CREATE TABLE IF NOT EXISTS users(
                    id SERIAL PRIMARY KEY NOT NULL,
                    firstname VARCHAR NOT NULL,
                    lastname VARCHAR NOT NULL,
                    othernames VARCHAR NOT NULL,
                    email VARCHAR NOT NULL,
                    phoneNumber VARCHAR NOT NULL,
                    username VARCHAR NOT NULL,
                    password VARCHAR NOT NULL,
                    registered  TIMESTAMP WITHOUT TIME ZONE,
                    isAdmin BOOLEAN
                    );

                CREATE TABLE IF NOT EXISTS incidents(
                    id SERIAL PRIMARY KEY NOT NULL,
                    createdOn  TIMESTAMP WITHOUT TIME ZONE,
                    createdBy INT REFERENCES users(id),
                    type VARCHAR NOT NULL,
                    title VARCHAR NOT NULL,
                    location VARCHAR NOT NULL,
                    status VARCHAR NOT NULL,
                    Images VARCHAR NOT NULL,
                    Videos VARCHAR NOT NULL,
                    comment VARCHAR NOT NULL
                    );

          """

            self.cur.execute(create_tables)
        except Exception as e:
            print(e)
            print('Failed to connect to the database.')
