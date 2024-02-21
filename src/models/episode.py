from sqlalchemy import String, Integer 
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Episode(Base):
    __tablename__ = 'episodes'
    
    ep_number: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    season: Mapped[int] = mapped_column(Integer, ForeignKey("seasons.id"))
    score: Mapped[int] = mapped_column(Integer, nullable=True)
    
    def __init__(self):
        from src.models.season import Season
        seasons_relationship:Mapped[Season] = relationship("Season", back_populates="seasons.id")