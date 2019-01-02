'''
SMTP
Simple mail transfer protocol

#App specific password
https://support.google.com/accounts/answer/185833?hl=en

Change account access for less secure apps
To help keep Google Accounts through work, school, or other groups more secure, we block some less secure apps from using them. If you have this kind of account, you’ll see a "Password incorrect" error when trying to sign in. If so, you have two options:

Option 1: Install a more secure app that uses stronger security measures. All Google products, like Gmail, use the latest security measures.
Option 2: Change your settings to allow less secure apps into your account. We don't recommend this option because it can make it easier for someone to break into your account. If you want to allow access anyway, follow these steps:
Go to your Google Account.
On the left navigation panel, click Security.
On the bottom of the page, in the Less secure app access panel, click Turn on access.
 If you don't see this setting, your administrator might have turned off less secure app account access.

 https://support.google.com/accounts/answer/185839?co=GENIE.Platform%3DDesktop&oco=1

'''
import smtplib

#server
emailServer = 'smtp.gmail.com'

#CREDENTIALS
username = 'steez.steez.steez.steez@gmail.com'
destination = 'steez.steez.steez.steez@gmail.com'
print('Password?')
password = input()

#Connection
conn = smtplib.SMTP(emailServer, 587)
#print(type(conn)) # Connection object -- <class 'smtplib.SMTP'>
conn.ehlo() #hello ...returns response code ...it it is 200 something, this is good
# (250, b'smtp.gmail.com at your service, [   MY IP ADDRESS......REDACTED  ]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
conn.starttls()
# (220, b'2.0.0 Ready to start TLS')
conn.login(username, password)
message = 'Subject: Greetings\n\nGreetings from Python.'
conn.sendmail(username, destination, message)
