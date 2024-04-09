#!/usr/bin/python3
"""module that queries the Reddit API and returns the number of subscribers"""
import requests


def top_ten(subreddit):
    """Function that  queries the Reddit API and
    returns the number of subscribers)"""
    link = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(link, headers={'User-Agent': 'raafat'})
    data = response.json()
    if response.status_code == 200:
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
