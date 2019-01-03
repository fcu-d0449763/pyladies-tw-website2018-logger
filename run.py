from loggerclass import LoggerCalss



system = LoggerCalss()
system.enable_system()
system.logger_warning("logger_warning")
system.logger_debug("logger_debug")
system.logger_info("logger_info")
system.logger_error("logger_error")
system.logger_critical("logger_critical")
system.disable_system()

