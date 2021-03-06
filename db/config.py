import psycopg2
from psycopg2.extras import RealDictCursor
import os

class DatabaseConnection:
    def __init__(self):

        if os.getenv('db_name') == 'devdb':
            self.db_name = 'devdb'
        else:
            self.db_name = 'testdb'
        try:
            self.connection = psycopg2.connect(
                dbname='ddpf9sqg4pc57d', user='uqmrwwmueeojmn', host='ec2-54-227-246-152.compute-1.amazonaws.com', password='7ebe323427be80bac4333f001b92fb070aaf7fd31c686af37fea9a1413a92c0d', port=5432
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
