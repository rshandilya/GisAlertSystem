import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

def send_email_to(email_address,message_to_send,subject):
    email='goldenhourrescue@gmail.com'
    password='Golden@hourrescue'
    message=message_to_send
    subject=subject
    msg=MIMEMultipart()
    msg['From']=email
    msg['To']=email_address
    msg['Subject']=subject
    msg.attach(MIMEText(message_to_send,'plain'))
    text=msg.as_string()
    server=smtplib.SMTP('smtp.gmail.com',587)  #the gmail server
    server.starttls() #statrt scripting in the Gmail account
    server.login(email,password) #login throuh t he provided gmail id password
    server.sendmail(email,email_address,text) #sending mail to the recipent
    server.quit()