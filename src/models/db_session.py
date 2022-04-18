import sqlalchemy as sa
import sqlalchemy.orm as orm
from decouple import config
from sqlalchemy.orm import scoped_session


def db_init() -> scoped_session:
    print(f"Connecting to database")

    engine = sa.create_engine(
        "postgresql://{}:{}@{}:{}/{}".format(
            config('POSTGRES_USER'),
            config('POSTGRES_PASSWORD'),
            config('POSTGRES_HOST'),
            config('POSTGRES_PORT'),
            config('POSTGRES_DB')
        )
    )
    return orm.scoped_session(orm.sessionmaker(autocommit=False, autoflush=False, bind=engine))
