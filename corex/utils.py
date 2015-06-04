# -*- coding: utf-8 -*-
"""
Helper Module

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__  = April 2015

"""
import time
from functools import wraps


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
