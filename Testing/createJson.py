"""
Program Name: createJson.py
Description: Used for testing the retrieval and sending of information between UNIX and website
Author: Christopher Beall (beallch@oregonstate.edu)
Course: CS467 (Fall 2019)
Last Modified: 2019-10-21
"""

#TODO: Currently this is just for testing, in the future it will be modified to use output from the crawler program


import sys
extra = sys.argv[1]
data  = '[{"URL": "'+extra+ '", "STATUS": "null", "Parent": "null", "Keyword Found": "False", "LINKS": ["null"]},'\
'{"URL": "www.ex.com", "STATUS": "null", "Parent":"'+extra+'", "Keyword Found": "False", "LINKS": ["null"]},'\
'{"URL": "www.ex2.com", "STATUS": "null", "Parent":"www.ex.com", "Keyword Found": "False", "LINKS": ["null"]}]'

print(data)
