#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-03-06 15:16:23 -0500 (Sun, 06 Mar 2016) $
#$Revision: 89413 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab08/parse.py $
#$Id: parse.py 89413 2016-03-06 20:16:23Z ee364b13 $
from sys import *

def parse_it(file):
    for l in file:
        line = l.split()
        sum = 0
        string = ""
        count = len(line)
        for num in line:
            try:
                sum += int(num)
            except (ValueError):
                string += num + " "
                count -= 1
            finally:
                pass
        try:
            avg = "%.3f " % (float(sum) / count)
        except (ZeroDivisionError):
            print(string)
        else:
            print(avg + string)
        finally:
            pass


if __name__ == "__main__":
    try:
        file = open(argv[1])
    except (IndexError):
        print("Usage: parse.py [filename]")
    except (IOError):
        err = argv[1] + " is not a readable file."
        print(err)
    else:
        parse_it(file)
    finally:
        pass

