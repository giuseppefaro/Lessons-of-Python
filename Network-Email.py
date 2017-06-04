import smtplib

#### This app will send an email using the TLS protocol

# Server Login Information
username = ('')
password = ('')
server = smtplib.SMTP ('') #SMTP Server Address


def sendmail(username,password,server):
       fromaddr = input('From: ')
       toaddrs = [input('To: ')]
       subject = input('Add the Subject: ')
       text = input('write here your message: ')
       # to work the message need to have this format show below
       msg = ("""From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (fromaddr, ", ".join(toaddrs), subject, text)
              )
       server.starttls()
       server.ehlo()
       server.login(username, password)
       server.sendmail(fromaddr, toaddrs, msg)
       server.quit()
       print('The mail has been sent successfully')

# Starting point
sendmail(username,password,server)
