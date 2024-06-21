# Pokémon API

Esta API proporciona información sobre Pokémon utilizando datos de la PokeAPI.

## Instalación

1. Clona el repositorio:

   ```sh
   git clone https://github.com/DilanRojasca/Pokemon-API.git
Instala las dependencias:

sh

cd Pokemon-API
pip install -r requirements.txt
Inicia el servidor:

sh
uvicorn main:app --reload
La API estará disponible en http://localhost:8000.

##Uso
Documentación de la API: http://localhost:8000/docs
Endpoints:
/pokemon/{pokemon_id}: Obtiene información detallada sobre un Pokémon específico.
/pokemon/random: Obtiene información sobre un Pokémon aleatorio.
/pokemon/types/{type}: Obtiene una lista de Pokémon que pertenecen a un tipo específico.
Contribuciones
¡Las contribuciones son bienvenidas! Abre un issue o envía un pull request para contribuir.

##Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.


Este formato simplificado proporciona los pasos de instalación, uso, información sobre endpoints, cómo contribuir y la licencia en un formato más conciso y fácil de copiar y pegar en tu repositorio.
