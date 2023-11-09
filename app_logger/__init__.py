'''
logger
'''
import logging

import app_constants


def getLogger(name:str)->logging.Logger:
    """
    pereopredelenie loggera
    :param name:
    :return:
    """
    log:logging.Logger=logging.Logger(name)
    console_handler:logging.streamHandler = logging.StreamHandler()
    #уровень логирования
    console_handler.setLevel(app_constants.LOG_LEVEL)
    #формат логирования
    console_handler.setFormatter(logging.Formatter(app_constants.LOG_FORMAT))

    file_handler:logging.FileHandler=logging.FileHandler(app_constants.LOG_FILE,
                                                         mode="w", encoding=app_constants.ENCODING)
    file_handler.setLevel(app_constants.LOG_LEVEL)
    file_handler.setFormatter(logging.Formatter(app_constants.LOG_FORMAT))

    log.addHandler(console_handler)
    log.addHandler(file_handler)
    return log