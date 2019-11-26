#!/usr/bin/env python3

"""Program Name: test_get_robots.py
Python Version: 3
Description: Runs tests for the get_robots function in crawlutil.py
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-11-16
Last Modified: 2019-11-16
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

print("Running get_robots() tests...", end = "")

if DEBUG:
    print("")
    
"""
Name: get_robots with URL missing robots.txt
Target: crawlutil.get_robots()
Input: "https://web.engr.oregonstate.edu/~metzgerb/crawler/index.html"
Expected Output: parser = None
"""
if DEBUG:
    print("Testing robots: " + ROOT_URL + "index.html")

test = cu.get_robots(ROOT_URL + "index.html")

#check for failures
if DEBUG:
    print("Checking output (empty): ", end = "")

try: 
    test = str(test).strip()
    assert(test == "")
    
    if DEBUG:
        print(test)
        
    passed += 1
    
    if DEBUG:
        print("PASSED\n\n")

except AssertionError:
    failed += 1
    if DEBUG:
        print("FAILED\n\n")


"""
Name: get_robots with URL missing robots.txt
Target: crawlutil.get_robots()
Input: "https://www.google.com/"
Expected Output: valid parser object
"""
if DEBUG:
    print("Testing robots: https://www.google.com/")

test = cu.get_robots("https://www.google.com/")

#check for failures
if DEBUG:
    print("Checking output (Not None): ", end = "")

try: 
    assert(test is not None)
    
    if DEBUG:
        print(test)
        
    passed += 1
    
    if DEBUG:
        print("PASSED\n\n")

except AssertionError:
    failed += 1
    if DEBUG:
        print("FAILED\n\n")


print("PASSED: %d FAILED: %d" % (passed, failed))