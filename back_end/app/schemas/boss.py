from typing import Optional

from pydantic import BaseModel


class Boss(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    Saúde: Optional[float] = None
    Defesa: Optional[float] = None
    Postura: Optional[float] = None
    Resistencia: Optional[str] = None
    Fraqueza: Optional[str] = None
    Recompensa: Optional[str] = None
    image: Optional[str] = None