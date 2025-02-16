import requests, json
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = env['SENDER_EMAIL']

SEND_MAIL_URL = f"https://graph.microsoft.com/v1.0/users/{SENDER_EMAIL}/sendMail"

def send_email(access_token, recipient, cc_list, subject, body):
    """Send an email with multiple CC recipients using Microsoft Graph API."""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    # Format CC recipients
    cc_recipients = [{"emailAddress": {"address": email}} for email in cc_list] if cc_list else []

    email_payload = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "Text",
                "content": body
            },
            "toRecipients": [{"emailAddress": {"address": recipient}}],
            "ccRecipients": cc_recipients
        }
    }

    response = requests.post(SEND_MAIL_URL, headers=headers, data=json.dumps(email_payload))

    if response.status_code == 202:
        print("✅ Email sent successfully!")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")
