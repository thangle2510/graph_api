import requests, logging
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Azure AD Credentials
TENANT_ID = env["TENANT_ID"]
CLIENT_ID = env['CLIENT_ID']
CLIENT_SECRET = env['CLIENT_SECRET']
TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

def get_access_token():
    """Retrieve an access token using client credentials."""
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "https://graph.microsoft.com/.default",
        "grant_type": "client_credentials",
    }
    
    try:
        response = requests.post(TOKEN_URL, data=payload)
        response.raise_for_status()
        token_data = response.json()
        logging.info("Successfully retrieved access token.")
        return token_data["access_token"]
    except requests.exceptions.RequestException as e:
        logging.error(f"Error retrieving access token: {e}")
        return None