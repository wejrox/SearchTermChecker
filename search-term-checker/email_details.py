# Replace details in here with your desired auth and recipient.

credentials = {
    'username': 'USERNAME',
    'password': 'PASSWORD'
}

# All server authentication is executed using TLS.
server = {
    # Outlook: smtp-mail.outlook.com
    # Gmail: smtp.gmail.com
    'host': 'SMTP_MAIL_SERVER',

    # Outlook: 587
    # Gmail: 587
    'port': 123
}

# Email address to send the message to on term hit.
recipient = 'some.email@PROVIDER.com'
