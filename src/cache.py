"""Keystone vector cache core."""

class KeystoneCache:
    def __init__(self, capacity: int = 1024):
        self.capacity = capacity
        self._entries = {}

    def get(self, key):
        return self._entries.get(key)
