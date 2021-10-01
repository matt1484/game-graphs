from sqlalchemy import Column, Integer, String, Float
from . import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    platform = Column(String)
    release_year = Column(Integer)
    genre = Column(String)
    publisher = Column(String)
    na_sales = Column(Float)
    eu_sales = Column(Float)
    jp_sales = Column(Float)
    other_sales = Column(Float)
