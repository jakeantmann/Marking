What I can now do:

(list2txt) Run a .txt file through Maxima using a batch file
(list2txt) Capture the output
(readtxt) Read the output using python
(maxima_reader) Convert the output into a list of output strings

Demonstration:
 - 

Why did I make this?
 - Part of final infrastructure, not for testing Maxima
 - For turning .txt file into usable output
 - Created early because was uncertain

Where does this sit in final infrastructure?
Process:
(Front-end) - Student answer received as CAS code
	    - Python inserts unedited student answer into .txt file
 (list2txt) - .txt file is run through Maxima, output captured
      (3,4) - output is turned into a list of strings
	    - output is turned into TeX
(Front-end) - TeX is sent back to student