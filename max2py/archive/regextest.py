# Extract Maxima outputs from a .txt file

import re

def readtxt(txtfile):
	in_file = open(txtfile, "rt") # open file lorem.txt for reading text data
	contents = in_file.read()         # read the entire file into a string variable
	in_file.close()                   # close the file
	return contents

def maxima_reader(txtfile,n_outputs):
    inputstring = readtxt(txtfile) 
    output_list=[None] * n_outputs
    pre = '(\(\%o'
    post = '\))(.*?)(\\n)'
    for i in range(n_outputs):
        mid=str(i+1)
        reg=pre+mid+post
        myRegex = re.compile(reg)
        mo = myRegex.search(inputstring)
        output_list[i]=mo.group(2)
        output_list[i]=output_list[i].replace(" ", "")
    return output_list

