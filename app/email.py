from flask_mail import Message
from . import mail
from app.models import User
from flask import url_for

sender_email = 'derrickip34@gmail.com'

def send_reset_email(user):
    token = user.get_token()
    message = Message('Password Reset Request', sender=sender_email,recipients=[user.email])
    message.body = f'''
    To reset your password, visit the following link
    {url_for('main.reset_token',token=token,_external=True)}
    '''
    mail.send(message)