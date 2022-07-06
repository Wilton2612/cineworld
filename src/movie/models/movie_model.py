from typing import NamedTuple, Optional


class Pelicula(NamedTuple):
    idpelicula: Optional[int] = None
    nombre: Optional[str] = None
    duracion: Optional[str] = None
    genero: Optional[int] = None
    descripcion: Optional[str] = None
    trailer: Optional[str] = None
    director: Optional[int] = None
    reparto: Optional[str] = None
    estreno: Optional[str] = None
    imagen: Optional[str] = None
