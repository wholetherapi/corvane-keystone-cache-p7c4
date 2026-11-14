"""Semantic-aware eviction policy."""

def choose_victim(entries):
    return min(entries, key=lambda e: e.get('last_score', 0))
