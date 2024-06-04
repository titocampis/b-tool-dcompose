from datetime import datetime
from flask import jsonify
from flask_mail import Mail, Message

import utils.utilities as mut

def send_mail(sender_mail_username:str, receiver_mail_username:str, subject:str, data_alias:str, data_birthday:datetime, data_sex:bool):
    try:

        # Validate email formats
        if '@' not in sender_mail_username:
            raise ValueError('Invalid sender email format')
        if '@' not in receiver_mail_username:
            raise ValueError('Invalid receiver email format')
        
        # Calculate years
        years = mut.calculate_old(data_birthday)
        
        # Define the message to send
        mail_message = Message(
                subject = subject, 
                sender =  ("B-Tool Bot", sender_mail_username), 
                recipients = [str(receiver_mail_username)])
        
        # Define body
        mail_message.body = f"Muchísimas felicidades {data_alias}!! Espero que pases un gran día, disfruta mucho de tus {years}.\nFeliz cumpleaños y un fuerte abrazo! <3"

        mail.send(mail_message)

        # return jsonify({'message': 'Email sent successfully'}), 200
    
    # If the message cannot be sent
    except Exception as e:
        print("Falle", e)
