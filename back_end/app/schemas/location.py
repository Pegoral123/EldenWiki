from pydantic import BaseModel


class Location(BaseModel):
    Local: str
    SubTitulo: str
    Descricao: str