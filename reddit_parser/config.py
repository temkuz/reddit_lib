from requests import Session

BASE_URL = 'https://www.reddit.com{}.json'

__headers = {'user-agent': 'test app (u/temkuz)'}

SESSION = Session()
SESSION.headers.update(__headers)
