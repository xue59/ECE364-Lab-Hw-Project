#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-03-06 15:16:23 -0500 (Sun, 06 Mar 2016) $
#$Revision: 89413 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab08/listmod.py $
#$Id: listmod.py 89413 2016-03-06 20:16:23Z ee364b13 $

from list import find_median

if __name__ == "__main__":
    list1_mapped = map(int, input("Enter the first list of numbers: ").split())
    list2_mapped = map(int, input("Enter the second list of numbers: ").split())
    list1 = list(list1_mapped)
    list2 = list(list2_mapped)
    print("First List:", list1)
    print("Second List:", list2)
    (Median, Sorted_List) = find_median(list1, list2)
    print("Merged List:", Sorted_List)
    print("Median:", Median)