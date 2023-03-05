"""

"""


import csv
import logging
import sys

import yaml

from api.sr import SR


logger = logging.getLogger(__name__)


def exception_hook(exc_type, exc_value, exc_traceback):
    logger.error(
        "uncaught exception",
        exc_info=(exc_type, exc_value, exc_traceback)
    )


sys.excepthook = exception_hook


def main():
    with open("lecture_2/answer/config.yaml") as f:
        config = yaml.safe_load(f)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(config["logging"]["file"])
        ]
    )

    logger.debug("running application")

    api = SR(config)
    channels = list(api.get_channels())

    with open(config["storage"]["file"], "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "type", "url"])
        writer.writeheader()
        for channel in channels:
            writer.writerow({
                "id": channel["id"],
                "name": channel["name"],
                "type": channel["channeltype"],
                "url": channel["siteurl"]
            })

    logger.info("processed %s channels", len(channels))


if __name__ == "__main__":
    main()
