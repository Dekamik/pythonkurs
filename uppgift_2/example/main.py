"""

"""


import logging

import yaml

from data import ViatiDAO


logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)s.%(module)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )

    with open("uppgift_2/example/config.yaml", "r") as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            logger.error(e, exc_info=True)

    logger.info("started application")

    with ViatiDAO(config["db"]["file"]) as dao:
        dao.add_person("Adam", "adam@viati.se", "123456789")
        dao.add_person("Bertil", "bertil@viati.se", "987654321")

        for row in dao.get_all_people():
            print(row)

    logger.info("finished")


if __name__ == "__main__":
    main()
