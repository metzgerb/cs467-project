#!/usr/bin/env python3

"""Program Name: crawlutil.py
Python Version: 3
Description: Utility functions for URL crawling program.
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-17
Last Modified: 2019-10-26
"""

#import dependencies
import urllib.request
import urllib.parse
from html.parser import HTMLParser

"""
Class Name: URL
Description: Has variables for tracking the data of URL as it is crawled
Member functions: __str__ (used to output the current data in the URL for logging)
        __init__ (used for initializing an empty URL object)
"""
class URL():
    def __init__(self, url = None):
        self.url = url
        self.status = None
        self.parent = None
        self.key = False
        self.links = []
    
    def __str__(self):
        #TODO: define output for logging (work with Christopher)
        response = "URL: " 
        if self.url:
            response += self.url
            
        response += "\nSTATUS: "
        if self.status:
            response += str(self.status)
        
        response += "\nParent: " 
        if self.parent:
            response += self.parent
        
        response += "\nKeyword Found: " 
        if self.key:
            response += "True"
        else:
            response += "False"
        
        response += "\nLINKS:"
        for link in self.links:
            response += "\n" + link
        
        return response

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
        #check data for keyword if specified, and if keyword has not already been found
        if not self.key_found and self.keyword and self.keyword.lower() in data.lower():
            self.key_found = True
            
    
    #used to reset the instance of the class
    def reset_parser(self):
        self.links = []
        self.no_index = False
        self.key_found = False


"""
Function Name: get_links
Description: Makes HTML Get request of provided link and parses all link tags 
    to extract the href 
Inputs: takes a string representing a URL to be crawled, an optional string 
    representing a keyword to be searched for and an optional string 
    representing the parent url the link was followed from
Outputs: returns a URL object
"""
def get_links(url, keyword = None, parent = None):
    #create URL object and set parent
    link = URL(url)
    link.parent = parent
    
    #make get request
    response = urllib.request.urlopen(link.url)
    
    #set status
    link.status = response.getcode()
    
    #read response data
    page = str(response.read())
    
    #TODO: check for no index meta tag in header 
    #NEED TO LOOK INTO GETTING ROBOTS.TXT IN ADDITION TO PARSING META TAGS AND 
    #REL ATTRS IN LINKS: https://www.deepcrawl.com/blog/best-practice/noindex-disallow-nofollow/
    
    #check for errors from response
    if response:      
        #parse HTML content
        parser = LinkParser(keyword)
        parser.reset_parser()
        parser.feed(page)

        #check if no index is set
        if not parser.no_index:
            #assign links to URL object
            link.links = parser.links.copy()
        
        #check if keyword was found
        link.key = parser.key_found
        parser.close()
        
        #parse original url
        parsed_url = urllib.parse.urlparse(link.url, scheme="http")
        
        #iterate through hrefs and convert relative URLs
        for i in range(len(link.links)):
            #check for "/" beginning
            if link.links[i][0] == "/":
                #add scheme and networkloc to url
                link.links[i] = parsed_url.scheme + "://" + parsed_url.netloc + link.links[i]
            
            #check for "./" beginning
            elif link.links[i][:2] == "./":
                #add scheme, networkloc, and all but last part of path to url
                link.links[i] = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path[:parsed_url.path.rfind('/')] + link.links[i][1:]
            
            #check for "../" beginning
            elif link.links[i][:3] == "../":
                #split original path
                split_path = parsed_url.path.split("/")
                
                #delete original page from path
                del split_path[-1]
                
                #split link
                split_link = link.links[i].split("/")
                
                #iterate through links in reverse order
                j = len(split_link) - 1 
                while j >= 0:
                    #check for ".."
                    if split_link[j] == "..":
                        #remove from link
                        del split_link[j]
                    
                        #remove a directory from the original path
                        del split_path[-1]
                    
                    #reduce index counter
                    j -= 1
                
                #combine resulting original path and remaining link path with scheme and netloc
                link.links[i] = parsed_url.scheme + "://" + parsed_url.netloc + "/".join(split_path) + "/" + "/".join(split_link)
                
        #testing DELETE
        #print(link)
    
    return link