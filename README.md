# Pokémon API

Este proyecto es una API desarrollada con FastAPI que proporciona información sobre Pokémon. La API está integrada con la PokeAPI para obtener datos actualizados y detallados sobre cada Pokémon.

## Instalación

Para utilizar esta API, primero asegúrate de tener Python instalado. Luego, clona este repositorio e instala las dependencias utilizando pip:

```bash
git clone https://github.com/DilanRojasca/Pokemon-API.git
cd Pokemon-API
pip install -r requirements.txt
Uso
Una vez instaladas las dependencias, puedes iniciar el servidor utilizando el siguiente comando:
bashCopyuvicorn main:app --reload
Esto iniciará el servidor en http://localhost:8000. Puedes acceder a la documentación interactiva de la API en http://localhost:8000/docs para ver los endpoints disponibles y probarlos directamente desde tu navegador.
Endpoints

/pokemon/{pokemon_id}: Obtiene información detallada sobre un Pokémon específico.
/pokemon/random: Obtiene información sobre un Pokémon aleatorio.
/pokemon/types/{type}: Obtiene una lista de Pokémon que pertenecen a un tipo específico.

Contribuciones
¡Las contribuciones son bienvenidas! Si quieres contribuir a este proyecto, por favor abre un issue o envía un pull request.
Licencia
Este proyecto está bajo la Licencia MIT. Para más información, por favor lee el archivo LICENSE.
