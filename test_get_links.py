#!/usr/bin/env python3

"""Program Name: test_get_links.py
Python Version: 3
Description: Runs tests for the get_links function in crawlutil.py
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-19
Last Modified: 2019-10-19
"""


#import dependencies
import crawlutil.crawlutil as cu

"""
Name: get_links Absolute Path Links
Target: crawlutil.get_links()
Input: "https://web.engr.oregonstate.edu/~metzgerb/crawler/index.html"
Expected Output: URL object with 5 links, no parent, and a status of 200
"""
test_url = cu.URL()
test_url = cu.get_links("https://web.engr.oregonstate.edu/~metzgerb/crawler/index.html")

#check for failures
assert(test_url.status == 200)
assert(test_url.parent is None)
assert(len(test_url.links) == 5)

test_list = [
    "https://web.engr.oregonstate.edu/~metzgerb/crawler/relative.html",
	"https://web.engr.oregonstate.edu/~metzgerb/crawler/nolinks.html",
	"https://web.engr.oregonstate.edu/~metzgerb/crawler/sub/sub1.html",
	"https://web.engr.oregonstate.edu/~metzgerb/crawler/sub/sub/subsub1.html",
	"https://web.engr.oregonstate.edu/~metzgerb/crawler/badlink.html",
]

#sort lists
test_list.sort()
test_url.links.sort()

assert(test_url.links == test_list)