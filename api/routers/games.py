from fastapi import APIRouter, Depends, Query
from ..schemas.games import Game as GameSchema
from ..models.games import Game
from ..db import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from ..utils import logger


games_router = APIRouter()


@games_router.get('/games')
def get_games(release_year: Optional[int] = Query(None), db: Session = Depends(get_db)) -> List[GameSchema]:
    filters = []
    if release_year:
        filters.append(Game.release_year == release_year)
    try:
        return db.query(Game).filter(*filters).all()
    except Exception as e:
        logger.error('failed to get games from db', exc_info=e)
        raise e