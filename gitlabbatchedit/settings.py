import os
import logging

from os.path import join, dirname, normpath
from dotenv import load_dotenv

log_level = (os.environ.get('LOG_LEVEL') or 'INFO').upper()

# logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s', level=getattr(logging, log_level))
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=getattr(logging, log_level))
