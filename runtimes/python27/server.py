import os
import sys
import logging
from time import time


class AppFilter(logging.Filter):
    def filter(self, record):
        record.function_id = os.environ.get("function_id", 'no_function_id')
        record.request_id = os.environ.get("request_id", 'no_request_id')
        return True


logger = logging.getLogger('pratai')
logger.setLevel(logging.DEBUG)

# Docker can log stdout and stderr
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(function_id)s - %(request_id)s - %(levelname)s - %(message)s')
logger.addFilter(AppFilter())

handler.setFormatter(formatter)
logger.addHandler(handler)


def load_function_from_filesystem(path='/etc/pratai/'):
    sys.path.append(path)
    from new_module import main
    return main


def load_payload():
    payload = os.environ.get("pratai_payload", None)
    return payload

    
def execute_function():
    f = load_function_from_filesystem()

    payload = load_payload()

    start = time()

    logger.debug("function started with payload {0}".format(str(payload)))

    result = None
    try:
        result = f(payload)
        status = 'succeeded'
    except Exception as err:
        status = 'failed'
        logger.error(err.message, exc_info=True)

    finish = time()

    logger.debug("function {0}, it took {1} seconds with response {2}"
                 .format(status, str(finish-start), str(result)))

    return result


if __name__ == '__main__':
    r = execute_function()


