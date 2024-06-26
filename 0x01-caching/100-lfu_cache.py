#!/usr/bin/python3
""" Caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LIFO caching
    """
    def __init__(self):
        """Initialise the LFUCache class"""
        super().__init__()
        self.recently_used = {}

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
                discard_key = self.discarder()
                print(f"DISCARD: {discard_key}")
                del self.cache_data[discard_key]
                del self.recently_used[discard_key]
            if key in self.recently_used.keys():
                self.recently_used[key] += 1
            else:
                self.recently_used[key] = 1
            self.cache_data[key] = item

    def get(self, key):
        """
        Get a value from the cache dictionary
        Arg:
            key: the key of the value to get
        """
        result = self.cache_data.get(key)
        if result:
            if key in self.recently_used.keys():
                self.recently_used[key] += 1
            else:
                self.recently_used[key] = 1
            return result

    def discarder(self):
        """
        Calculates the least recently used and returns its key
        """
        temp_dict = self.recently_used
        keys = list(temp_dict.keys())
        least_used_key = keys[0]
        for key in keys:
            if temp_dict[key] < temp_dict[least_used_key]:
                least_used_key = key
        return least_used_key
