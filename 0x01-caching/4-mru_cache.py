#!/usr/bin/python3
""" Caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache (BaseCaching):
    """
    LIFO caching
    """
    def __init__(self):
        """Initialise the MRUCache  class"""
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
            keys = list(self.cache_data.keys())
            if len(keys) == self.MAX_ITEMS and key not in keys:
                print(f"DISCARD: {keys[-1]}")
                del self.cache_data[keys[-1]]
            if key in keys:
                del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """
        Get a value from the cache dictionary
        Arg:
            key: the key of the value to get
        """
        result = self.cache_data.get(key)
        if result:
            del self.cache_data[key]
            self.cache_data[key] = result
            return result
