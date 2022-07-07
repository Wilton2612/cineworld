from typing import NamedTuple, Optional


class Alimento(NamedTuple):
    idalimento: Optional[int] = None
    nombre1: Optional[str] = None
    precio1: Optional[str] = None
    idbebida: Optional[int] = None
    nombre2: Optional[str] = None
    precio2: Optional[str] = None

class Bebida(NamedTuple):
    idbebida: Optional[int] = None
    nombre: Optional[str] = None
    precio: Optional[str] = None
    