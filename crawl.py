#!/usr/bin/env python3

"""Program Name: crawl.py
Python Version: 3
Description: URL crawling program that can search DFS or BFS through links.
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-17
Last Modified: 2019-10-20
"""

#import dependencies
import crawlutil as cu

"""
Function Name: main
Description: The main controlling program of the crawler. 
Inputs: takes a string representing the starting URL, a char flag for type of 
    search, an integer representing the link limit and an optional keyword for
    halting the search
Outputs: ???
"""
def main(url, search_type, link_limit, keyword = None):
    print("main crawl function")
    
    #Validate variables
    
    #initialize any beginning variables
    
    #branch based on DFS or BFS (Use different functions for each, general flow below)
        #loop until out of links or link limit hit or until keyword found
            #get_links
            #choose random link to follow
                #apply BFS or DFS
                
    #log the resulting output
    #TODO: determine output with Christopher
    
    return 0

if __name__ == "__main__":
    #TODO: update once we determine what input will be from website/data transfer utility
    #may need if statement for when keyword not supplied?
    main("1","2","3")
    