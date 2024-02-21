from src.models.utils.schemas_base import SchemasBase
from pydantic import Field

class NewSeries(SchemasBase):
    title:str = Field(description="title of the new series")
    
class NewSeriesResponse(SchemasBase):
    id: int = Field(description="id of the new series")
    title: str = Field(description="title of the new series")
    seasons_number: int = Field(description="number of seasons")

class GetAllSeriesResponse(SchemasBase):
    id: int = Field(description="id of the series")
    title: str =Field(description="title of the series")
    seasons_number: int = Field(description="number of seasons")

class NewSeasonPayload(SchemasBase):
    title : str = Field(description="title of the new season")

class NewSeasonResponse(SchemasBase):
    id: int = Field(description="id of the season")
    series_id: int = Field(description="id of the series")
    title: str =Field(description="title of the season")
    
class GetAllSeasonsResponse(SchemasBase):
    id: int = Field(description="id of the season")
    series_id: int = Field(description="id of the series")
    title: str = Field(description="title of the season")

class NewEpisode(SchemasBase):
    title: str = Field(description="title of the episode")
    
class GetEpisodesResponse(SchemasBase):
    ep_number: int = Field("id of the episode")
    title: str = Field("title of the episode")
    season: int = Field("season id")
    score: int = Field("score of the episode")
    
    