from fastapi import APIRouter
from src.models.movie import Movie

from .schemas import NewMovie, NewMovieResponse, GetAllMoviesResponse, SelectedMovieIdResponse
from .services import MovieService

movie_router = APIRouter(prefix="/movies", tags=["Movies"])

@movie_router.post("/", status_code=201, response_model=NewMovieResponse)
async def add_movie(payload:NewMovie)->Movie:
    return MovieService.add_new_movie(payload=payload)

@movie_router.get("/", status_code=200, response_model=list[GetAllMoviesResponse])
async def get_all_movies() -> list[Movie]:
    return MovieService.get_all_movies()

@movie_router.get("/{id}", status_code=200, response_model=SelectedMovieIdResponse)
async def get_movie_from_id(id : int) -> Movie:
    return MovieService.get_movie_from_id(id)

@movie_router.delete("/{id}", status_code=200, response_model=None)
async def delete_movie_from_id(id : int)-> None:
    return MovieService.delete_movie_from_id(id)

@movie_router.post("/score/{id}", status_code=201, response_model=None)
async def score_movie_from_id(id : int, score : int) -> None:
    return MovieService.score_movie_from_id(id, score)