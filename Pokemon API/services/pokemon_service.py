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

    def get_pokemon_by_id(self, id:int):
        url = f"{self.base_url}/{id}"
        return self.get_pokemon_details(url)

    def add_new_pokemon(self, pokemon: Pokemon):
        # PokeAPI npo admite solicitudes post
        raise HTTPException(status_code=405, detail="Method not allowed")
    
    def update_pokemon(self, id:  int, pokemon_data:Pokemon):
        # PokeAPI no tiene soporte para PUT
        url = f"{self.base_url}/{id}"
        response = requests.get(url)

        if response.status_code == 404:
            raise HTTPException(status_code=404, detail= "Pokemon not found")
        
        existing_pokemon = self.get_pokemon_details(url)
        updated_pokemon = pokemon_data.dict(exclude_unset=True)
        updated_pokemon = {**existing_pokemon.dict(), **updated_pokemon}

        response = requests.put(url, json=updated_pokemon)

        if response.status_code == 200:
            return Pokemon(**response.json())
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

    def update_pokemon_patch(self, id: int, data: Pokemon):
        # PokeAPI no tiene soporte para PATCH
        url = f"{self.base_url}/{id}"
        response = requests.get(url)
        
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        
        existing_pokemon = self.get_pokemon_details(url)
        updated_pokemon = updated_pokemon = data.__dict__
        updated_pokemon = {**existing_pokemon.dict(), **updated_pokemon}

        if response.status_code == 200:
            return Pokemon(**response.json())
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
    def delete_pokemon(self, id:int):
        url = f"{self.base_url}/{id}"
        response = requests.get(url)

        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Pokemon not found")

        if response.status_code == 200:
            response = requests.delete(url)
            if response.status_code == 204:
                return {"message": f"Pokemon {id} deleted successfully"}
            else:
                raise HTTPException(status_code=response.status_code, detail=response.text)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
