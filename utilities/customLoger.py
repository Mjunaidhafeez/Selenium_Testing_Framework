import inspect
import logging
class LogGen():
    def loggen(logLevel=logging.INFO):
        logger_name=inspect.stack()[1][3]
        logger=logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        fh=logging.FileHandler("H:\\Selenium_Test_Project\\Logs\\automation.log")
        formatter=logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
    # @staticmethod
    # def loggen():
    #     logging.basicConfig(filename="H:\\Selenium_Test_Project\\Logs\\automation.log",
    #                         format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:S %p')
    #     logger = logging.getLogger()
    #     logger.setLevel(logging.INFO)
    #     return logger
# class calling():
#     log=LogGen.loggen()
#     log.info("********************Verifying Login Test Page Started******************")
