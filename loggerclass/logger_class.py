import logging


class LoggerCalss(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def enable_system(self):
        self.logger.warning('Enabling system!')
        self.logger.info('Still enabling system!!')

    def disable_system(self):
        self.logger.warning('Disabling system!')
        self.logger.info('Still disabling system!!')
