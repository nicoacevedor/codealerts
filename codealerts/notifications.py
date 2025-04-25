import smtplib
from email.mime.text import MIMEText
from typing import Any, Callable


def send_email(subject: str, body: str) -> None:
    from_email = "nacevedo@meteodata.cl"
    from_password = "bdnu lelu vddi vxgf"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = from_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(from_email, from_password)
        smtp.send_message(msg)

