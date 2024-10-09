import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_SECRET_KEY = os.getenv("PROJECT_SECRET_KEY")
PROJECT_DEBUG = os.getenv("PROJECT_DEBUG")

PROJECT_EMAIL_HOST_USER = os.getenv("PROJECT_EMAIL_HOST_USER")
PROJECT_EMAIL_HOST_PASSWORD = os.getenv("PROJECT_EMAIL_HOST_PASSWORD")

PROJECT_DOMAIN_NAME = os.getenv("PROJECT_DOMAIN_NAME")

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_OPTIONS = os.getenv("DB_OPTIONS")
