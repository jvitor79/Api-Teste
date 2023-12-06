from src.models.utils.schemas_base import SchemasBase
from pydantic import Field

class NewSeries(SchemasBase):
    title:str = Field(description="title of the new series")
    
class NewSeriesResponse(SchemasBase):
    id: int = Field(description="id of the new series")
    title: str = Field(description="title of the new series")
    seasons: int = Field(description="number of seasons of the new series")