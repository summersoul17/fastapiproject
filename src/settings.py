from os import environ
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = environ.get("POSTGRES_DB")
POSTGRES_HOST = environ.get("POSTGRES_HOST")
