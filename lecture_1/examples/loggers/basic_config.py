import logging


logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler()
        ])

    logger.debug("this is a debug message")
    logger.info("this is an info message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")

    try:
        raise ValueError()
    except:
        logger.exception("this is an exception message")


if __name__ == "__main__":
    main()
