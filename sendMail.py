# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 12:09:04 2020

@author: Venkat
"""


import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email=EmailMessage()
email['from'] = 'Name of Sender'
email['to'] = 'Your email id'
email['subject'] = 'This is an Test Email'

email.set_content(html.substitute({'name':'Test'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Enter you GMail ID','Enter Your Password')
    smtp.send_message(email)
    
    