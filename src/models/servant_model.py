from typing import NamedTuple, Optional


class Servicio(NamedTuple):
    idservicio: Optional[int] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    condiciones: Optional[str] = None
    imagen: Optional[str] = None