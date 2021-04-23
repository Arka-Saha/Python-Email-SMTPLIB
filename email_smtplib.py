import smtplib
from email.message import EmailMessage

email_msg = EmailMessage()  # setting up a email

email_msg['Subject'] = 'Subject Of The Email'  # subject of the email
email_msg['From'] = 'Sender Name'  # From name in the email(sender's Name)
email_msg['To'] = 'reciever@domail.com'  # receiver's email eg, abcd@gmail.com
email_msg.set_content("Main Content or Body")  # body of email

# setting up the server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # the default values and port number, same for all!
server.login('Sender Email', 'Sender Password')  # sender's email and password
server.send_message(email_msg)  # sending the message through the smtplib server
server.quit()  # closing the server to prevent ensues like, email and password leaking!
# © Tech Stop | Arka
