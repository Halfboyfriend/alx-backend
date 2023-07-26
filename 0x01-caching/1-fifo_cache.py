#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCACHE
    """

    def __init__(self):
        """
        Initializing"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """

        :param key:
        :param item:
        :return:
        """
        if key is None or item is None:
            pass

        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.queue.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}\n")

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Return None"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
