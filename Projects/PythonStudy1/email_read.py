'''
IMAP - Internet message access protocol
#not using imaplib

pip install imapaclient
pip install pyzmail36
'''

import imapclient
import pyzmail

#server
emailServer = 'smtp.gmail.com'

#CREDENTIALS
username = 'steez.steez.steez.steez@gmail.com'
#print('Password?')
password = 'qenXef-toxmu4-kevtov' #input()

#Connection
conn = imapclient.IMAPClient(emailServer, ssl=True)
loginMessage = conn.login(username, password)
print(loginMessage)

#Read
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search() #['SINCE 01-DECEMBER-2018'] ---threw an error
print(UIDs)

#Print message function
def printMessage(UID):
    rawMessage = conn.fetch([uid], ['BODY[]', 'FLAGS'])
    #print(rawMessage)
    message = pyzmail.PyzMessage.factory(rawMessage[uid][b'BODY[]'])
    print(message.get_addresses('from'))
    print(message.get_subject())
    print(message.text_part.charset)
    if message.html_part != None:
        print(message.html_part.charset)
        print(message.html_part.get_payload().decode('UTF-8'))
    if message.text_part != None:
        print(message.text_part.charset)
        print(message.text_part.get_payload().decode('UTF-8'))

#loop
for uid in UIDs:
    if uid == 14:
        printMessage(uid)

