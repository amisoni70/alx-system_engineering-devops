#!/usr/bin/python3
"""Function that queries the Reddit api"""
import requests
import sys


def top_ten(subreddit):
    """
    A function that prints the titles of the first 10
    hot posts listed for a given subreddit
    Return 0 for an invalid subreddit
    """
    headers = {'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/Efficient_Reading189)'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    firstten = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=firstten)

    if response.status_code == 200:
        hottitles = response.json().get('data').get('children')
        for hottitle in hottitles:
            print(hottitle.get('data').get('title'))
    else:
        print(None)
