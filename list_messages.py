import requests, logging
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

user_email = env['SENDER_EMAIL']
LIST_ALL_MESSAGES_URL = f"https://graph.microsoft.com/v1.0/users/{user_email}/messages"

def list_all_messages(access_token):
    """Call Microsoft Graph API with the access token."""
    headers = {"Authorization": f"Bearer {access_token}"}
    try:
        response = requests.get(LIST_ALL_MESSAGES_URL, headers=headers)
        response.raise_for_status()
        logging.info("Successfully called Microsoft Graph API.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error calling Graph API: {e}")
        return None