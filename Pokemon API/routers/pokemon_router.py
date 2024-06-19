from fastapi import APIRouter, Path
from models import Pokemon
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


@router.post("/", summary="Agregar un nuevo pokemon")
async def add_pokemon(pokemon: Pokemon):
    new_pokemon = pokemon_services.add_new_pokemon(pokemon)
    return new_pokemon


@router.put("/{id}", response_model= Pokemon, summary="Actualiza la informacion de un pokemon")
async def update_pokemon_endpoint(id: int, pokemon_data: Pokemon):
    return pokemon_services.update_pokemon(id, pokemon_data)

@router.patch("/{id}",response_model=Pokemon, summary="Actualiza en especifico la informacion del pokemon")
async def update_pokemon_patch(id : int , pokemon_data = Pokemon):
    return pokemon_services.update_pokemon_patch(id, pokemon_data)

@router.delete("/{id}", response_model=Pokemon, summary= "Opcion para eleminar un  Pokemon")
async def delete_pokemon(id:int):
    return pokemon_services.delete_pokemon(id)