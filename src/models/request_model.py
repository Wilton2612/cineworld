from typing import NamedTuple, Optional


class Solicitud(NamedTuple):
    idservicio: Optional[int] = None
    email: Optional[str] = None
    nombre: Optional[str] = None
    telefono: Optional[int]= None
    informacion: Optional[str] = None
    servicioid: Optional[int] = None
    teatroid: Optional[int] = None
    