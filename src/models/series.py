from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

class Series(Base):
    __tablename__ = "series"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    seasons_number: Mapped[int] = mapped_column(Integer, nullable=True)
    
    def __init__(self):
        from src.models.season import Season
        id_season:Mapped[list[Season]] = relationship("Season", back_populates="seasons.series_id")
        