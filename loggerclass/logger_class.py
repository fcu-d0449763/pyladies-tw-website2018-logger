import logging
import logging.handlers
import os
import zlib

def namer(name):
    return name + ".gz"

def rotator(source, dest):
    print(f'compressing {source} -> {dest}')
    with open(source, "rb") as sf:
        data = sf.read()
        compressed = zlib.compress(data, 9)
        with open(dest, "wb") as df:
            df.write(compressed)
    os.remove(source)


class LoggerCalss(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        logger_handler = logging.handlers.TimedRotatingFileHandler('python_logging.log', when="M", interval=1,encoding='utf-8', backupCount=30, utc=True)
        #logger_handler = logging.handlers.RotatingFileHandler('python_logging.log', when="M", interval=1,encoding='utf-8', backupCount=30, utc=True)
        logger_handler.rotator = rotator
        logger_handler.namer = namer
        logger_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)
        self.logger.info('Completed configuring logger()!')

    def debug(self,text):
        self.logger.debug(text)

    def info(self,text):
        self.logger.info(text)

    def warning(self,text):
        self.logger.warning(text)

    def error(self,text):
        self.logger.error(text)
    
    def critical(self,text):
        self.logger.critical(text)

    def enable_system(self):
        self.logger.warning('Enabling system!')
        self.logger.info('Still enabling system!!')

    def disable_system(self):
        self.logger.warning('Disabling system!')
        self.logger.info('Still disabling system!!')
