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
from Url import URL
from LinkParser import LinkParser

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