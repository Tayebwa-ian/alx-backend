#!/usr/bin/env python3
"""
Pagination
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for
    those particular pagination parameters.
    """
    start = page_size * (page - 1)
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Paginate the dataset
        Args:
            page: the page number to display the data on
            page_size: size of the data to be displayed on the page
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        range = index_range(page, page_size)
        if (page * page_size) <= len(self.dataset()):
            return self.dataset()[range[0]:range[1]]
        else:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Hypermedia pagination
        Args:
            page: the page number to display the data on
            page_size: size of the data to be displayed on the page
        """
        page_data = self.get_page(page, page_size)
        dataset_size = len(self.dataset())
        if dataset_size % page_size == 0:
            total_pages = dataset_size // page_size
        else:
            total_pages = (dataset_size // page_size) + 1
        pagination_info = {
            "page_size": page_size,
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "previous_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
        return pagination_info
