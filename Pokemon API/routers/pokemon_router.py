from fastapi import APIRouter
from models import models
from services.pokemon_service import PokemonService

router = APIRouter(prefix="/pokemon",
                   tags=["Pokemon"],
                   responses={404:{"message":"not found"}})

pokemon_services = PokemonService()

@router.get("/", summary="Obtener una lista de Pokémon")
async def get_pokemonList(offset: int = 0, limit:int = 10):
    pokemon_list = pokemon_services.get_pokemon_list(offset, limit)
    return pokemon_list

@router.get("/{id}", summary="obtener un pokemon por medio del ID")
async def get_pokemon_id(id: int):
    pokemon = pokemon_services.get_pokemon_by_id(id)
    return pokemon

# Endpoint #3
@router.post("/", summary="Agregar un nuevo pokemon")
async def add_pokemon(pokemon: models.Pokemon):
    new_pokemon = pokemon_services.add_new_pokemon(pokemon)
    return new_pokemon
