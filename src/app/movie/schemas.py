from pydantic import Field
from src.models.utils.schemas_base import SchemasBase

class NewMovie(SchemasBase):
    title: str = Field(description="Movie Title")
    duration: int = Field(description="Duration of the movie")
    category: str = Field(description="Category of the movie")
    
class NewMovieResponse(SchemasBase):
    id: int = Field(description="Id of the inserted movie")
    title: str = Field(description="Movie Title")
    duration: int = Field(description="Duration of the movie")
    category: str = Field(description="Category of the movie")

class SelectedMovieId(SchemasBase):
    id: int = Field(description="Id of the movie")
    
class SelectedMovieIdResponse(SchemasBase):
    id: int = Field(description="Id of the movie")
    title: str = Field(description="Title of the movie")
    duration: int = Field(description="Duration of the movie")
    category: str = Field(description="Category of the movie")
    score: int = Field(description="Score of the movie")
       

