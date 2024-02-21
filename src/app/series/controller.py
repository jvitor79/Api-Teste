from fastapi import APIRouter
from .services import SeriesService
from .schemas import NewSeries, GetAllSeriesResponse, NewSeasonPayload, GetAllSeasonsResponse, NewEpisode, GetEpisodesResponse

from src.models.series import Series

series_router = APIRouter(prefix="/series", tags=["Series"])


@series_router.post("/", status_code=201, response_model=None)
async def add_new_series(payload:NewSeries)->None:
    return SeriesService.add_new_series(payload=payload)

@series_router.get("/", status_code=200, response_model=list[GetAllSeriesResponse])
async def get_all_series() -> list[dict]:
    return SeriesService.get_all_series()

@series_router.delete("/{id}", status_code=200, response_model=None)
async def delete_series(id:int) -> None:
    return SeriesService.delete_series(id)

@series_router.post("/season/{series_id}", status_code=201, response_model=None)
async def add_new_season(series_id:int, payload:NewSeasonPayload)->None:
    return SeriesService.add_new_season(series_id=series_id, payload=payload)

@series_router.get("/season/{series_id}", status_code=200, response_model=list[GetAllSeasonsResponse])
async def get_all_seasons(series_id:int)->list[dict]:
    return SeriesService.get_all_seasons(series_id)

@series_router.delete("/season/{season_id}", status_code=200, response_model=None)
async def remove_season(season_id:int)->None:
    return SeriesService.remove_season(season_id)

@series_router.post("/episode/{season_id}", status_code=201, response_model=None)
async def add_episode(season_id:int, payload:NewEpisode)->None:
    return SeriesService.add_episode(season_id=season_id, payload=payload)

@series_router.get("/episode/{season_id}", status_code=200, response_model=list[GetEpisodesResponse])
async def get_episodes(season_id:int)->list[dict]:
    return SeriesService.get_episodes(season_id)

@series_router.post("/episode/score/{ep_number}", status_code=201, response_model=None)
async def score_episode(ep_number:int, score:int)->None:
    return SeriesService.score_episode(ep_number=ep_number, score=score)

@series_router.delete("/episode/{ep_number}", status_code=200, response_model=None)
async def delete_episode(ep_number:int)->None:
    return SeriesService.delete_episode(ep_number)