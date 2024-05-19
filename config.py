import os
from dotenv import load_dotenv

if os.environ.get("FLASK_ENV") == "production":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env")


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
