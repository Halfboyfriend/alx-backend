#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """

        :param key:
        :param item:
        :return:
        """
        if key is None and item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lastItem = self.cache_data.pop(-1)
            del self.cache_data[lastItem]

        self.cache_data[key] = item