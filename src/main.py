from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.app.movie.controller import movie_router
from src.app.series.controller import series_router

app = FastAPI(
    title="Api de Filmes e Series", 
    description="Api para armazenar uma coleção de filmes e series, sendo possível avalia-las"
)

@app.get("/", status_code=200)
async def redirect_docs():
    return RedirectResponse("/docs")

app.include_router(movie_router)
app.include_router(series_router)
