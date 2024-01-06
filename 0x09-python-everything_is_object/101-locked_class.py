#!/usr/bin/python3
"""Define a locked class"""


class LockedClass():
    """
    Locked class that prevents the creation of other instance
    """
    
    __slots__ = ["first_name"]