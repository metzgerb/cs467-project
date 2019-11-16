#!/usr/bin/env python3

"""Program Name: crawlutil.py
Python Version: 3
Description: Utility functions for URL crawling program.
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-17
Last Modified: 2019-11-09
"""

#import dependencies
import urllib.request
import urllib.parse
#import urllib.robotparser
from Url import URL
from LinkParser import LinkParser
import BotParser

"""
Function Name: get_robots
Description: Attempts to get and parse a robots.txt file for the domain 
Inputs: takes a string representing a URL to be crawled 
Outputs: returns RobotFileParser object or None if no robots.txt exists
"""
def get_robots(url):
    #parse url to get domain
    parsed_url = urllib.parse.urlparse(url, scheme="http")
    
    #construct robots.txt url
    robots_url = parsed_url.scheme + "://" + parsed_url.netloc + "/robots.txt"

    #create robot parser
    #source: https://docs.python.org/3/library/urllib.robotparser.html
    #rp = urllib.robotparser.RobotFileParser()
    rp = BotParser.RobotFileParser()
    rp.set_url(robots_url)
    
    #parse robots.txt file
    rp.read()
        
    #return parser object
    return rp

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
    
    try:        
        #make get request
        response = urllib.request.urlopen(link.url)
        
        #set status
        link.status = response.getcode()        
    
    except urllib.error.HTTPError as e:
        #set response to nothing since an error occurred
        response = None
        #log the returned status code
        link.status = e.code
    
    #check for errors from response
    if response:      
        #read response data
        page = str(response.read())
        #remove any unwanted newlines prior to parsing
        page = page.replace("\\n","")
        
        #parse HTML content
        parser = LinkParser(keyword)
        parser.reset_parser()
        parser.feed(page)

        #check if no follow is set
        if not parser.no_follow:
            #assign links to URL object
            link.links = parser.links.copy()
        
        #check if keyword was found and store title
        link.key = parser.key_found
        link.title = parser.title
        parser.close()
        
        #parse original url
        parsed_url = urllib.parse.urlparse(link.url, scheme="http")
        
        #iterate through hrefs and convert relative URLs
        for i in range(len(link.links)):
            #check for empty string
            if len(link.links[i]) == 0:
                link.links[i] = parsed_url.scheme + "://" + parsed_url.netloc + link.links[i]
            
            #check for "/" or "?" at beginning
            elif link.links[i][0] == "/" or link.links[i][0] == "?":
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
            
            #account for relative links with no ./, ../, or / notation
            else:
                #parse link
                child_url = urllib.parse.urlparse(link.links[i], scheme="http")
                
                #check for empty networkloc
                if child_url.netloc == '':
                    #replace empty string with net location from original url
                    new_child = child_url._replace(netloc = parsed_url.netloc)
                    
                    #set original to new child
                    child_url = new_child
                
                #join child_url again
                link.links[i] = urllib.parse.urlunparse(child_url)
    
    return link


"""
Function Name: depth_search
Description: Uses a Depth First Search algorithm to construct a list of links
    that can be followed from 
Inputs: takes a string representing a URL to be crawled, an integer for the 
    maximum number of links to follow, a robots.txt parser and a string 
    representing a keyword to be searched for
Outputs: returns a list of URL objects
"""
def depth_search(url, link_limit, robots, keyword = None):
    #set link counter and initial variables
    links_visited = set()
    stack = [url]
    parent = "null"
    tree = []
    
    #loop until link_limit reached
    while len(links_visited) < link_limit and url is not None and stack:
        #pop from stack
        vertex = stack.pop()
        
        #check if already visited or in robots.txt
        if vertex not in links_visited and robots.can_fetch("*", vertex):
            #get initial link
            link = get_links(vertex, keyword, parent)
        
            #add link to list of visited and add to tree
            links_visited.add(vertex)
            tree.append(link)
        
            #get_random links
            random_links = link.get_random()
            
            #add to stack
            for l in random_links:
                stack.append(l)
            
            parent = link.url
            
            #check if keyword found
            if link.key:
                break
        
    return tree
    
    
"""
Function Name: breadth_search
Description: Uses a Breadth First Search algorithm to construct a list of links
    that can be followed from 
Inputs: takes a string representing a URL to be crawled, an integer for the 
    maximum depth of links to follow, a robots.txt parser and a string 
    representing a keyword to be searched for
Outputs: returns a list of URL objects
"""
def breadth_search(url, depth_limit, robots, keyword = None):
    #set link counter and initial variables
    links_visited = set()
    queue = [url]
    parent = "null"
    tree = []
    depth = 0
    
    #begin node increase counter at 1 in order to account for root
    #adapted from source: https://stackoverflow.com/questions/10258305/how-to-implement-a-breadth-first-search-to-a-certain-depth
    depth_increase_counter = 1
    pending_depth_increase = False
    
    #loop until link_limit reached
    while depth <= depth_limit and url is not None and queue:
        #get vertex from queue and reduce counter
        vertex = queue.pop()
        depth_increase_counter -= 1
        
        #check if depth has increased
        if depth_increase_counter == 0:
            #increase depth 
            depth += 1
            pending_depth_increase = True
        
        #check if already visited or in robots.txt
        if vertex not in links_visited and robots.can_fetch("*", vertex):
            #get initial link
            link = get_links(vertex, keyword, parent)
            
            #add link to list of visited and add to tree
            links_visited.add(vertex)
            tree.append(link)
            
            #add to back of queue
            for l in link.links:
                #add to queue
                queue.insert(0,l)
            
            #check if pending depth increase
            if pending_depth_increase:
                #set counter to what's already in the queue and reset flag
                depth_increase_counter = len(queue)
                pending_depth_increase = False
            
            parent = link.url
            
            #check if keyword found
            if link.key:
                break
        
    return tree