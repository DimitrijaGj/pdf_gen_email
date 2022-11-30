#!/usr/bin/env python3

from email.message import EmailMessage
import os
import mimetypes
import smtplib
import getpass


message = EmailMessage()
#print(message)
#gives us empty mail message
sender = 'zimzelen929@gmail.com'
recipient = 'dimitrijagjoshev@hotmail.com'
# giving two variables tha can be reused latter
message['From'] = sender
message['To'] = recipient
print(message)
# fills in the blank message 
message['Subject'] = 'Greetings from {} to {}'.format(sender,recipient)
#print(message)
#add the subject of the message
body = '''Hey there !
....
..... I'm leraning how to send mails in Python'''
message.set_content(body)
print(message)
# Here set_content() method addded couple of headers in the body
atachment_path = './atachment/example.png'
atachment_filename = os.path.basename(atachment_path)
mime_type, _= mimetypes.guess_type(atachment_path)
print(mime_type)
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)
# we use mime 'mimetypes' library to guess the attachemnt format and sent it trough a strings but separe file name and file type
with open(atachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(atachment_path) )
### comment out for clarity print(message)
# we open the attachment to put it in the string form attached to the mail serialized as string
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1)
mail_pass = getpass.getpass(input('Pls ente pass:'))
mail_server.login(sender, mail_pass)
mail_server.send_message(message)
{}
mail_server.quit()
# we have sesion with SMTP_SSl to our mail server then mail and password log in and send the message should return dict {} if somthing is happening
# so we create a message with email module and EmailMessage class we attached
# and send the mail with the smtp library
