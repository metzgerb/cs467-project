#!/usr/bin/env python3

"""Program Name: LinkParser.py
Python Version: 3
Description: Holds the LinkParser class for crawlutil.py
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-26
Last Modified: 2019-11-11
"""

#dependencies
from html.parser import HTMLParser

"""
Class Name: LinkParser
Description: Inherited from HTMLParser, customizes tag parsing functions
Member functions: handle_starttag (collects all start tags)
    handle_startendtag (collects all self closing tags)
    handle_data (collects data and searches for keywords)
"""
class LinkParser(HTMLParser):
    
    def __init__(self, keyword = None):
        super().__init__()
        self.links = list()
        self.no_index = False
        self.keyword = keyword
        self.key_found = False
        self.title = None
        self.title_match = False
        
    #parses any starting HTML tag to add href data to links array
    #TODO: ADD META TAG CHECKING
    #ADD ATTR SEARCH FOR REL: NOFOLLOW
    def handle_starttag(self, tag, attrs):
        #capture only links
        if tag == 'a':
            #loop through attributes
            for attr in attrs:
                #loop through attributes
                if attr[0] == 'href':
                    self.links.append(attr[1])
        #set title flag if title tag found
        elif tag == "title":
            self.title_match = True
    
    #parses any self-closing HTML tag to add href data to links array
    #TODO: ADD META TAG CHECKING
    #ADD ATTR SEARCH FOR REL: NOFOLLOW
    def handle_startendtag(self, tag, attrs):
        #capture only links
        if tag == 'a':
            #loop through attributes
            for attr in attrs:
                #collect only hrefs
                if attr[0] == 'href':
                    self.links.append(attr[1])
    
    def handle_data(self, data):
        #check if title found
        if self.title_match:
            self.title = data
            self.title_match = False
        
        #check data for keyword if specified, and if keyword has not already been found
        if not self.key_found and self.keyword and self.keyword.lower() in data.lower():
            self.key_found = True
            
    
    #used to reset the instance of the class
    def reset_parser(self):
        self.links = []
        self.no_index = False
        self.key_found = False
        self.title = None
        self.title_match = False