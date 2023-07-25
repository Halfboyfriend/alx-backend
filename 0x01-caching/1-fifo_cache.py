#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCACHE
    """

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
            return None

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.queue.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}\n")

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        if key is None:
            return None
        return self.cache_data.get(key, None)
