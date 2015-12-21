# -*- coding: utf-8 -*-
"""
Helper Module

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__  = April 2015

"""
# ============================================================================
# imports
# ============================================================================
import time
from functools import wraps
from hashlib import md5
from difflib import SequenceMatcher


# ============================================================================
# utility functions
# ============================================================================
def flatten_list(lst):
    """flatten a list of lists"""
    lst = [item for sublist in lst for item in sublist]

    return lst


def auto_retry(tries=3, exc=Exception, delay=5):
    """retry decorator factory"""
    def decorator(func):
        """function decorator"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            """func wrapper"""
            for _ in range(tries):
                try:
                    return func(*args, **kwargs)
                except exc:
                    time.sleep(delay)
                    continue
            raise exc
        return wrapper
    return decorator


def are_similar(str1, str2, index=0.9):
    """Check if two strings are similar using a similarity index/ratio

    are_similar(str1, str2, index=0.9) -> True/False

    """
    if (not str1 or not str2):
        return False
    if SequenceMatcher(None, str1.strip(), str2.strip()).ratio() >= index:
        return True

    return False


def get_hash(obj):
    """get md5 digest of obj"""
    return md5(str(obj)).digest().decode("iso-8859-1")
# ============================================================================
# EOF
# ============================================================================
