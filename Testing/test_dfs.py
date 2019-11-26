#!/usr/bin/env python3

"""Program Name: test_dfs.py
Python Version: 3
Description: Runs tests to check the DFS function in crawlutil.py
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-11-09
Last Modified: 2019-11-24
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

print("Running DFS tests...", end = "")

if DEBUG:
    print("")


"""
Name: depth_search with root.html
Target: crawlutil.depth_search()
Input: "root.html" limit = 3
Expected Output: Tree containing 3 links
"""
for x in range(10):
    if DEBUG:
        print("Testing DFS with depth of 3: " + ROOT_URL + "root.html")
    
    test_tree = cu.depth_search(ROOT_URL + "root.html", 3)
    tree_list = []

    for link in test_tree:
        tree_list.append(link.url)

    test_list1 = [
        ROOT_URL + "root.html",
        ROOT_URL + "1depth-1.html",
        ROOT_URL + "2depth-1.html",
    ]

    test_list2 = [
        ROOT_URL + "root.html",
        ROOT_URL + "1depth-2.html",
        ROOT_URL + "2depth-2.html",
    ]

    test_list3 = [
        ROOT_URL + "root.html",
        ROOT_URL + "1depth-2.html",
        ROOT_URL + "2depth-3.html",
    ]

    #check for failures
    if DEBUG:
        print("Checking output (3 links): ", end = "")

    try:        
        assert(tree_list == test_list1 or tree_list == test_list2 or tree_list == test_list3)
        passed += 1
    
        if DEBUG:
            print(str(len(tree_list)))
            print("PASSED\n\n")

    except AssertionError:
        failed += 1
        if DEBUG:
            print(str(len(tree_list)))
            print("FAILED\n\n")

    del test_tree


"""
Name: depth_search with root.html with keyword "monkey"
Target: crawlutil.depth_search()
Input: "root.html" limit = 3 keyword = "monkey"
Expected Output: Tree containing 2 or 3 links
"""
for x in range(10):
    if DEBUG:
        print("Testing DFS with depth of 3: " + ROOT_URL + "root.html")
    
    test_tree = cu.depth_search(ROOT_URL + "root.html", 3, "monkey")
    tree_list = []

    for link in test_tree:
        tree_list.append(link.url)

    test_list1 = [
        ROOT_URL + "root.html",
        ROOT_URL + "1depth-1.html",
        ROOT_URL + "2depth-1.html",
    ]

    test_list2 = [
        ROOT_URL + "root.html",
        ROOT_URL + "1depth-2.html",
    ]

    #check for failures
    if DEBUG:
        print("Checking output (3 or 2 links): ", end = "")

    try:        
        assert(tree_list == test_list1 or tree_list == test_list2)
        passed += 1
    
        if DEBUG:
            print(str(len(tree_list)))
            print("PASSED\n\n")

    except AssertionError:
        failed += 1
        if DEBUG:
            print(str(len(tree_list)))
            print("FAILED\n\n")

    del test_tree
    

"""
Name: depth_search with google.com using disallow in robots.txt
Target: crawlutil.depth_search()
Input: "root.html" limit = 3
Expected Output: Tree containing 0 links
"""
if DEBUG:
    print("Testing DFS with depth of 3: https://www.google.com/search")
    
test_tree = cu.depth_search("https://www.google.com/search", 3)
tree_list = []

for link in test_tree:
    tree_list.append(link.url)

#check for failures
if DEBUG:
    print("Checking output (0 links): ", end = "")

try:        
    assert(len(tree_list) == 0)
    passed += 1
    
    if DEBUG:
        print(str(len(tree_list)))
        print("PASSED\n\n")

except AssertionError:
    failed += 1
    if DEBUG:
        print(str(len(tree_list)))
        print("FAILED\n\n")

del test_tree
    
    
"""
Name: depth_search with google.com using allow in robots.txt
Target: crawlutil.depth_search()
Input: "root.html" limit = 3
Expected Output: Tree containing more than 0 links
"""
if DEBUG:
    print("Testing DFS with depth of 3: https://www.google.com/finance")

test_tree = cu.depth_search("https://www.google.com/finance", 3)
tree_list = []

for link in test_tree:
    tree_list.append(link.url)

#check for failures
if DEBUG:
    print("Checking output (> 0 links): ", end = "")

try:        
    assert(len(tree_list) > 0)
    passed += 1
    
    if DEBUG:
        print(str(len(tree_list)))
        print("PASSED\n\n")

except AssertionError:
    failed += 1
    if DEBUG:
        print(str(len(tree_list)))
        print("FAILED\n\n")

del test_tree    
    
print("PASSED: %d FAILED: %d" % (passed, failed))