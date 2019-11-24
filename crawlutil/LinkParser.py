#!/usr/bin/env python3

"""Program Name: LinkParser.py
Python Version: 3
Description: Holds the LinkParser class for crawlutil.py
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-26
Last Modified: 2019-11-16
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
        self.no_follow = False
        self.keyword = keyword
        self.key_found = False
        self.title = None
        self.title_match = False
        
        
    #parses any starting HTML tag to add href data to links array
    #also adds title information and checks for nofollow tags
    def handle_starttag(self, tag, attrs):
        #set title flag if title tag found
        if tag == "title":
            self.title_match = True
        
        #check no_follow
        if self.no_follow:
            #skip all links on page
            return
        
        #capture only links
        elif tag == 'a':
            #check for rel attribute 
            #source:https://www.deepcrawl.com/blog/best-practice/noindex-disallow-nofollow/
            for attr in attrs:
                if attr[0] == 'rel' and 'nofollow' in attr[1].lower():
                    #skip adding to list of links
                    return
            
            #find href attribute
            for attr in attrs:
                #loop through attributes
                if attr[0] == 'href':
                    self.links.append(attr[1])
                    
        #check if meta tag contains "nofollow"
        elif tag == 'meta':
            #check for robots meta tag 
            #source:https://www.deepcrawl.com/blog/best-practice/noindex-disallow-nofollow/
            for attr in attrs:
                if attr[0] == 'name' and attr[1].lower() == 'robots':
                    #check content
                    for attr in attrs:
                        #check if attr is content and contains "nofollow"
                        if attr[0] == 'content' and 'nofollow' in attr[1].lower():
                            self.no_follow = True
    
    
    #parses any self-closing HTML tag to add href data to links array
    #also checks for nofollow tags
    def handle_startendtag(self, tag, attrs):
        #check if no_follow is set
        if self.no_follow:
            #skip all links on page
            return
        
        #capture only links
        elif tag == 'a':
            #check for rel attribute
            #source:https://www.deepcrawl.com/blog/best-practice/noindex-disallow-nofollow/
            for attr in attrs:
                if attr[0] == 'rel' and 'nofollow' in attr[1].lower():
                    #skip adding to list of links
                    return
            
            #find href attribute
            for attr in attrs:
                #collect only hrefs
                if attr[0] == 'href':
                    self.links.append(attr[1])
        
        #check if meta tag contains "nofollow"
        #source:https://www.deepcrawl.com/blog/best-practice/noindex-disallow-nofollow/
        elif tag == 'meta':
            #check for robots meta tag
            for attr in attrs:
                if attr[0] == 'name' and attr[1].lower() == 'robots':
                    #check content
                    for attr in attrs:
                        #check if attr is content and contains "nofollow"
                        if attr[0] == 'content' and 'nofollow' in attr[1].lower():
                            self.no_follow = True
    
    
    #parses data and store title while searching for keyword
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
        self.no_follow = False
        self.key_found = False
        self.title = None
        self.title_match = False