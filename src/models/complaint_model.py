from typing import NamedTuple, Optional


class Contacto(NamedTuple):
    idqueja: Optional[int] = None
    email: Optional[str] = None
    nombre: Optional[str] = None
    tipocomentario: Optional[str] = None
    comentario: Optional[str] = None
    teatroid: Optional[int] = None
    