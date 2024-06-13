from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from routers import pokemon_router

app = FastAPI()

app.include_router(pokemon_router.router)

