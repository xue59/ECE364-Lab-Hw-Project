#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-02-21 21:48:26 -0500 (Sun, 21 Feb 2016) $
#$Revision: 88534 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab06/function_finder.py $
#$Id: function_finder.py 88534 2016-02-22 02:48:26Z ee364b13 $
import os
import sys
import re

def finder(filename):
    readable = check(filename)
    if not readable:
        print ("Error: Could not read " + filename)
        return
    with open(filename, 'r') as f:
        for line in f:
            func = re.match(r"def (.*)\((.*)\)", line)
            if not func:
                continue
            name = func.group(1)
            args = func.group(2).split(",")
            print(name)
            i = 1;
            for arg in args:
                start = "Arg"+str(i)+": "
                print (start + arg.strip())
                i += 1
    return

def check(filename):
    return os.access(filename, os.R_OK)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: function_finder.py [python_file_name]")
    else:
        finder(sys.argv[1])