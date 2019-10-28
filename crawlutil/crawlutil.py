#!/usr/bin/env python3

"""Program Name: crawlutil.py
Python Version: 3
Description: Utility functions for URL crawling program.
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-17
Last Modified: 2019-10-20
"""

#import dependencies
import urllib.request
import urllib.parse
from html.parser import HTMLParser

"""
Class Name: URL
Description: Has variables for tracking the data of URL as it is crawled
Member functions: __str__ (used to output the current data in the URL as JSON)
        __init__ (used for initializing an empty URL object)
"""
class URL():
    def __init__(self, url = "null"):
        self.url = url
        self.status = None
        self.parent = None
        self.key = False
        self.links = []
    
    def __str__(self):
        #TODO: define output for logging (work with Christopher)
        response = '{"URL: ' 
        if self.url:
            response += self.url
            
        response += ',"STATUS": '
        if self.status:
            response += str(self.status)
        
        response += ',"Parent": ' 
        if self.parent:
            response += self.parent
        
        response += ',"Keyword Found": ' 
        if self.key:
            response += "True"
        else:
            response += "False"
        
        response += ',"LINKS": ['
        response += ', '.join(self.links)
        response += ']}'

        return response


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
    
    #used to reset the instance
    def reset_links(self):
        self.links = []


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
    response = urllib.request.urlopen(link.url)
    
    #set status
    link.status = response.getcode()
    
    
    #read response data
    page = str(response.read())
    
    #TODO: search for keyword and set keyword flag
    
    #TODO: check for no index meta tag in header
    
    #check for errors from response
    if response:
        #parse HTML content
        parser = LinkParser()
        parser.reset_links()
        parser.feed(page)

        #assign to URL object
        link.links = parser.links.copy()
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


def output_links(url_list):
    """
    THis will loop through a list of URL objects and form them into one large JSON string, and then print this string to 
    stdout
    IN: An array of URL objects
    OUT: A string that should be in JSON format.
    """
    json_string = "["
    comma_join = ', '.join(url_list)
    json_string += comma_join
    json_string += ']'
    print(json_string)
