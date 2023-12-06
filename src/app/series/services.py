from src.app.series.schemas import NewSeries
from src.models.series import Series
from src.database import db

class SeriesService:
    def addNewSeries(payload:NewSeries):
        data = Series(**payload.model_dump())
        db.add(data)
        db.commit()
        db.refresh(data)
        return data
        
        