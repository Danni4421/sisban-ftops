import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    database = os.getenv('DB_DATABASE')

    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"
    SQLALCHEMY_TRACK_MODIFICATIONS=False