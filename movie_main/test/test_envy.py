import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

# Print the result
if api_key:
    print("Loaded API key:", api_key[:20] + "..." if len(api_key) > 20 else api_key)
else:
    print("API key not found in .env file.")
