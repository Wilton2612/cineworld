from typing import List
from ..models.theater_model import Teatro
from ..database import theater_db


def lista_teatros() -> List[Teatro]:
    return theater_db.list_all()