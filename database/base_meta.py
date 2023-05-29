import configparser
import sqlalchemy.ext.declarative as dec
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import sessionmaker, Session

Base = dec.declarative_base()

__factory = None

config = configparser.ConfigParser()
config.read('config/config.ini')

database_host = config['database']['host']
database_port = config['database']['port']
database_username = config['database']['username']
database_password = config['database']['password']
database_name = config['database']['name']


def global_init(
        host=database_host, port=database_port, user=database_username, password=database_password,
        db_name=database_name
):
    global __factory

    if __factory:
        return

    connection_string = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    # connection_string = f'postgresql://VPirog:QqPWDom5p8sR@ep-green-sunset-942649.eu-central-1.aws.neon.tech/neondb'
    # print(f"Подключение к БД: {connection_string}")

    engine = sa.create_engine(connection_string, echo=0)
    # engine = sa.create_engine(connection_string)

    __factory = orm.sessionmaker(engine)


def create_session():
    return __factory()


connection_string = f'postgresql://{database_username}:{database_password}@{database_host}:{database_port}/{database_name}'
engine = sa.create_engine(connection_string, echo=0)
session_factory = sessionmaker(bind=engine,
                               expire_on_commit=False)


def get_session() -> Session:
    return session_factory()
