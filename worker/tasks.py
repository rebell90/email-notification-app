from celery_app import celery
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from dotenv import load_dotenv

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")

@celery.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 3})
def send_email(self, to_email: str, name: str):
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject="Welcome!",
        html_content=f"<strong>Hello {name},</strong><br>Thanks for signing up!"
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"Email sent to {to_email}, status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
        raise e
