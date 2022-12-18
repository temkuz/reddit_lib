from typing import Iterable

from .base import BaseParser
from ..config import BASE_URL

from ..classes.comment import Comment, CommentListing
from ..classes.post import Post, PostListing


class CommentParser(BaseParser):
    def __init__(self, permalink):
        self.permalink = permalink
        self.url = BASE_URL.format(permalink)

    @staticmethod
    def __get_post(response_json) -> Post:
        listing = PostListing(**response_json[0])
        listing_data = listing['data']
        child = listing_data['children'][0]
        post = child['data']
        return post

    @staticmethod
    def __get_comments(response_json):
        listing = CommentListing(**response_json[1])
        listing_data = listing['data']
        children = listing_data['children']

        for child in children:
            kind = child['kind']
            if kind == 'more':
                continue
            yield child['data']

    def get(self) -> (Post, Iterable[Comment]):
        response_json = self._make_request(self.url)
        post = self.__get_post(response_json)
        comments = self.__get_comments(response_json)
        return post, comments
