import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")

print("API key:", api_key)
print("Database URL:", database_url)
