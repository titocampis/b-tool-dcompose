import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(
    sender_mail_username: str,
    sender_mail_password: str,
    sender_name: str,
    receiver_mail_username: str,
    subject: str,
    body: str,
) -> bool:
    """
    Method to send a mail which python using google account

    Parameters:
    sender_mail_username (str): email which sends the mail.
    sender_mail_password (str): key from email which send the mail.
    sender_name (str): name whic will appear on the email.
    receiver_mail_username (str): email which receives the mail.
    subject (str): subject of the email.
    body (str): main content of the email.

    Returns:
    bool: True if the email has been sent successfully.
    """
    try:
        # Validate email formats
        if "@" not in sender_mail_username:
            raise ValueError("Invalid sender email format")
        if "@" not in receiver_mail_username:
            raise ValueError("Invalid receiver email format")

        # Create a MIMEText object to represent the email
        message = MIMEMultipart()

        # Define the message to send
        message["From"] = f"{sender_name} <{sender_mail_username}>"
        message["To"] = receiver_mail_username
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server (in this case, Gmail's SMTP server)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login to your email account
        server.login(sender_mail_username, sender_mail_password)

        # Send the email
        server.sendmail(
            sender_mail_username, receiver_mail_username, message.as_string()
        )

        # Quit the SMTP server
        server.quit()

        print(f"[{datetime.now()}]: Email sent successfully!")
        return True

    # If the message cannot be sent
    except ValueError as ve:
        raise ValueError(f"Invalid email or password format: {ve}") from ve

    except smtplib.SMTPException as smtp_err:
        raise smtplib.SMTPException(
            f"SMTP error occurred: {smtp_err}"
        ) from smtp_err
