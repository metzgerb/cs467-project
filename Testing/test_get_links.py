#!/usr/bin/env python3

"""Program Name: test_get_links.py
Python Version: 3
Description: Runs tests for the get_links function in crawlutil.py
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-19
Last Modified: 2019-10-20
"""


#import dependencies
import sys, os

#add package path to syspath
sys.path.append(os.path.join(os.getcwd(),'crawlutil'))

import crawlutil as cu

ROOT_URL = "https://web.engr.oregonstate.edu/~metzgerb/crawler/"

"""
Name: get_links Absolute Path Links
Target: crawlutil.get_links()
Input: "index.html"
Expected Output: URL object with 5 links, no parent, and a status of 200
"""
print("Testing Absolute Path links: " + ROOT_URL + "index.html")
test_url = cu.URL()
test_url = cu.get_links(ROOT_URL + "index.html")

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
	ROOT_URL + "nolinks.html",
	ROOT_URL + "sub/sub1.html",
	ROOT_URL + "sub/sub/subsub1.html",
	ROOT_URL + "badlink.html",
]

#sort lists
test_list.sort()
test_url.links.sort()

print("Checking links match: ", end = "")
assert(test_url.links == test_list)
print("PASSED\n\n")

del test_url

"""
Name: get_links Relative Path Links in Same directory
Target: crawlutil.get_links()
Input: "relative.html"
Expected Output: URL object with 5 links, no parent, and a status of 200
"""
print("Testing Relative Path Links in Same Directory: " + ROOT_URL + "relative.html")
test_url = cu.URL()
test_url = cu.get_links(ROOT_URL + "relative.html")

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
	ROOT_URL + "sub/sub1.html",
	ROOT_URL + "sub/sub/subsub1.html",
	ROOT_URL + "badlink.html",
]

#sort lists
test_list.sort()
test_url.links.sort()

print("Checking links match: ", end = "")
assert(test_url.links == test_list)
print("PASSED\n\n")

del test_url


"""
Name: get_links Relative Path Links in parent directory
Target: crawlutil.get_links()
Input: "sub/sub1.html"
Expected Output: URL object with 5 links, no parent, and a status of 200
"""
print("Testing Relative Path Links in Parent Directory: " + ROOT_URL + "sub/sub1.html")
test_url = cu.URL()
test_url = cu.get_links(ROOT_URL + "sub/sub1.html")

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
	ROOT_URL + "sub/sub/subsub1.html",
	ROOT_URL + "badlink.html",
]

#sort lists
test_list.sort()
test_url.links.sort()

print("Checking links match: ", end = "")
assert(test_url.links == test_list)
print("PASSED\n\n")

del test_url


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


"""
Name: get_links No links
Target: crawlutil.get_links()
Input: "nolinks.html"
Expected Output: URL object with 0 links, no parent, and a status of 200
"""
print("Testing URL with no links: " + ROOT_URL + "nolinks.html")
test_url = cu.URL()
test_url = cu.get_links(ROOT_URL + "nolinks.html")

#check for failures
print("Checking status (200): ", end = "")
assert(test_url.status == 200)
print(str(test_url.status))

print("Checking parent (None): ", end = "")
assert(test_url.parent is None)
print("None")

print("Checking # of links (0): ", end = "")
assert(len(test_url.links) == 0)
print(len(test_url.links))

test_list = []

#sort lists
test_list.sort()
test_url.links.sort()

print("Checking links match: ", end = "")
assert(test_url.links == test_list)
print("PASSED\n\n")

del test_url

print("ALL TESTS PASSED")