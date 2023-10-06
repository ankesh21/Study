import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('hello')

def ask():
    while True:
        try:
            logger.info('ask user to insert values')
            num=int(input('Input an Integer : '))
        except:
            logger.info('user provided wrong input,so ask to insert again')
            print('An error occured! Please try again')
            continue
        else:
            logger.info('user provided the correct value')
            print('Thank you , your number square is '+str(num**2))
            break
logger.info('Starting of the program')
ask()
logger.info('end of the program')