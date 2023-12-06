from fastapi import APIRouter
from src.app.series.services import SeriesService
from src.app.series.schemas import NewSeries, NewSeriesResponse

series_router = APIRouter(prefix="/series", tags=["Series"])


@series_router.post("/addseries", status_code=201, response_model=NewSeriesResponse)
async def addSeries(payload:NewSeries):
    return SeriesService.addNewSeries(payload=payload)