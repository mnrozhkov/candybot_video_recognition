from pathlib import Path
top = Path(__file__).resolve().parents[2].as_posix()

import logging
import os
LOG_FOLDER = top + '/logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)


class ErrorLogger:
    '''
    append log file with specified filename
    '''

    def __init__(sefl, log_file_name: str, e: Exception):
        '''
        Constructor
        open and append log file
        Args:
            log_file_name: name of log file
            e: object of Exception class
        '''

        try:
            path_parts = log_file_name.split('/')
            log_file = path_parts[-1:][0]
            print(LOG_FOLDER + '/' + log_file + '.log')
            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            handler = logging.FileHandler(LOG_FOLDER + '/' + log_file + '.log')
            handler.setLevel(logging.ERROR)
            formatter = logging.Formatter('[%(asctime)s] %(message)s\n\n')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.error(e, exc_info=True)
        except Exception as e:
            print(str(e))
            pass

class Logger():
    """
    Custom logger class to save logs into file
    """
    def __init__(self):
        self.loggers = {}

    def setup_logger(self, name: str, filename: str, level: int = logging.INFO):
        """
        Setup logger

        Args:
            name: name of logger. type: str
            filename: full path to log file. type: str
            level: logging level. default = logging.INFO

        Returns: logger

        """
        if self.loggers.get(name):
            print(name)
            return self.loggers.get(name)

        else:

            logger = logging.getLogger(name)
            # logger.setLevel(logging.INFO)
            logger.setLevel(level)

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            #os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'a+') as temp_file:
                temp_file.close()

            handler = logging.FileHandler(filename)
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            self.loggers.update(dict(name=logger))

            return logger

# initialize app logger
app_logger = Logger()
