# from os import path, remove
# import logging
# from .logger_class import LoggerCalss
# import os
# import zlib
# import logging.handlers


# def namer(name):
#     return name + ".gz"


# def rotator(source, dest):
#     print(f'compressing {source} -> {dest}')
#     with open(source, "rb") as sf:
#         data = sf.read()
#         compressed = zlib.compress(data, 9)
#         with open(dest, "wb") as df:
#             df.write(compressed)
#     os.remove(source)

# # # If applicable, delete the existing log file to generate a fresh log file during each execution
# # if path.isfile("python_logging.log"):
# #     remove("python_logging.log")

# # Create the Logger
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# # # Create the Handler for logging data to a file
# # logger_handler = logging.FileHandler('python_logging.log')
# # logger_handler.setLevel(logging.DEBUG)


# logger_handler = logging.handlers.TimedRotatingFileHandler('python_logging.log', when="M", interval=1,encoding='utf-8', backupCount=30, utc=True)
# logger_handler.rotator = rotator
# logger_handler.namer = namer

# # Create a Formatter for formatting the log messages
# # 定義輸出格式
# logger_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# # Add the Formatter to the Handler
# logger_handler.setFormatter(logger_formatter)

# # Add the Handler to the Logger
# logger.addHandler(logger_handler)
# logger.info('Completed configuring logger()!')
