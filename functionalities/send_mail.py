from flask import jsonify
from flask_mail import Mail, Message

def send_email(sender_mail_username, receiver_mail_username, subject, data_name, data_birthday, data_sex):
    try:

        # Check if any required field is empty
        if not subject or not data_name or not data_birthday or not data_sex:
            raise ValueError('Missing required fields')

        # Validate email formats
        if '@' not in sender_mail_username:
            raise ValueError('Invalid sender email format')
        if '@' not in receiver_mail_username:
            raise ValueError('Invalid receiver email format')
        
        # Calculate years
        # years =
        
        # Define the message to send
        mail_message = Message(
                subject = subject, 
                sender =  ("B-Tool Bot", sender_mail_username), 
                recipients = [str(receiver_mail_username)])
        
        # Define body
        mail_message.body = f"Muchísimas felicidades {data_name}!! Espero que pases un muy feliz {years} día de cumpleaños, un fuerte abrazo <3"
        
        # Send the email
        # mail.send(mail_message)

        return jsonify({'message': 'Email sent successfully'}), 200
    
    # If the message cannot be sent
    except Exception as e:
        return jsonify({'error': str(e)}), 500
