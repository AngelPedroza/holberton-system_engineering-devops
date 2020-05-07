#!/usr/bin/python3
"""Recursive with after that calls the rest comments"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    '''Return alll title of the posts of a subreddit'''
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)
    header = {'User-Agent': 'your bot 0.1'}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response:
        data = response.json().get('data')
        children = data.get('children')
        [hot_list.append(x.get('data').get('title')) for x in children]
        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
