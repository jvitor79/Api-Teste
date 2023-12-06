from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class Movie(Base):
    __tablename__ = "movies"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    duration: Mapped[int] = mapped_column(Integer, nullable=False)
    category: Mapped[str] = mapped_column(String(128), nullable=False)
    score: Mapped[int] = mapped_column(Integer, nullable=False)
    