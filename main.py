import logging
from os import environ as env
from dotenv import load_dotenv

from get_token import get_access_token
from send_mail import send_email
from list_messages import list_all_messages

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send():
    # === Configure Email Details ===
    RECIPIENT_EMAIL = "recipient@yourdomain.com"
    CC_EMAILS = ["user1@yourdomain.com", "user2@yourdomain.com"]  # List of CC recipients
    SUBJECT = "🚀 Test Email with Multiple CCs"
    BODY = "Hello! This is a test email sent via Microsoft Graph API with multiple CC recipients."

    # Send Email
    send_email(access_token=get_access_token(), recipient=RECIPIENT_EMAIL, cc_list=CC_EMAILS, subject=SUBJECT, body=BODY)

def main():
    # === Send email ===
    # send()

    # === List messages ===
    messages = list_all_messages(get_access_token())
    print(messages)

if __name__ == "__main__":
    main()
