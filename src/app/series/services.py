from .schemas import NewSeries, NewSeasonPayload, NewEpisode
from src.models.series import Series
from src.models.season import Season
from src.models.episode import Episode
from src.database import db
from src.errors.exceptions import HTTPInternalException, NotFoundException
from sqlalchemy import insert

class SeriesService:
    def add_new_series(payload:NewSeries):
        try:
            stmt = insert(Series).values(seasons = 0, title = payload.title)
            db.execute(stmt)
            db.commit()
        except Exception as e:
            raise HTTPInternalException(f"Could not fetch series data - {e}")
        
    def get_all_series() -> list[dict]:
        try:
            response : list[dict] = []
            query = (db.query(Series.id, Series.title, Series.seasons_number))
            data = query.all()
            for serie in data:
                response.append(serie._asdict())
            return response
        except Exception as e:
            raise HTTPInternalException(f"Could not fetch series data - {e}")
    
    def delete_series(id):
        try:
            res = db.query(Series).filter(Series.id == id).delete()
            if not res:
                raise NotFoundException("Series not found")
            db.commit()
        except Exception as e:
            raise HTTPInternalException(f"Could not fetch series data - {e}")
    
    def add_new_season(series_id:int, payload:NewSeasonPayload):
        try:
            stmt = insert(Season).values(series_id = series_id, title = payload.title)
            db.execute(stmt)
            db.commit()
            db.query(Series).filter(Series.id == series_id).update({Series.seasons_number : Series.seasons_number + 1})
            db.commit()
        except Exception as e:
            raise HTTPInternalException(f"Could not fetch season data - {e}")
    
    def get_all_seasons(series_id:int)->list[dict]:
        try:
            response : list[dict] = []
            query = (db.query(Season.id, Season.series_id, Season.title).filter(Season.series_id == series_id))
            data = query.all()
            for season in data:
                response.append(season._asdict())
            return response
        except Exception as e:
            raise HTTPInternalException(f"Could not fetch season data - {e}")
        
    def remove_season(season_id: int):
        try:
            series_id = db.query(Season.series_id).filter(Season.id == season_id).first().tuple()
            res = db.query(Season).filter(Season.id == season_id).delete()
            if not res:
                raise NotFoundException("Season not found")
            db.commit()
            db.query(Series).filter(Series.id == series_id[0]).update({Series.seasons_number : Series.seasons_number - 1})
            db.commit()
        except Exception as e:
            raise HTTPInternalException(f"Could not delete season data - {e}")
    
    def add_episode(season_id: int, payload: NewEpisode):
        try:
            stmt = insert(Episode).values(title = payload.title, season = season_id, score = 0)
            db.execute(stmt)
            db.commit()
        except Exception as e:
            raise HTTPInternalException(f"Could not fecth episode data - {e}")
    
    def get_episodes(season_id)->list[dict]:
        try:
            response : list[dict] = []
            query = (db.query(Episode.ep_number, Episode.title, Episode.season, Episode.score))
            data = query.all()
            for episode in data:
                response.append(episode._asdict())
            return response
        except Exception as e:
            raise HTTPInternalException(f"Could not fecth episode data - {e}")
        
    def score_episode(ep_number, score):
        try:
            db.query(Episode).filter(Episode.ep_number == ep_number).update({Episode.score: score})
            db.commit()
        except Exception as e:
            raise HTTPInternalException(f"Could not fecth episode data - {e}")
    
    def delete_episode(ep_number):
        try:
            res = db.query(Episode).filter(Episode.ep_number == ep_number).delete()
            if not res:
                raise NotFoundException("Season not found")
            db.commit()
        except Exception as e:
            raise HTTPInternalException(f"Could not fecth episode data - {e}")
    