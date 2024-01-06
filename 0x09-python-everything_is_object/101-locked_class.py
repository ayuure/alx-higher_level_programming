#!/usr/bin/python3
class LockedClass():
    """
    Locked class that prevents the creation of other instance
    """
    __slots__ = ["first_name"]