#!/usr/bin/env python3

"""Program Name: test_keywords.py
Python Version: 3
Description: Runs tests to check the get_random function of the URL class used
    in crawlutil.py
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-26
Last Modified: 2019-10-28
"""


#import dependencies
import sys, os

#add package path to syspath
sys.path.append(os.path.join(os.getcwd(),'crawlutil'))

import crawlutil as cu

ROOT_URL = "https://web.engr.oregonstate.edu/~metzgerb/crawler/"

#set debug flag and counters
DEBUG = False
passed = 0
failed = 0


if len(sys.argv) > 1:
    DEBUG = True 

print("Running get_random() tests...", end = "")

if DEBUG:
    print("")
    
"""
Name: get_random with no black_list
Target: URL.get_random()
Input: "sub/sub/subsub1.html"
Expected Output: random link from the URL object links
"""
for x in range(10):
    if DEBUG:
        print("Testing get_random: " + ROOT_URL + "sub/sub/subsub1.html")

    test_url = cu.URL()
    test_url = cu.get_links(ROOT_URL + "sub/sub/subsub1.html")

    test_random = test_url.get_random()

    #check for failures
    if DEBUG:
        print("Checking random link in URL object (True): ", end = "")

    try:
        assert(test_random in test_url.links)
    
        passed += 1
    
        if DEBUG:
            print("True")
            print("PASSED\n\n")
    except AssertionError:
    
        failed += 1
    
        if DEBUG:
            print("False")
            print("FAILED\n\n")

    del test_url

"""
Name: get_random with black_list
Target: URL.get_random()
Input: "sub/sub/subsub1.html"
Expected Output: "random" link (badlink.html) from the URL object links
"""
for x in range(10):
    if DEBUG:
        print("Testing get_random: " + ROOT_URL + "sub/sub/subsub1.html")

    test_url = cu.URL()
    test_url = cu.get_links(ROOT_URL + "sub/sub/subsub1.html")

    #build blacklist for testing (all of subsub1.html links except badlink.html)

    test_black_list = [
        ROOT_URL + "relative.html",
        ROOT_URL + "index.html",
        ROOT_URL + "nolinks.html",
        ROOT_URL + "sub/sub1.html",
    ]

    test_random = test_url.get_random(test_black_list)

    #check for failures
    if DEBUG:
        print("Checking random link in URL object (badlink.html): ", end = "")

    try:
        assert(test_random == ROOT_URL + "badlink.html")
    
        passed += 1
    
        if DEBUG: 
            print(str(test_random))
            print("PASSED\n\n")

    except AssertionError:
    
        failed += 1
    
        if DEBUG:
            print(str(test_random))
            print("FAILED\n\n")

    del test_url


"""
Name: get_random with full black_list
Target: URL.get_random()
Input: "sub/sub/subsub1.html"
Expected Output: None (all links are in black_list)
"""
for x in range(10):
    if DEBUG:
        print("Testing get_random: " + ROOT_URL + "sub/sub/subsub1.html")

    test_url = cu.URL()
    test_url = cu.get_links(ROOT_URL + "sub/sub/subsub1.html")

    #build blacklist for testing (all of subsub1.html links)

    test_black_list = [
        ROOT_URL + "relative.html",
        ROOT_URL + "index.html",
        ROOT_URL + "nolinks.html",
        ROOT_URL + "sub/sub1.html",
        ROOT_URL + "badlink.html"
    ]

    test_random = test_url.get_random(test_black_list)

    #check for failures
    if DEBUG:
        print("Checking random link in URL object (None): ", end = "")

    try:
        assert(test_random == None)
    
        passed += 1
    
        if DEBUG:
            print(str(test_random))
            print("PASSED\n\n")

    except AssertionError:
    
        failed += 1
    
        if DEBUG:
            print(str(test_random))
            print("FAILED\n\n")

    del test_url


print("PASSED: %d FAILED: %d" % (passed, failed))