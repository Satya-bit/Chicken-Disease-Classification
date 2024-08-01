import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"   #Log message to be displayed

log_dir = "logs"   # This creates a directory of log and inside it a logging file is created
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,    #Taking information from the log
    format= logging_str,     #Initializing the logging string

    handlers=[
        logging.FileHandler(log_filepath),  #Create the log file
        logging.StreamHandler(sys.stdout)  #Prints the log on the terminal also
    ]
)

logger = logging.getLogger("cnnClassifierLogger")   #Naming the log
