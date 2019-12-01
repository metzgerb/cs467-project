#!/usr/bin/env python3

"""Program Name: crawlutil.py
Python Version: 3
Description: Utility functions for URL crawling program.
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-17
Last Modified: 2019-12-01
"""

#import dependencies
import urllib.request
import urllib.parse
#import urllib.robotparser
from Url import URL
from LinkParser import LinkParser
import BotParser
import time


"""
Function Name: get_robots
Description: Attempts to get and parse a robots.txt file for the domain 
Inputs: takes a string representing a URL to be crawled 
Outputs: returns RobotFileParser object or None if no robots.txt exists
"""
def get_robots(url):
    #parse url to get domain
    parsed_url = urllib.parse.urlparse(url, scheme="http")
    
    #check scheme
    bot_scheme = parsed_url.scheme
    if bot_scheme not in ["http", "https"]:
        bot_scheme = "http"
        
    #construct robots.txt url
    robots_url = bot_scheme + "://" + parsed_url.netloc + "/robots.txt"

    #check if valid url can be passed to parser
    if parsed_url.netloc == '':
        #set bot parser to empty
        rp = None
    else:
        #create robot parser
        #source: https://docs.python.org/3/library/urllib.robotparser.html
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
        
        #iterate through hrefs and convert relative URLs
        for i in range(len(link.links)):
            #takes base url and combines with link if link does not have base of its own
            link.links[i] = urllib.parse.urljoin(link.url, link.links[i])              
    
    return link


"""
Function Name: depth_search
Description: Uses a Depth First Search algorithm to construct a list of links
    that can be followed from 
Inputs: takes a string representing a URL to be crawled, an integer for the 
    maximum number of links to follow, and a string representing a keyword to 
    be searched for
Outputs: returns a list of URL objects, and a robots flag
"""
def depth_search(url, link_limit, keyword = None):
    #set link counter and initial variables
    links_visited = set()
    stack = [url]
    parent_stack = ["null"]
    tree = []
    start_time = time.time()
    robots_flag = False
    
    #loop until link_limit reached
    while len(links_visited) < link_limit and url is not None and stack:
        #check if timelimit reached
        if time.time()-start_time > 28:
            print("timeout")
            break
        
        #pop from stack
        vertex = stack.pop()
        parent = parent_stack.pop()
        #get robot parser
        robots = get_robots(vertex)
        
        #check if already visited or in robots.txt
        if vertex not in links_visited and robots is not None:
            #check if robots can't fetch
            if not robots.can_fetch("*", vertex) and not robots_flag:
                robots_flag = True
            else:
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
                    parent_stack.append(link.url)
            
                #check if keyword found
                if link.key:
                    break
        
    return tree, robots_flag
    
    
"""
Function Name: breadth_search
Description: Uses a Breadth First Search algorithm to construct a list of links
    that can be followed from 
Inputs: takes a string representing a URL to be crawled, an integer for the 
    maximum depth of links to follow, and a string representing a keyword to 
    be searched for
Outputs: returns a list of URL objects, and a robots flag
"""
def breadth_search(url, depth_limit, keyword = None):
    #set link counter and initial variables
    links_visited = set()
    queue = [url]
    parent = "null"
    tree = []
    depth = 0
    start_time = time.time()
    robots_flag = False
    
    #begin node increase counter at 1 in order to account for root
    #adapted from source: https://stackoverflow.com/questions/10258305/how-to-implement-a-breadth-first-search-to-a-certain-depth
    depth_increase_counter = 1
    pending_depth_increase = False
    
    #loop until link_limit reached
    while depth <= depth_limit and url is not None and queue:
        #check if timelimit reached
        if time.time()-start_time > 28:
            print("timeout", end = "")
            break
        
        #get vertex from queue and reduce counter
        vertex = queue.pop()
        depth_increase_counter -= 1
        
        #check if depth has increased
        if depth_increase_counter == 0:
            #increase depth 
            depth += 1
            pending_depth_increase = True
        
        #get robot parser
        robots = get_robots(vertex)
        
        #check if already visited or in robots.txt
        if vertex not in links_visited and robots is not None:
            #check if robots can't fetch
            if not robots.can_fetch("*", vertex) and not robots_flag:
                robots_flag = True
            else:
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
        
    return tree, robots_flag