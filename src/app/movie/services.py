from src.app.movie.schemas import NewMovie, SelectedMovieId
from src.models.movie import Movie
from src.database import db

from sqlalchemy.orm.exc import NoResultFound
from src.errors.exceptions import NotFoundException

class MovieService:
    def add_new_movie(payload: NewMovie):
        data = Movie(**payload.model_dump())
        db.add(data)
        db.commit()
        db.refresh(data)
        return data
    
    def get_movie_from_id(payload: SelectedMovieId):
        try:
            movie = db.query(Movie).filter(Movie.id == payload.id).one()
        except NoResultFound as err:
            raise NotFoundException("Movie not found") from err
        if not movie.score:
            movie.score = -1
        return movie
    
    def delete_movie_from_id(payload: SelectedMovieId):
        res = db.query(Movie).filter(Movie.id == payload.id).delete()
        if not res:
            raise NotFoundException("Movie not found")
        db.commit()
        
        
