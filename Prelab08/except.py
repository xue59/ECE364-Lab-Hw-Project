#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-03-06 15:16:23 -0500 (Sun, 06 Mar 2016) $
#$Revision: 89413 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab08/except.py $
#$Id: except.py 89413 2016-03-06 20:16:23Z ee364b13 $


def find_sum(values):
    sum = 0
    for value in values:
        try:
            sum += float(value)
        except (ValueError):
            pass
        finally:
            pass
    return sum

if __name__ == "__main__":
    values = input("Please enter some values: ").split()
    print("The sum is:", find_sum(values))