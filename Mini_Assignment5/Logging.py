import inspect
import logging


def getlogger():
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    file_handler = logging.FileHandler('/Users/vidmisra/PycharmProjects/Selenium/Mini_Assignment4/logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)
    return logger
