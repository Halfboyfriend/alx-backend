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

        :param key:
        :param item:
        :return:
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lastItem = self.queue.pop()
            del self.cache_data[lastItem]
            print(f'DISCARD: {lastItem}')

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        if key is None:
            return None
        return self.cache_data[key, None]
