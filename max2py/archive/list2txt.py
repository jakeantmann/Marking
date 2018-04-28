## Turns a list of strings into a txt file
# thelist must be a list of strings
# name must be a string ending in .txt
# directory must be of form: r"C:\Users\User\Dropbox\Personal\Sandbox\list2txt"

def list2txt(thelist, name, directory):
    import os
    os.chdir(directory)
    
    thefile = open(name, 'w+')
    for item in thelist:
        thefile.write("%s\n" % item)
    thefile.close()