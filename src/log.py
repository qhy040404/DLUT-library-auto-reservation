# import
import logging
def initialLogger():
    # initial logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # initial filehandler
    logfile = './access.log'
    fh = logging.FileHandler(logfile, mode='a')
    fh.setLevel(logging.INFO)
    # initial format
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %message(s)")
    fh.setFormatter(formatter)
    # add handler
    logger.addHandler(fh)
    return logger