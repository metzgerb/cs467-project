#!/usr/bin/env python3

"""Program Name: Url.py
Python Version: 3
Description: Holds the URL class for crawlutil.py
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-26
Last Modified: 2019-11-01
"""

#dependencies
import random

"""
Class Name: URL
Description: Has variables for tracking the data of URL as it is crawled
Member functions: __str__ (used to output the current data in the URL for logging)
    __init__ (used for initializing an empty URL object)
    get_random (used for getting a random url)
"""
class URL():
    def __init__(self, url = None):
        self.url = url
        self.status = None
        self.parent = None
        self.key = False
        self.links = []
    
    #output string format designed by Christopher Beall
    def __str__(self):
        #store URL
        response = '{"URL: '
        if self.url:
            response += self.url
        #store Status
        response += ',"STATUS": '
        if self.status:
            response += str(self.status)
        #store parent
        response += ',"Parent": '
        if self.parent:
            response += self.parent
        #store keyword
        response += ',"Keyword Found": '
        if self.key:
            response += "True"
        else:
            response += "False"
        #store links
        response += ',"LINKS": ['
        response += ', '.join(self.links)
        response += ']}'

        return response

    """
    Function Name: get_random
    Description: returns a random URL from a URL class objects' links
    Inputs: takes an optional list of URL strings that should not be chosen
    Outputs: returns a string representing a URL or None
    """
    def get_random(self, black_list = []):
        #copy links that do not appear in black_list
        #source: https://stackoverflow.com/questions/4211209/remove-all-the-elements-that-occur-in-one-list-from-another
        rand_links = [x for x in self.links if x not in black_list]

        #check if any links remaining
        if len(rand_links) > 0:
            return rand_links[random.randint(0,len(rand_links)- 1)]
        #no links remain to choose from
        else:
            return None
    __repr__ = __str__
