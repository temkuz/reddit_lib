from reddit_lib.parsers import CommentParser

permalink = '/r/Python/comments/y9u87s/can_we_stop_creating_docker_images_that_require/'

comment_parser = CommentParser(permalink)
post, comments = comment_parser.get()

for comment in comments:
    rating = comment['ups']
    author = comment['author']
    body = comment['body'].replace('\n', '')
    print(rating, author, body)
