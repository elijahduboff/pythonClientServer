import inspect
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


class Log:
    def __init__(self):
        pass

    def __call__(self, func):
        def decorator(*args, **kwargs):
            frame = inspect.currentframe().f_back
            logger.info(f'Вызываем функцию {func} c параметрами {args} {kwargs} из функции {frame.f_code.co_name}')
            return func(*args, **kwargs)

        return decorator


def log_func(func):
    def wrapper(*args, **kwargs):
        frame = inspect.currentframe().f_back
        logger.info(f'Вызываем функцию {func} с параметрами {args} {kwargs} из функции {frame.f_code.co_name}')
        return func(*args, **kwargs)

    return wrapper
