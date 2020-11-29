import smtplib
from email.message import EmailMessage

#Login ID and Password of your email
username = 'email_id'
password = 'password'

#senders email address and recipients email address
sender = 'studyhacks@example.com'
recipients = ['abc@example.com', 'def@example.com']

#subject of email
subject = 'This is subject'

for recipient in recipients:
    try:
        email = EmailMessage()

        email['From'] = sender
        email['To'] = recipient

        email['Subject'] = subject

        #The content file consist of the body of your message
        with open('content.txt') as file:
            email.set_content(file.read())

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.send_message(email)
        server.quit()

        print("🙂 Email to  '%s'  is sent successfully 🙂 " %recipient)

    except:
        print("Sorry ☹ Email to  '%s'  is Failed" %recipient)