#!/usr/bin/python3
"""module that queries the Reddit API and returns the number of subscribers"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Function that  queries the Reddit API and
    returns the number of subscribers)"""
    link = 'https://www.reddit.com/r/{}/about.json'.format(sys.argv[1])
    responce = requests.get(link)
    if responce.status_code == 200:
        data = responce.json()
        return(data['data']['subscribers'])
    else:
        return 0
