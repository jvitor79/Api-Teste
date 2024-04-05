from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")

POSTGRES_DATABASE_URI = getenv("POSTGRES_DATABASE_URI")
