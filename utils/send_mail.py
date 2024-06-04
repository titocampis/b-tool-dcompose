from datetime import datetime
from flask import jsonify

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import utils.utilities as mut

def send_mail(sender_mail_username:str, sender_mail_password:str, sender_name:str, receiver_mail_username:str, subject:str, data_birthday:datetime):
    '''Method to send a mail'''
    try:

        # Validate email formats
        if '@' not in sender_mail_username:
            raise ValueError('Invalid sender email format')
        if '@' not in receiver_mail_username:
            raise ValueError('Invalid receiver email format')
        
        # Calculate years
        years = mut.calculate_old(data_birthday)
        
        # Create a MIMEText object to represent the email
        message = MIMEMultipart()

        # Define the message to send
        message["From"] = sender_mail_username
        message["To"] = receiver_mail_username
        message["Subject"] = "Test email from Python"
        
        # Define & attach body
        body = f"Muchísimas felicidades!! Espero que pases un gran día, disfruta mucho de tus {years}.\nFeliz cumpleaños y un fuerte abrazo! <3"
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server (in this case, Gmail's SMTP server)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login to your email account
        server.login(sender_mail_username, sender_mail_password)

        # Send the email
        server.sendmail(sender_mail_username, receiver_mail_username, message.as_string())

        # Quit the SMTP server
        server.quit()

        print("Email sent successfully!")

        # return jsonify({'message': 'Email sent successfully'}), 200
    
    # If the message cannot be sent
    except Exception as e:
        print("Falle", e)
