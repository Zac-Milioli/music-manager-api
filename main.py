"""Arquivo inicializador. Define as rotas e faz as conexões entre as funções"""

import uvicorn
from fastapi import FastAPI
from src.routes.music_routes import router as music_router
from src.routes.database_routes import router as database_router

app = FastAPI()

app.include_router(router=music_router)
app.include_router(router=database_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
