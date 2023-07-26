#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """

        :param key: Key
        :param item:
        :return:
        """
        if key is None or item is None:
            pass

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last = self.queue.pop()
            del self.cache_data[last]
            print(f'\nDISCARD: {last}')

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        if key is None:
            return None
        return self.cache_data[key, None]
