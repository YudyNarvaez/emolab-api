import datetime

from sqlalchemy.orm import registry

mapper_registry = registry()


class Base:
    pass


def now(context):
    return datetime.datetime.now(tz=datetime.timezone.utc)
