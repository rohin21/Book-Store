from pydantic import PostgresDsn
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from config.setting import settings


postgres_url = PostgresDsn.build(scheme=settings.SCHEMA, user=settings.DB_USER, password=settings.DB_PASSWORD,
                                 host=settings.DB_HOST, path=f"/{settings.DB_PATH}", port=settings.DB_PORT)
print(postgres_url)

engine = create_engine(postgres_url)
session_factory = sessionmaker(autocommit=False,autoflush=True,bind=engine)
SessionLocal = scoped_session(session_factory=session_factory)