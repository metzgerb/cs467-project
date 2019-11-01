#!/usr/bin/env python3

"""Program Name: crawl.py
Python Version: 3
Description: URL crawling program that can search DFS or BFS through links.
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-17
Last Modified: 2019-11-01
"""

#import dependencies
import sys, os
sys.path.append(os.path.join(os.getcwd(),'crawlutil')) #add package path to syspath
import crawlutil.crawlutil as cu

"""
Function Name: main
Description: The main controlling program of the crawler. 
Inputs: takes a string representing the starting URL, a char flag for type of 
    search, an integer representing the link limit and an optional keyword for
    halting the search
Outputs: ???
"""
def main(url, search_type, link_limit, keyword = None):   
    #Validate variables
    
    #branch based on DFS or BFS (Use different functions for each, general flow below)
    if True:
        tree = cu.depth_search(url, link_limit, keyword)
    else:
        #TODO: change to breadth first search once written
        tree = cu.depth_search(url, link_limit, keyword)
                
    #log the resulting output
    for node in tree:
        print(node)
    
    return 0

if __name__ == "__main__":
    #check number of arguments
    if len(sys.argv) == 4 and sys.argv[3].isnumeric():
        #sys.exit(main("https://web.engr.oregonstate.edu/~metzgerb/crawler/index.html","2",5))
        sys.exit(main(sys.argv[1],sys.argv[2],int(sys.argv[3])))
    #keyword provided
    elif len(sys.argv) == 5 and sys.argv[3].isnumeric():
        #sys.exit(main("https://web.engr.oregonstate.edu/~metzgerb/crawler/index.html","2",5,"turkey"))
        sys.exit(main(sys.argv[1],sys.argv[2],int(sys.argv[3]),sys.argv[4]))
    else:
        #exit with code 1
        sys.exit(1)
    