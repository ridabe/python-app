import os
import smtplib
from email.message import EmailMessage
from configEmail import usuario, senha, smtpHost, port

EMAIL_ADRESS = usuario
EMAIL_PASSWORD = senha

def sendMail(subject, fromUser, to, mensage ):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['from'] = fromUser
    msg['to'] = to
    msg.set_content(mensage)
    
    with smtplib.SMTP_SSL(f'{smtpHost}', port) as smtp:
        smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    
    

