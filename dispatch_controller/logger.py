import os
import logging
from dispatch_controller.config import app

def create_loggin():

    log_level = logging.INFO

    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)

    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, 'logs')
    
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    
    log_file = os.path.join(logdir, 'app.log')

    handler = logging.FileHandler(log_file)

    handler.setLevel(log_level)

    app.logger.addHandler(handler)

    app.logger.setLevel(log_level)

    defaultFormatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
    handler.setFormatter(defaultFormatter)