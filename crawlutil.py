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
from html.parser import HTMLParser

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
Class Name: LinkParser
Description: Inherited from HTMLParser, customizes tag parsing functions
Member functions: handle_starttag (collects all start tags)
    handle_startendtag (collects all self closing tags)
"""
class LinkParser(HTMLParser):
    links = list()
    
    def handle_starttag(self, tag, attrs):
        #capture only links
        if tag == 'a':
            #loop through attributes
            for attr in attrs:
                #loop through attributes
                if attr[0] == 'href':
                    self.links.append(attr[1])

    def handle_startendtag(self, tag, attrs):
        #capture only links
        if tag == 'a':
            #loop through attributes
            for attr in attrs:
                #collect only hrefs
                if attr[0] == 'href':
                    self.links.append(attr[1])


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
        parser = LinkParser()
        parser.feed(response.text)
        
        #filter HTML to hrefs only
        for link in parser.links:
            print(link)
        
        #iterate through hrefs and create dictionary of URLs
            #convert relative URLs
    
    return link