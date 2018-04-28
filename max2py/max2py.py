import os
import re
from subprocess import Popen

# Turns a list of strings into a txt document
def list2txt(thelist, name, directory):
    os.chdir(directory)
    
    thefile = open(name, 'w+')
    for item in thelist:
        thefile.write("%s\n" % item)
    thefile.close()

# Runs a batch file
def batchrun(name, directory):
    p = Popen(name, cwd=directory)
    stdout, stderr = p.communicate()

# Reads in a txt file
def readtxt(txtfile):
	in_file = open(txtfile, "rt") # open file lorem.txt for reading text data
	contents = in_file.read()         # read the entire file into a string variable
	in_file.close()                   # close the file
	return contents

# Extracts the relevant output
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

	
	
	
	
	
	
	
	
	
	
	
	
list1 = ["a:2;", "b:3;", "a+b;"]











list2txt(list1,"input.txt",r"C:\Users\User\Desktop\Marking\max2py")
batchrun('pipe.bat',r'C:\Users\User\Desktop\Marking\max2py')
output=maxima_reader('output.txt',3)
print(output)

































