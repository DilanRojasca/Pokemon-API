from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class Pokemon(BaseModel):
    id:int
    name:str
    type:str

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

#endpoint #1
@app.get("/pokemon/", response_model=list[Pokemon])
async def get_pokemon():
    return pokemonList

#Endpoint #2
@app.get("/pokemon/{id}")
async def get_pokemon_id(id:int):
    return search_pokemon(id)



def search_pokemon(id: int):
        pokes = filter(lambda pokemon: pokemon.id == id, pokemonList)
        try:   
            return list(pokes)[0]
        except:
             raise HTTPException(status_code=404, detail="pokemon not found")