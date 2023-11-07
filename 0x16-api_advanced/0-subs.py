#!/usr/bin/python3
"""Function that queries the Reddit api"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    A function that returns the no. of subscribers
    for a given subreddit.
    Return 0 for an invalid subreddit
    """
    headers = {'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/Efficient_Reading189)'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
