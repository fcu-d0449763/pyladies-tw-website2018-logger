import logging


class LoggerCalss(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)



    def logger_debug(self,text):
        self.logger.debug(text)

    def logger_info(self,text):
        self.logger.info(text)

    def logger_warning(self,text):
        self.logger.warning(text)

    def logger_error(self,text):
        self.logger.error(text)
    
    def logger_critical(self,text):
        self.logger.critical(text)

    def enable_system(self):
        self.logger.warning('Enabling system!')
        self.logger.info('Still enabling system!!')

    def disable_system(self):
        self.logger.warning('Disabling system!')
        self.logger.info('Still disabling system!!')
