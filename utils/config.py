import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')
