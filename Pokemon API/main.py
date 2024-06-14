# main.py
from fastapi import FastAPI
from routers import pokemon_router

app = FastAPI(
    title="Pokémon API",
    description="Una API RESTful para acceder a información detallada de Pokémon",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(pokemon_router.router)
