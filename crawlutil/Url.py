#!/usr/bin/env python3

"""Program Name: Url.py
Python Version: 3
Description: Holds the URL class for crawlutil.py
Author: Brian Metzger (metzgerb@oregonstate.edu)
Course: CS467 (Fall 2019)
Created: 2019-10-26
Last Modified: 2019-11-11
"""

#dependencies
import random
import json

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
        self.title = None
        self.key = False
        self.links = []
    
    #output string format designed by Christopher Beall
    def __str__(self):
        """#store URL
        response = '{"URL": '
        if self.url:
            response += '"' + self.url + '"'
        #store Status
        response += ',"STATUS": '
        if self.status:
            response += '"' + str(self.status) + '"'
        #store Title
        response += ',"Title": '
        if self.title:
           response += '"' + self.title + '"'
        #store parent
        response += ',"Parent": '
        if self.parent:
            response += '"' + self.parent + '"'
        #store keyword
        response += ',"Keyword Found": '
        if self.key:
            response += '"True"'
        else:
            response += '"False"'
        #store links
        response += ',"LINKS": ['
        response += ','.join(['"' + link + '"' for link in self.links])
        response += ']}'
        """
        #source: https://docs.python.org/3/library/json.html
        #https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
        response = json.dumps(self, default=lambda o:o.__dict__)
        return response

    """
    Function Name: get_random
    Description: returns a randomized list of URLs from a URL class objects' links
    Inputs: Nothing
    Outputs: returns a randomized list of URLs or None
    """
    def get_random(self):
        #return shuffled links
        random.shuffle(self.links)
        return self.links
        

