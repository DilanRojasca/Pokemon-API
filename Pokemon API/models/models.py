from pydantic import BaseModel, Field
from typing import Optional

class Pokemon(BaseModel):
    """
    Representa un Pokémon
    """
    id: int = Field(..., description="El identificador único del Pokémon")
    name: str = Field(..., description="El nombre del Pokémon")
    base_experience: int = Field(..., description="La experiencia base del Pokémon")
    height: int = Field(..., description="La altura del Pokémon en metros")
    weight: int = Field(..., description="El peso del Pokémon en kilogramos")
    is_default: bool = Field(..., description="Indica si este es el Pokémon por defecto")
    order: int = Field(..., description="El orden del Pokémon en la Pokédex")
    sprites: Optional[dict] = Field(None, description="Sprites del Pokémon (opcional)")