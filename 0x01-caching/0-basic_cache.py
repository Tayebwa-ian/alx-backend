#!/usr/bin/python3
""" Caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Implements a basic caching system
    """
    def __init__(self):
        """Intialize BasicCache Class"""
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        Args:
            key: key in the dictionary
            item: value to the key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get a value from the cache dictionary
        Arg:
            key: the key of the value to get
        """
        result = self.cache_data.get(key)
        if result:
            return result
