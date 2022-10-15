from reddit_parser import SubredditParser

subreddit_name = '/r/python'

s = SubredditParser(subreddit_name)


for post in s.get():
    title = post['title']
    body = post['selftext'].replace('\n', '')
    rating = post['ups']
    print(rating, title, body)
