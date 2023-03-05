"""

"""


import csv
import logging

import requests
import yaml

from data.db import SverigesRadioDAO
from api.sr import SR


logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )

    logger.debug("starting application")

    with open("uppgift_2/example/config.yaml", "r") as f:
        config = yaml.safe_load(f)

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

    """
    with SverigesRadioDAO(config["db"]["file"]) as dao:
        for channel in channels:
            dao.add_channel(channel["name"], channel["id"],
                            channel["channeltype"], channel["siteurl"])
    """

    logger.info("finished")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"unhandled exception: {e}", exc_info=True)
        raise
