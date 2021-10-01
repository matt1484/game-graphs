from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import POSTGRES_DB, POSTGRES_PORT, POSTGRES_PASSWORD, POSTGRES_USER, POSTGRES_HOST

engine = create_engine(
    f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}',
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()