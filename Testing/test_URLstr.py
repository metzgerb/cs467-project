#!/usr/bin/env python3

"""Program Name: test_get_links.py
Python Version: 3
Description: Runs tests for the get_links function in crawlutil.py
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-19
Last Modified: 2019-11-16
"""


#import dependencies
import sys, os

#add package path to syspath
sys.path.append(os.path.join(os.getcwd(),'crawlutil'))

import crawlutil as cu

ROOT_URL = "https://web.engr.oregonstate.edu/~metzgerb/crawler/"

test_url = cu.URL()
test_url = cu.get_links(ROOT_URL + "index.html")

print(test_url)