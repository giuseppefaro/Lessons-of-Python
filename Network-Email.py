import smtplib

#### This app will send an email using the TLS protocol

fromaddr = input('From: ')
toaddrs = [input('To: ')]

subject = input('Add the Subject: ')
text = input('write here your message: ')

# to work the message need to have this format show below
msg = ("""From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (fromaddr, ", ".join(toaddrs), subject, text)
       )

#server configuration
print('Now i will ask you your login information')
username = input('Username: ')
password = input('Password:')
server = smtplib.SMTP (input('Smtp Server'))

server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
print('The mail has been sent successfully')

