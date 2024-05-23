import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_SECRET_KEY = os.getenv("PROJECT_SECRET_KEY")