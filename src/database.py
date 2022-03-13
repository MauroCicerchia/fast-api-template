from peewee import *
from config import DB_CONFIG

database = PostgresqlDatabase(
    host=DB_CONFIG.HOST,
    port=DB_CONFIG.PORT,
    database=DB_CONFIG.DATABASE,
    user=DB_CONFIG.USER,
    password=DB_CONFIG.PASSWORD
)


def db_startup():
    if database.is_closed():
        database.connect()


def db_shutdown():
    if not database.is_closed():
        database.close()
