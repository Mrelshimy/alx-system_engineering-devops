#!/usr/bin/python3
"""module that queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Function that  queries the Reddit API and
    returns the number of subscribers)"""
    link = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    responce = requests.get(link, headers={'User-Agent': 'raafat/1.0'})
    if responce.status_code == 200:
        data = responce.json()
        return(data['data']['subscribers'])
    else:
        return 0