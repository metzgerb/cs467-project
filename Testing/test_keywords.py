#!/usr/bin/env python3

"""Program Name: test_keywords.py
Python Version: 3
Description: Runs tests to check the keyword functionality of get_links 
    function in crawlutil.py
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
Name: get_links keyword positive test exact match inside p tag
Target: crawlutil.get_links()
Input: "index.html", keyword = "banana" found in data contained in tags
Expected Output: URL object with key flag set to True
"""
keyword = "banana"
print("Testing exact match inside tag (" + keyword + "): " + ROOT_URL + "index.html")
test_url = cu.URL()
test_url = cu.get_links(ROOT_URL + "index.html", keyword)

#check for failures
print("Checking key attribute (True): ", end = "")
assert(test_url.key)
print(str(test_url.key))

print("PASSED\n\n")

del test_url


"""
Name: get_links keyword positive test case insensitive inside p tag
Target: crawlutil.get_links()
Input: "index.html", keyword = "BANANA" found in data contained in tags
Expected Output: URL object with key flag set to True
"""
keyword = "BANANA"
print("Testing case-insensitive match inside tag (" + keyword + "): " + ROOT_URL + "index.html")
test_url = cu.URL()
test_url = cu.get_links(ROOT_URL + "index.html", keyword)

#check for failures
print("Checking key attribute (True): ", end = "")
assert(test_url.key)
print(str(test_url.key))

print("PASSED\n\n")

del test_url


"""
Name: get_links keyword positive test exact match outside tag
Target: crawlutil.get_links()
Input: "index.html", keyword = "taco" found in data
Expected Output: URL object with key flag set to True
"""
keyword = "taco"
print("Testing exact match outside tag (" + keyword + "): " + ROOT_URL + "index.html")
test_url = cu.URL()
test_url = cu.get_links(ROOT_URL + "index.html", keyword)

#check for failures
print("Checking key attribute (True): ", end = "")
assert(test_url.key)
print(str(test_url.key))

print("PASSED\n\n")

del test_url


"""
Name: get_links keyword positive test case insensitive outside of tag
Target: crawlutil.get_links()
Input: "index.html", keyword = "taCo" found in data contained in tags
Expected Output: URL object with key flag set to True
"""
keyword = "taCo"
print("Testing case-insensitive match outside tag (" + keyword + "): " + ROOT_URL + "index.html")
test_url = cu.URL()
test_url = cu.get_links(ROOT_URL + "index.html", keyword)

#check for failures
print("Checking key attribute (True): ", end = "")
assert(test_url.key)
print(str(test_url.key))

print("PASSED\n\n")

del test_url


"""
Name: get_links keyword negative test keyword not found anywhere
Target: crawlutil.get_links()
Input: "index.html", keyword = "walnut" not found on page
Expected Output: URL object with key flag set to True
"""
keyword = "walnut"
print("Testing no keyword (" + keyword + "): " + ROOT_URL + "index.html")
test_url = cu.URL()
test_url = cu.get_links(ROOT_URL + "index.html", keyword)

#check for failures
print("Checking key attribute (False): ", end = "")
assert(not test_url.key)
print(str(test_url.key))

print("PASSED\n\n")

del test_url


"""
Name: get_links keyword negative test keyword found in attribute of tag
Target: crawlutil.get_links()
Input: "index.html", keyword = "bacon" in class attribute of tag
Expected Output: URL object with key flag set to True
"""
keyword = "bacon"
print("Testing keyword in attribute of tag (" + keyword + "): " + ROOT_URL + "index.html")
test_url = cu.URL()
test_url = cu.get_links(ROOT_URL + "index.html", keyword)

#check for failures
print("Checking key attribute (False): ", end = "")
assert(not test_url.key)
print(str(test_url.key))

print("PASSED\n\n")

del test_url


"""
Name: get_links keyword negative test keyword found in tag (bad syntax)
Target: crawlutil.get_links()
Input: "index.html", keyword = "cheesecake" in tag (bad syntax)
Expected Output: URL object with key flag set to True
"""
keyword = "cheesecake"
print("Testing keyword in tag (" + keyword + "): " + ROOT_URL + "index.html")
test_url = cu.URL()
test_url = cu.get_links(ROOT_URL + "index.html", keyword)

#check for failures
print("Checking key attribute (False): ", end = "")
assert(not test_url.key)
print(str(test_url.key))

print("PASSED\n\n")

del test_url


print("ALL TESTS PASSED")