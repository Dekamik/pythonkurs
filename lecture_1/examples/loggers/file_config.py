

import logging
import logging.config


logging.config.fileConfig("lecture_1/examples/loggers/logging.conf")
logger = logging.getLogger(__name__)


def main():
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == "__main__":
    main()
