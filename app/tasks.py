from app.celery_app import celery
from app.config import settings
import smtplib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@celery.task
def send_reset_email(email: str, token: str):
    # send email logic here
    sender_email = settings.sender_email
    email_host = settings.email_host
    email_port = settings.email_port
    email_host_user = settings.email_host_user
    email_host_password = settings.email_host_password
    message = f"""Subject: Password Reset Request
    To reset your password, use the following token: {token}
    """
    logging.info(f"Preparing to send reset email to {email} with token {token}")
    logging.info(f"Email host: {email_host}, port: {email_port}, user: {email_host_user}, sender: {sender_email}")
    try:
        with smtplib.SMTP(email_host, email_port) as server:
                server.starttls()
                server.login(email_host_user, email_host_password)
                server.sendmail(sender_email, email, message)
        logger.info(f"Sending reset email to {email} with token {token}")
    except Exception as e:
        logger.error(f"Failed to send reset email to {email}: {e}")