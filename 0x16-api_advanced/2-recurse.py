#!/usr/bin/python3
""" recursive function that queries the Reddit API """
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """A function that returns a list containing the titles of all
    hot articles for a given subreddit.
    Return None if no results are found for the given subreddit
    """
    global after
    headers = {'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/Efficient_Reading189)'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        hottitles = response.json().get('data').get('children')
        for hottitle in hottitles:
            hot_list.append(hottitle.get('data').get('title'))
        return hot_list
    else:
        return (None)
