from typing import Protocol


class Role(Protocol):
    """
    I wrote this to control editability of products and stores. However, I later realized is_superuser field of django's
    built in User class is sufficient for my use case.
    """

    @staticmethod
    def can_edit() -> bool:
        ...


class AdminRole:
    @staticmethod
    def can_edit() -> bool:
        return True


class GeneralRole:
    @staticmethod
    def can_edit() -> bool:
        return False
