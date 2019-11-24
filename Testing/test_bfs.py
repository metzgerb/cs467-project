#!/usr/bin/env python3

"""Program Name: test_bfs.py
Python Version: 3
Description: Runs tests to check the BFS function in crawlutil.py
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-11-08
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

print("Running BFS tests...", end = "")

if DEBUG:
    print("")

"""
Name: breadth_search with index.html
Target: crawlutil.breadth_search()
Input: "index.html" limit = 1
Expected Output: Tree containing 6 links
"""
if DEBUG:
    print("Testing BFS with depth of 1: " + ROOT_URL + "index.html")

test_tree = cu.breadth_search(ROOT_URL + "index.html", 1)
tree_list = []

for link in test_tree:
    tree_list.append(link.url)

test_list = [
        ROOT_URL + "index.html",
        ROOT_URL + "relative.html",
        ROOT_URL + "nolinks.html",
        ROOT_URL + "sub/sub1.html",
        ROOT_URL + "sub/sub/subsub1.html",
        ROOT_URL + "badlink.html",
    ]
    

#check for failures
if DEBUG:
    print("Checking output (6 links): ", end = "")

try:        
    assert(tree_list == test_list)
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
Name: breadth_search with root.html
Target: crawlutil.breadth_search()
Input: "root.html" limit = 1
Expected Output: Tree containing 3 links
"""
if DEBUG:
    print("Testing BFS with depth of 1: " + ROOT_URL + "root.html")

test_tree = cu.breadth_search(ROOT_URL + "root.html", 1)
tree_list = []

for link in test_tree:
    tree_list.append(link.url)

test_list = [
        ROOT_URL + "root.html",
        ROOT_URL + "1depth-1.html",
        ROOT_URL + "1depth-2.html",
    ]
    
#check for failures
if DEBUG:
    print("Checking output (3 links): ", end = "")

try:        
    assert(tree_list == test_list)
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
Name: breadth_search with root.html
Target: crawlutil.breadth_search()
Input: "root.html" limit = 2
Expected Output: Tree containing 6 links
"""
if DEBUG:
    print("Testing BFS with depth of 2: " + ROOT_URL + "root.html")

test_tree = cu.breadth_search(ROOT_URL + "root.html", 2)
tree_list = []

for link in test_tree:
    tree_list.append(link.url)

test_list = [
        ROOT_URL + "root.html",
        ROOT_URL + "1depth-1.html",
        ROOT_URL + "1depth-2.html",
        ROOT_URL + "2depth-1.html",
        ROOT_URL + "2depth-2.html",
        ROOT_URL + "2depth-3.html",
    ]

#check for failures
if DEBUG:
    print("Checking output (6 links): ", end = "")

try:        
    assert(tree_list == test_list)
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
Name: breadth_search with root.html
Target: crawlutil.breadth_search()
Input: "root.html" limit = 3
Expected Output: Tree containing 10 links
"""
if DEBUG:
    print("Testing BFS with depth of 3: " + ROOT_URL + "root.html")

test_tree = cu.breadth_search(ROOT_URL + "root.html", 3)
tree_list = []

for link in test_tree:
    tree_list.append(link.url)

test_list = [
        ROOT_URL + "root.html",
        ROOT_URL + "1depth-1.html",
        ROOT_URL + "1depth-2.html",
        ROOT_URL + "2depth-1.html",
        ROOT_URL + "2depth-2.html",
        ROOT_URL + "2depth-3.html",
        ROOT_URL + "relative.html",
        ROOT_URL + "index.html",
        ROOT_URL + "sub/sub1.html",
        ROOT_URL + "sub/sub/subsub1.html",
    ]
    
#check for failures
if DEBUG:
    print("Checking output (10 links): ", end = "")

try:        
    assert(tree_list == test_list)
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
Name: breadth_search with root.html with keyword "aardvark"
Target: crawlutil.breadth_search()
Input: "root.html" limit = 3 keyword = "aardvark"
Expected Output: Tree containing 5 links
"""
if DEBUG:
    print("Testing BFS with depth of 3: " + ROOT_URL + "root.html")

test_tree = cu.breadth_search(ROOT_URL + "root.html", 3, "aardvark")
tree_list = []

for link in test_tree:
    tree_list.append(link.url)

test_list = [
        ROOT_URL + "root.html",
        ROOT_URL + "1depth-1.html",
        ROOT_URL + "1depth-2.html",
        ROOT_URL + "2depth-1.html",
        ROOT_URL + "2depth-2.html",
    ]
    
#check for failures
if DEBUG:
    print("Checking output (5 links): ", end = "")

try:        
    assert(tree_list == test_list)
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
Name: breadth_search with google.com using disallow in robots.txt
Target: crawlutil.breadth_search()
Input: "google.com/groups " limit = 3
Expected Output: Tree containing 0 links
"""
if DEBUG:
    print("Testing BFS with depth of 3: " + ROOT_URL + "root.html")

test_tree = cu.breadth_search("https://www.google.com/groups", 3)
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


print("PASSED: %d FAILED: %d" % (passed, failed))