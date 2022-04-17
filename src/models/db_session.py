import sqlalchemy as sa
import sqlalchemy.orm as orm
from decouple import config

factory = None


def global_init() -> None:
    global factory

    if factory:
        return

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
    factory = orm.sessionmaker(bind=engine)
