#!/usr/bin/python3
"""
Using reddit's API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """returning top ten post titles recursively"""
    global after
    headers = {'User-Agent': 'raafat'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    responce = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)

    if responce.status_code == 200:
        data = responce.json().get("data").get("after")
        if data is not None:
            after = data
            recurse(subreddit, hot_list)
        all_titles = responce.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
