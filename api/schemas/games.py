from pydantic import BaseModel


class Game(BaseModel):
    title: str = ...
    platform: str = ...
    release_year: int = ...
    genre: str = ...
    publisher: str = ...
    na_sales: float = ...
    eu_sales: float = ...
    jp_sales: float = ...
    other_sales: float = ...

    class Config:
        orm_mode = True
