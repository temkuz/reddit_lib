from typing import Iterable

from ..config import BASE_URL, SESSION
from ..classes.post import ChildrenListing, Post, PostListing
from .base import BaseParser


class SubredditParser(BaseParser):

    def __init__(self, sub_name):
        self.sub_name = sub_name
        self.url = BASE_URL.format(sub_name)

    def get(self) -> Iterable[Post]:
        params = {'limit': 100}
        while True:
            response = SESSION.get(self.url, params=params)
            response.raise_for_status()
            data = PostListing(**response.json())['data']

            for child in data['children']:
                yield child['data']

            after = data['after']
            if after is None:
                break
            params['after'] = after
