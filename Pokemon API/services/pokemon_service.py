import requests
from fastapi import HTTPException
from models.models import Pokemon

class PokemonService:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon"

    def get_pokemon_list(self, offset=0, limit=10):
        url = f"{self.base_url}?offset={offset}&limit={limit}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            pokemon_list = []
            for pokemon_data in data["results"]:
                pokemon_url = pokemon_data["url"]
                pokemon = self.get_pokemon_details(pokemon_url)
                pokemon_list.append(pokemon)
            return pokemon_list
        else:
            raise HTTPException(status_code=404, detail="No se encontraron Pokémon")

    def get_pokemon_details(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return Pokemon(
                id=data["id"],
                name=data["name"],
                base_experience=data["base_experience"],
                height=data["height"],
                weight=data["weight"],
                is_default=data["is_default"],
                order=data["order"],
                abilities=data["abilities"],
                types=data["types"],
                stats=data["stats"],
                sprites=data["sprites"]
            )
        else:
            raise HTTPException(status_code=404, detail="Pokemon not found")

    def get_pokemon_by_id(self, id):
        url = f"{self.base_url}/{id}"
        return self.get_pokemon_details(url)

    def add_new_pokemon(self, pokemon: Pokemon):
        raise HTTPException(status_code=405, detail="Method not allowed")