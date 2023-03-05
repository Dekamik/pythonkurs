

import requests


class ApiError(Exception):
    """Raised on errors when calling external Apis"""

    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text

    def __str__(self):
        return f"{self.status_code} - {self.text}"


class SR:
    def __init__(self, config):
        self.__channels_url = config["sr_api"]["channels_url"]

    def get_channels(self):
        def call_endpoint(url):
            res = requests.get(url)
            if not res.ok:
                raise ApiError(res.status_code, res.text)
            return res.json()

        res_json = call_endpoint(f"{self.__channels_url}?format=json")
        for channel in res_json["channels"]:
            yield channel

        while "nextpage" in res_json["pagination"].keys():
            res_json = call_endpoint(res_json["pagination"]["nextpage"])
            for channel in res_json["channels"]:
                yield channel
