import logging
import os

class ColorFormatter(logging.Formatter):
    
    COLORS = {
        logging.DEBUG : "\033[36m",
        logging.INFO : "\033[32m",
        logging.WARNING : "\033[33m",
        logging.ERROR : "\033[31m",
        logging.CRITICAL : "\033[1;31m"
    }
    
    RESET = "\033[0m"
    
    def format(self, record):
        base = super().format(record)
        color = self.COLORS.get(record.levelno, '')
        return f"{color}{record.levelname} line : {record.lineno} {base}{self.RESET}\nend-------------"

def configure_logging(log_file = 'app.log', level = logging.DEBUG, console_level = logging.DEBUG, file_level = logging.DEBUG, use_color = True):
    
    formatt = '%(levelname)s line : %(lineno)s %(name)s %(asctime)s  : \n%(message)s'
    
    logger = logging.getLogger()
    logger.setLevel(level)
    
    if logger.hasHandlers():
        return
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    if use_color:
        console_handler.setFormatter(ColorFormatter(formatt))
    else:
        console_handler.setFormatter(logging.Formatter(formatt))
    
    logger.addHandler(console_handler)
    
    file_handler = logging.FileHandler(filename= os.path.join('Output', log_file), mode= 'w', encoding='utf-8')
    file_handler.setLevel(file_level)
    
    file_handler.setFormatter(logging.Formatter(formatt))
    
    logger.addHandler(file_handler)
    
