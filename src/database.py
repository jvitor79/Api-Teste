from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from src.constants import POSTGRES_DATABASE_URI

postgresDbEngine = create_engine(url=POSTGRES_DATABASE_URI, echo=False)

postgresDbSession = sessionmaker(bind=postgresDbEngine, autoflush=False, autocommit=False)
db = scoped_session(postgresDbSession)

Base = declarative_base()
Base.query = db.query_property()

