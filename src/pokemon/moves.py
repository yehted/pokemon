import logging
import requests

class Move(object):
    def __init__(self, url, full_obj=None):
        self.full_obj = full_obj or self.get_from_api(url)

        self._name = None
        self._power = 0

    @property
    def name(self):
        if self.full_obj is None:
            self.full_obj = self.get_move_from_api()
        self._name = self.full_obj['name']

        return self._name

    @property
    def power(self):
        if self.full_obj is None:
            self.full_obj = self.get_move_from_api()
        p = self.full_obj['power']

        if p is None:
            p = 0.0

        self._power = p

        return self._power

    def get_from_api(self, url):
        """ Retrieves move information from web API """
        if url is None:
            return { "name": None, "power": None }

        logging.info("Retrieving move from api url: {}".format(url))
        res = requests.get(url)
        res.raise_for_status()
        info = res.json()

        return info

