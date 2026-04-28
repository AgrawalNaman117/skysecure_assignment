import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    ZOHO_CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
    ZOHO_CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
    ZOHO_REDIRECT_URI = os.getenv("ZOHO_REDIRECT_URI")
    ZOHO_ACCOUNTS_URL = os.getenv("ZOHO_ACCOUNTS_URL")

    SESSION_SECRET = os.getenv("SESSION_SECRET", "supersecret")

settings = Settings()