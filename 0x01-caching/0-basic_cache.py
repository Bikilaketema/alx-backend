#!/usr/bin/env python3
"""basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """represents object that allows to store
    and retrieve items from dic. """
    def put(self, key, item):
        """+ an item in to the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """retrieves an item by key.
        """
        return self.cache_data.get(key, None)
