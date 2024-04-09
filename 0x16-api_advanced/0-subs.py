#!/usr/bin/python3
"""module that queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Function that  queries the Reddit API and
    returns the number of subscribers)"""
    link = 'https://www.reddit.com/r/{}/about.json'.format(str(subreddit))
    responce = requests.get(link, headers={'User-Agent': 'raafat'})
    if responce.status_code == 200:
        data = responce.json()
        return data.get('data').get('subscribers')
    else:
        return 0
