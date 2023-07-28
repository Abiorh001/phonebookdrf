from .base_settings import *
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USERNAME"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

SECRET_KEY = os.getenv("SECRET_KEY")
