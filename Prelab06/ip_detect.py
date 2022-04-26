#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-02-21 21:48:26 -0500 (Sun, 21 Feb 2016) $
#$Revision: 88534 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab06/ip_detect.py $
#$Id: ip_detect.py 88534 2016-02-22 02:48:26Z ee364b13 $

import os
import sys
import re

def detect(filename):
    with open(filename, 'r') as f:
        for line in f:
            validip = all((ip.isdigit() and int(ip) <= 255) for ip in re.split(r"[.|:]", line.strip())[0:-1])
            port = line.strip().split(":")[-1]
            validport = port.isdigit() and int(port) <= 32767 and int(port) >= 1

            result = line.strip()
            if validip:
                if validport:
                    result += " - Valid (root privileges required)"
                else:
                    result += " - Invalid Port Number"
            else:
                result += " - Invalid IP Address"
            print(result)

    return None


if __name__ == "__main__":
    if not (len(sys.argv) == 2):
        print("Usage: ip_detect.py <filename>")
    else:
        filename = sys.argv[1]
        detect(filename)