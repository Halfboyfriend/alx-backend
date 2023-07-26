#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.queue[0]))
                del self.cache_data[self.queue[0]]
                del self.queue[0]
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
