#smtp is a protocal we use to send mails
import smtplib
from email import encoders
from email.mime.text import MIMEText #ordinary text to be used
from email.mime.base import MIMEBase #used for the attachment
from email.mime.multipart import MIMEMultipart #

server = smtplib.SMTP('smtp.gmail.com', 587) #Gooogle the specific smtp server address(e.g., gmail =smtp.gmail) and definite port num 

#to start the whole process, call the function below
server.ehlo()

#unsecure login method
#server.login('netw06292@gmail.com', 'password')

#secure login method with encrypted txt file containg the mail password
with open('password.txt', 'r') as f:
    password = f.read()

server.login('netw06292@gmail.com', password)

#define message and header
msg = MIMEMultipart()
msg['From'] = 'Hobs' #sender
msg['To'] = 'chenxe6@gmail.com' #receiver
msg['Subject'] = 'Testing things out'

with open('message.txt', 'r') as f:
    message = f.read()

#attach text, image etc.
msg.attach(MIMEText(message, 'plain'))

filename = 'image.png'
attachment = open(filename, 'rb') # rb = reading binary (images)

p = MIMEBase('application', 'octet-scream') #scream to process image data
p.set_payload(attachment.read())

#encode image data that has just been read and set as a payload 
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename=(filename)')
msg.attach(p) #adding actual payload to the message 

text = msg.as_string() #Get the whole thing aas a string
server.sendmail('netw06292@gmail.com', 'chengxe6@gmail.com', text)


