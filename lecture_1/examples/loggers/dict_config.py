

import logging
import logging.config

import yaml


with open("lecture_1/examples/loggers/logging.yaml") as f:
    logging_conf = yaml.safe_load(f)
logging.config.dictConfig(logging_conf)
logger = logging.getLogger(__name__)


def main():
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == "__main__":
    main()
