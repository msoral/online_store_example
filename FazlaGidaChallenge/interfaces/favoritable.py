from typing import Protocol


class Favoritable(Protocol):
    @staticmethod
    def is_favorite() -> bool:
        """Add an item to favorites"""
