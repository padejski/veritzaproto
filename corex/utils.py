"""
Helper Module

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__  = April 2015

"""

def flatten_list(lst):
    """flatten a list of lists"""
    lst = [item for sublist in lst for item in sublist]

    return lst
