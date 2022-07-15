from typing import NamedTuple, Optional


class Pelicula(NamedTuple):
    idpelicula: Optional[int] = None
    nombre: Optional[str] = None
    duracion: Optional[int] = None
    genero: Optional[str] = None
    descripcion: Optional[str] = None
    trailer: Optional[str] = None
    director: Optional[str] = None
    reparto: Optional[str] = None
    estreno: Optional[str] = None
    imagen: Optional[str] = None


class Horario(NamedTuple):
    idhorario: Optional[int] = None
    hora: Optional[str] = None