# <p align = "center"> Reddit Lib </p>

This library allows you to parse reddit without using api keys.

**Note:** this library not finished yet.
If you encounter any bugs or have suggestions for improvement,
I will be glad to receive feedback.

Development plans:
- Make all parsers
  - [x] For subreddit
  - [x] For comments
  - [ ] For users
- Make a normal wiki
  - [ ] Subreddit describe
  - [ ] Comments describe
  - [ ] Comments describe

# Documentation

## Installation

This library is not finished yet, and not loaded into pip yet,
so use the command:

`pip install git+https://github.com/temkuz/reddit_lib`

## Examples

### Posts

If you need to get all posts from subreddit

```python
from reddit_lib import SubredditParser

s = SubredditParser('/r/python')
for post in s.get():
    print(post)
```

In this case `post` is a TypedDict an object that stores information about the post.
Because of the use of TypedDict, your IDE can tell you which keys you can use.
You can find a more detailed description on the wiki.

### Comments

If you need to get comments from post you need post permalink

You can get it from

```python
from reddit_lib import SubredditParser

s = SubredditParser('/r/python')
for post in s.get():
    permalink = post['permalink']
```

Or take from browser, but you need to delete this part of url https://www.reddit.com

Similar to use SubredditParser you can get comments this way:

```python
from reddit_lib import CommentParser

permalink = '/r/Python/comments/y9u87s/can_we_stop_creating_docker_images_that_require/'

comment_parser = CommentParser(permalink)
post, comments = comment_parser.get()

for comment in comments:
    print(comment)
```

CommentParser return 2 objects:
- post object
- generator for comments