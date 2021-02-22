import logging
import os
from logging import handlers

log_directory = os.getcwd()
log_file = os.path.join(log_directory, 'chat/log/logs/client.log')

logging.basicConfig(
    filename=log_file,
    format='%(asctime)s %(levelname)s %(module)s %(message)s',
    level=logging.INFO
)

logger = logging.getLogger('client')
