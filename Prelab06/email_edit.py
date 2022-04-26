#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-02-21 21:48:26 -0500 (Sun, 21 Feb 2016) $
#$Revision: 88534 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab06/email_edit.py $
#$Id: email_edit.py 88534 2016-02-22 02:48:26Z ee364b13 $

import os
import sys
import re

def edit():
    filename = "Part2.in"

    with open(filename, 'r') as f:
        for line in f:
            matchStr = re.match(r'([\w.-]+)@([\w.-]+)', line)
            if matchStr.group(2) == "purdue.edu":
                print (re.sub(r'(.*)@(.*)', r'\1@ecn.\2/100', line.strip()))
    return None

if __name__ == "__main__":
    edit()