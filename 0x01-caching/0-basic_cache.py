#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCaching
    """
    def put(self, key, item):
        """

        :param key:
        :param item:
        :return:
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        
        :param key:
        :return:
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
