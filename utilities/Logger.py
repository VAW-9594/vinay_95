import logging
import os
class log_generator_class:
    @staticmethod
    def loggen_method():
        logger = logging.getLogger(__name__)
        log_file = logging.FileHandler("Logs/CredKart_Automation.log")
        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(funcName)s  - %(lineno)d - %(message)s") #
        log_file.setFormatter(log_format) # here we are setting log format
        logger.addHandler(log_file) # here we are adding log file
        logger.setLevel(logging.INFO) # here we are setting log level
        return logger


''''
What is log level ?
Debug
Info
Warning
Error
Critical
'''

'''
log file
log format
on every run, logs should add(append in same file
log level
'''


