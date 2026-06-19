import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Gemini API configuration
GEMINI_API_KEY = os.getenv("Your Gemini Key Here")
# App configuration
APP_TITLE = "AI-Powered Study Buddy"
APP_ICON = "📚"
