from src.app.movie.schemas import NewMovie
from src.models.movie import Movie
from src.database import db

from sqlalchemy.orm.exc import NoResultFound
from src.errors.exceptions import HTTPInternalException, NotFoundException

class MovieService:
    def add_new_movie(payload: NewMovie):
        try:
            data = Movie(**payload.model_dump())
            db.add(data)
            db.commit()
            db.refresh(data)
            return data
        except Exception as e:
            raise HTTPInternalException(f"Could not fetch movie data - {e}")
    
    def get_all_movies() -> list[Movie]:
        try:
            data = db.query(Movie).all()
            return data
        except Exception as e:
            raise HTTPInternalException(f"Could not fetch movie data - {e}")
    
    def get_movie_from_id(id : int):
        try:
            return db.query(Movie).filter(Movie.id == id).one()
        except NoResultFound as err:
            raise NotFoundException("Movie not found") from err
        except Exception as e:
            raise HTTPInternalException(f"Could not fetch movie data - {e}")
        
    def delete_movie_from_id(id : int):
        try:
            res = db.query(Movie).filter(Movie.id == id).delete()
            if not res:
                raise NotFoundException("Movie not found")
            db.commit()
        except Exception as e:
            raise HTTPInternalException(f"Could not fetch movie data - {e}")
        
    def score_movie_from_id(id : int, score : int):
        try:
            db.query(Movie).filter(Movie.id == id).update({Movie.score : score})
            db.commit()
        except Exception as e:
            raise HTTPInternalException(f"Could not fetch movie data - {e}")
            
        
        
