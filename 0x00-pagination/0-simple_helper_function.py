#!/usr/bin/env python3
"""
Helper Function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    a tuple of size two containing a start index and an end index corresponding
    to the range of indexes to return in a list for those particular
    pagination parameters.
    """
    start = page_size * (page - 1)
    end = start + page_size
    return (start, end)
