from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import scoped_session

from .session import SessionLocal


@as_declarative()
class Base:
    uuid: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

   
Base.query = scoped_session(SessionLocal).query_property()