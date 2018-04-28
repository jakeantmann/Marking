# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:07:09 2018

@author: User
"""

def readtxt(txtfile):
	in_file = open(txtfile, "rt") # open file lorem.txt for reading text data
	contents = in_file.read()         # read the entire file into a string variable
	in_file.close()                   # close the file
	return contents