#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Make a request of a specific subreddit"""
    url = 'https://api.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-agent': 'your bot 0.1'}
    subred = requests.get(url, headers=header, allow_redirects=False)

    if subred.status_code != 200:
        return 0

    try:
        theme = subred.json()
    except:
        print("Not a valid JSON")
        return 0

    data = theme.get("data")
    subscribers = data.get("subscribers")
    return subscribers
