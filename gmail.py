# a module to send email
import smtplib
from email.mime.text import MIMEText
import os
import string
from random import choice

def send_from_gmail(subject, contents, rec):
    username = os.environ['GMAIL_USERNAME']
    password = os.environ['GMAIL_PASSWORD']
    
    message = MIMEText(contents)
    message['Subject'] = subject
    message['From'] = "Bush Schedule App"
    message['To'] = rec

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(username, password)
    
    session.sendmail(username, [rec], message.as_string())

def send_password(email):
    if email.endswith("@bush.edu"):
        temp_password = ''.join(choice(string.letters + string.digits) for _ in xrange(10))
        message = "Your Email: %s\nYour Password: %s" % (email, temp_password)
        send_from_gmail("Create Account", message, email)
        return temp_password
    