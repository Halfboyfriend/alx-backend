#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """
    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data:
                print("DISCARD: {}".format(self.stack[0]))
                del self.cache_data[self.stack[0]]
                del self.stack[0]
            if key in self.stack:
                del self.stack[self.stack.index(key)]
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """
        if key is not None and key in self.cache_data.keys():
            del self.stack[self.stack.index(key)]
            self.stack.append(key)
            return self.cache_data[key]
        return None
