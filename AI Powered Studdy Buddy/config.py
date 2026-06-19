import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Gemini API configuration
GEMINI_API_KEY = os.getenv("AQ.Ab8RN6JJP6Kgmi0jWTmhI2qEC9tt8JRVQIhoL3f0HShhFZ1nPg")
# App configuration
APP_TITLE = "AI-Powered Study Buddy"
APP_ICON = "📚"