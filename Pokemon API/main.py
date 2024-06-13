from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(openapi_prefix="/pokemon")

class Pokemon(BaseModel):
    id: int
    name: str
    type: str

pokemonList = [
    Pokemon(id=1, name="Bulbasaur", type="Grass"),
    Pokemon(id=2, name="Ivysaur", type="Grass"),
    Pokemon(id=3, name="Venusaur", type="Grass"),
    Pokemon(id=4, name="Charmander", type="Fire"),
    Pokemon(id=5, name="Charmeleon", type="Fire"),
    Pokemon(id=6, name="Charizard", type="Fire"),
    Pokemon(id=7, name="Squirtle", type="Water"),
    Pokemon(id=8, name="Wartortle", type="Water"),
    Pokemon(id=9, name="Blastoise", type="Water"),
    Pokemon(id=10, name="Caterpie", type="Bug")
]

# Endpoint #1
@app.get("/", response_model=list[Pokemon])
async def get_pokemonList():
    return pokemonList

# Endpoint #2
@app.get("/{id}", response_model=Pokemon)
async def get_pokemon_id(id: int):
    pokemon = search_pokemon(id)
    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

# Endpoint #3
@app.post("/", response_model=Pokemon, status_code=201)
async def add_pokemon(pokemon: Pokemon):
    if search_pokemon(pokemon.id) is not None:
        raise HTTPException(status_code=409, detail="Pokemon already exists")
    pokemonList.append(pokemon)
    return pokemon

def search_pokemon(id: int):
    for poke in pokemonList:
        if poke.id == id:
            return poke
    return None