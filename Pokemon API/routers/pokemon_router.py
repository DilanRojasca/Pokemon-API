from fastapi import APIRouter, HTTPException
from models.pokemon import Pokemon
from services.pokemon_service import PokemonService

router = APIRouter(prefix="/pokemon",
                   tags=["Pokemon"],
                   responses={404:{"message":"not found"}})

pokemon_services = PokemonService()

@router.get("/", response_model=list[Pokemon])
async def get_pokemonList():
    return pokemon_services.get_pokemon_list()

@router.get("/{id}", response_model=Pokemon)
async def get_pokemon_id(id: int):
    pokemon = pokemon_services.get_pokemon_by_id(id)
    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

# Endpoint #3
@router.post("/", response_model=Pokemon, status_code=201)
async def add_pokemon(pokemon: Pokemon):
    existing_pokemon = pokemon_services.get_pokemon_by_id(pokemon.id)
    if existing_pokemon:
        raise HTTPException(status_code=409, detail="Pokemon already exists")
    new_pokemon = pokemon_services.add_new_pokemon(pokemon)
    if new_pokemon is None:
        raise HTTPException(status_code=500, detail="Failed to add new Pokemon")
    return new_pokemon
