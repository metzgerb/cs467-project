#!/usr/bin/env python3

"""Program Name: crawlutil.py
Python Version: 3
Description: Utility functions for URL crawling program.
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-17
Last Modified: 2019-10-19
"""

#import dependencies
import requests
from lxml import html

"""
Class Name: URL
Description: Has variables for tracking the data of URL as it is crawled
Member functions: __str__ (used to output the current data in the URL for logging)
        __init__ (used for initializing an empty URL object)
"""
class URL():
    def __init__(self, url):
        self.url = url
        self.status = None
        self.parent = None
        self.links = {}
    
    def __str__(self):
        #TODO: define output for logging (work with Christopher)
        print(self.url)
        print(self.status)
        print(self.parent)
        for link in links:
            print(link)

"""
Function Name: get_links
Description: Makes HTML Get request of provided link and parses all link tags 
    to extract the href 
Inputs: takes a string representing a URL to be crawled, and an optional string
    representing the parent url the link was followed from
Outputs: returns a URL object
"""
def get_links(url, parent = None):
    #create URL object and set parent
    link = URL(url)
    link.parent = parent
    
    #make get request
    response = requests.get(link.url)
    
    #set status
    link.status = response.status_code
    
    #TODO: check for no index meta tag in header
    
    #check for errors from response
    if response:
        #parse HTML content
        body = html.fromstring(response.content)
        print(body)
        #filter HTML to hrefs only
        
        #iterate through hrefs and create dictionary of URLs
            #convert relative URLs
    
    return link