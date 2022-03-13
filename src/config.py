from os import environ

class DB_CONFIG:
    HOST = environ.get('DB_HOST', 'localhost')
    PORT = environ.get('DB_PORT', '5432')
    USER = environ.get('DB_USER', 'postgres')
    PASSWORD = environ.get('DB_PASSWORD', 'admin')
    DATABASE = environ.get('DB_DATABASE', 'postgres')