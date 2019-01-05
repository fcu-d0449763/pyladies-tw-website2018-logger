from loggerclass.logger_class import LoggerCalss  


system = LoggerCalss()
system.enable_system()
system.warning("警告")
system.debug("debug")
system.info("一般")
system.error("錯誤")
system.critical("critical")
system.disable_system()

