from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

class Season(Base):
    __tablename__ = "seasons"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    series_id: Mapped[int] = mapped_column(Integer, ForeignKey("series.id"))
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    
    def __init__(self):
        from src.models.series import Series
        from src.models.episode import Episode
        
        series_title:Mapped[Series] = relationship("Series", back_populates="series.id")
        season_number:Mapped[list[Episode]] = relationship("Episode", foreign_keys="episodes.season")