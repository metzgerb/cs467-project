#!/usr/bin/env python3

"""Program Name: test_keywords.py
Python Version: 3
Description: Runs tests to check the get_random function of the URL class used
    in crawlutil.py
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-26
Last Modified: 2019-11-03
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
        
        #sort lists
        test_random.sort()
        test_url.links.sort()
        
        assert(test_random == test_url.links)
    
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


print("PASSED: %d FAILED: %d" % (passed, failed))