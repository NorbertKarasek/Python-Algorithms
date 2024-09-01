# Using logging module to log messages to a file or console

import logging

# Create a logger object
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Create a file handler
fh = logging.FileHandler('my.log')
fh.setLevel(logging.DEBUG)

# Create a console handler
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

# Log some messages
logger.debug('This is a debug message')
logger.debug('This is another debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Close the file handler
fh.close()

# Close the console handler
ch.close()

# Remove the handlers
logger.removeHandler(fh)
logger.removeHandler(ch)

# Remove the logger
del logger

# Read the log file
with open('my.log', 'r') as f:
    print(f.read())

# Output:
# 2020-07-31 12:16:54,037 - my_logger - WARNING - This is a warning message
# 2020-07-31 12:16:54,037 - my_logger - ERROR - This is an error message
# 2020-07-31 12:16:54,037 - my_logger - CRITICAL - This is a critical message
