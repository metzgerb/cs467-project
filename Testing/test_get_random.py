#!/usr/bin/env python3

"""Program Name: test_keywords.py
Python Version: 3
Description: Runs tests to check the get_random function of the URL class used
    in crawlutil.py
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-26
Last Modified: 2019-10-26
"""


#import dependencies
import sys, os

#add package path to syspath
sys.path.append(os.path.join(os.getcwd(),'crawlutil'))

import crawlutil as cu

ROOT_URL = "https://web.engr.oregonstate.edu/~metzgerb/crawler/"

"""
Name: get_links Relative Path Links in grandparent directory
Target: crawlutil.get_links()
Input: "sub/sub/subsub1.html"
Expected Output: URL object with 5 links, no parent, and a status of 200
"""
print("Testing Relative Path Links in Grandparent Directory: " + ROOT_URL + "sub/sub/subsub1.html")
test_url = cu.URL()
test_url = cu.get_links(ROOT_URL + "sub/sub/subsub1.html")

#check for failures
print("Checking status (200): ", end = "")
assert(test_url.status == 200)
print(str(test_url.status))

print("Checking parent (None): ", end = "")
assert(test_url.parent is None)
print("None")

print("Checking # of links (5): ", end = "")
assert(len(test_url.links) == 5)
print(len(test_url.links))

test_list = [
    ROOT_URL + "relative.html",
	ROOT_URL + "index.html",
	ROOT_URL + "nolinks.html",
	ROOT_URL + "sub/sub1.html",
	ROOT_URL + "badlink.html",
]

#sort lists
test_list.sort()
test_url.links.sort()

print("Checking links match: ", end = "")
assert(test_url.links == test_list)
print("PASSED\n\n")

del test_url


print("ALL TESTS PASSED")