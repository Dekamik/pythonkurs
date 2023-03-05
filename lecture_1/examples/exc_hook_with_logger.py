import logging
import sys


logger = logging.getLogger(__name__)


def exc_hook(exc_type, exc_value, exc_traceback):
    logger.error(
        "uncaught exception",
        exc_info=(exc_type, exc_value, exc_traceback)
    )


sys.excepthook = exc_hook


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler()
        ])

    raise ValueError("Some error")


if __name__ == "__main__":
    main()
