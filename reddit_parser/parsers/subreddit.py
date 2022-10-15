from typing import Iterable

from ..config import BASE_URL, SESSION
from ..classes.post import ChildrenListing, Post, PostListing
from .base import BaseParser


class SubredditParser(BaseParser):

    def __init__(self, sub_name):
        self.sub_name = sub_name
        self.url = BASE_URL.format(sub_name)

    def __get_children_listings(self) -> Iterable[ChildrenListing]:
        params = {'limit': 100}
        while True:
            response = SESSION.get(self.url, params=params)
            response.raise_for_status()
            data = PostListing(**response.json())['data']

            yield data['children']

            after = data['after']
            if after is None:
                break
            params['after'] = after

    def get(self) -> Iterable[Post]:
        for child in self.__get_children_listings():
            yield child['data']