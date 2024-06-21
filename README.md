**Pokémon API**
================

This API provides information about Pokémon using data from PokeAPI.

**Installation**
---------------
git clone https://github.com/DilanRojasca/Pokemon-API.git cd Pokemon-API pip install -r requirements.txt uvicorn main:app --reload

The API will be available at [http://localhost:8000](http://localhost:8000).

**Usage**
-----

### Documentation

API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).

### Endpoints

* `/pokemon/{pokemon_id}`: Get detailed information about a specific Pokémon.
* `/pokemon/random`: Get information about a random Pokémon.
* `/pokemon/types/{type}`: Get a list of Pokémon that belong to a specific type.

**Contributions**
--------------

Contributions are welcome! Open an issue or send a pull request to contribute.

**License**
---------

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
