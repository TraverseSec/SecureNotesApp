from dotenv import load_dotenv
import os

load_dotenv()


APP_NAME = os.getenv("APP_NAME", "Secure Notes")
raw_database_url = "sqlite:///./secure_notes.db"
DATABASE_URL = os.getenv("DATABASE_URL")

if not raw_database_url:
    raise ValueError("No Database URL Found")

DATABASE_URL = raw_database_url