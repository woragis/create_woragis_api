import smtplib

from email.mime.text import MIMEText

from app.core.config import settings


def send_email(subject: str, to_email: str, body: str):
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = "noreply@woragis.com"
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("your_email@gmail.com", "your_password")
            server.send_message(msg)
        return True
    except Exception as e:
        print("Failed to send email:", e)
        return False
