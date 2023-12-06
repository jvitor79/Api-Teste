from pydantic import BaseModel, ConfigDict

class SchemasBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)