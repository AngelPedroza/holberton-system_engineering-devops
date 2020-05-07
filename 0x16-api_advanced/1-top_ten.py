#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """Make a request of a specific subreddit the 10 hot posts"""
    url = 'https://api.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-agent': 'your bot 0.1'}
    subred = requests.get(url, headers=header, allow_redirects=False)

    if subred.status_code != 200:
        print(None)
        return None

    try:
        theme = subred.json()
    except:
        print("Not a valid JSON")
        return 0

    try:
        maindata = theme.get("data")
        children = maindata.get("children")
        for child in children[:10]:
            data = child.get("data")
            print(data.get("title"))
    except:
        return None
