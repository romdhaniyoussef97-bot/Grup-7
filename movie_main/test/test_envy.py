import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("API_KEY")

# Print the result
if api_key:
    print("Loaded API key:", api_key[:20] + "..." if len(api_key) > 20 else api_key)
else:
    print("API key not found in .env file.")
