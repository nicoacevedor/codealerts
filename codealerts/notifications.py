import smtplib
from email.mime.text import MIMEText

from .environment import load_env


def send_email(subject: str, body: str) -> None:
    env = load_env()
    # from_email = "nacevedo@meteodata.cl"
    # from_password = "bdnu lelu vddi vxgf"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = env["EMAIL"]
    msg["To"] = env["EMAIL"]

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(env["EMAIL"], env["PASSWORD"])
        smtp.send_message(msg)

