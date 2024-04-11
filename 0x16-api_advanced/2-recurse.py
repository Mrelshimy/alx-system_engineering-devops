#!/usr/bin/python3
"""Script to paginate response"""

import requests


def recurse(subreddit, hot_list=[], page=1, limit=100):
    """A recursive function that queries the Reddit API
    returns a list containing the titles
    of all hot articles for a given subreddit.
    """

    if len(hot_list) >= limit:
        return hot_list

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {"page": page}
    heads = {
        "User-Agent": "raafat"
    }

    responce = requests.get(url, params=parameters, headers=heads)
    if responce.status_code == 404:
        return None
    data = responce.json()

    if "data" in data and "children" in data["data"]:
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])

    if "data" in data and "after" in data["data"]:
        page += 1
        return recurse(subreddit, hot_list, page)
    return hot_list
