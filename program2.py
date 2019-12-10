import smtplib, ssl
from template_reader import read_template
from contact_getter import get_contacts


port = 465
smtp_sever = 'smtp.gmail.com'
sender_email = 'ohdeeritsjon123@gmail.com'
receivers_name, receivers_email = get_contacts('files/contacts.txt')
message = read_template('files/message.txt')
password = input('Pass it in: ')

print(receivers_name, receivers_email, message)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_sever, port, context=context) as server:
    server.login(sender_email, password=password)
    for name, email in zip(receivers_name, receivers_email):
        message = message.format(name.title())
        print(message)
        server.sendmail(sender_email, email, message)