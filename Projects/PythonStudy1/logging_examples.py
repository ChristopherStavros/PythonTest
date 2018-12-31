import logging

#log to file
#logging.basicConfig(filename = 'log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') #notice the 'string formating'

#log to screen
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') #notice the 'string formating'

#disable all logging except for critical messages
logging.disable(logging.CRITICAL)

'''
We are using logging.debug() below ..whcih is the lowest level

but we could use the following:

logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()

'''

#debug calls are kind of like print fuction calls
#but they give lots of additional info
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial (%s)' % (n)) #notice the 'string formating'
    total = 1
    for i in range(1, n + 1): #range start at 1 and up to n+1
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))
logging.debug('End of program')