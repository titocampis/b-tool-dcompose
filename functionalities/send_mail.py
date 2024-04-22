from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

def send_email(sender_mail_username):
    try:
        # Retrieve data from form
        data = request.get_json()
        
        # Define Variables
        name = str(data['name'])
        email = str(data['email'])
        subject = str(data['subject'])
        message = str(data['message'])

        # Check if any required field is empty
        if not name or not email or not subject or not message:
            raise ValueError('Missing required fields')

        # Validate email format
        if '@' not in email:
            raise ValueError('Invalid email format')
        
        # Define the message to send
        mail_message = Message(
                subject = subject, 
                sender =  (name, sender_mail_username), 
                recipients = ['andreasscorelli@gmail.com'])
        
        # Define body
        mail_message.body = f"Nombre: {name}\nMail: {email}\n{message}"
        
        # Send the email
        # mail.send(mail_message)

        return jsonify({'message': 'Email sent successfully'}), 200
    
    # If the message cannot be sent
    except Exception as e:
        return jsonify({'error': str(e)}), 500
