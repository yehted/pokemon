import logging
import requests

class Moves(object):
    url_dict = {}

    @classmethod
    def _get_from_move_url(cls, url):
        res = requests.get(url)
        res.raise_for_status()
        info = res.json()

        return info

    @classmethod
    def get_move_power(cls, url, percent=0.1):
        if url in cls.url_dict:
            logging.info("Already seen this move: {}".format(
                cls.url_dict[url]['name']))
            return cls.url_dict[url]['power'] * percent

        info = cls._get_from_move_url(url)
        move_power = info['power']

        if move_power is None:
            logging.error("Move power is null for {}, setting to 0".format(
                info['name']))
            move_power = 0

        cls.url_dict[url] = {
            'name': info['name'],
            'power': move_power
        }

        return move_power * percent

