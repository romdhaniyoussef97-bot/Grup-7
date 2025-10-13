import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
print("Loaded API key:", api_key[:20] + "..." if api_key else "Not found!")
