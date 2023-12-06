from fastapi import APIRouter
from src.models.movie import Movie
from src.app.movie.schemas import NewMovie, NewMovieResponse, SelectedMovieId, SelectedMovieIdResponse
from src.app.movie.services import MovieService

movie_router = APIRouter(prefix="/movies", tags=["Movies"])

@movie_router.post("/addmovie", status_code=201, response_model=NewMovieResponse)
async def add_movie(payload:NewMovie)->Movie:
    return MovieService.add_new_movie(payload=payload)

@movie_router.post("/getmoviefromid", status_code=200, response_model=SelectedMovieIdResponse)
async def get_movie_from_id(payload:SelectedMovieId)->Movie:
    return MovieService.get_movie_from_id(payload=payload)

@movie_router.delete("/deletemoviefromid", status_code=200, response_model=None)
async def delete_movie_from_id(payload:SelectedMovieId)->None:
    return MovieService.delete_movie_from_id(payload=payload)