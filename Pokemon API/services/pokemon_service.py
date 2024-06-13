from models.pokemon import Pokemon
import requests

class PokemonService:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon"

    def get_pokemon_list(self, offset=0, limit=10):
        url = f"{self.base_url}?offset={offset}&limit={limit}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            pokemon_list = []
            for pokemon in data["results"]:
                pokemon_data = requests.get(pokemon["url"]).json()
                pokemon_list.append(Pokemon(
                    id=pokemon_data["id"],
                    name=pokemon_data["name"],
                    type=pokemon_data["types"][0]["type"]["name"]
                ))
            return pokemon_list
        else:
            return []

    def get_pokemon_by_id(self, id):
        url = f"{self.base_url}/{id}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return Pokemon(
                id=data["id"],
                name=data["name"],
                type=data["types"][0]["type"]["name"]
            )
        else:
            return None