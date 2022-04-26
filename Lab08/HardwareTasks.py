#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-03-08 14:31:19 -0500 (Tue, 08 Mar 2016) $
#$Revision: 89545 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Lab08/HardwareTasks.py $
#$Id: HardwareTasks.py 89545 2016-03-08 19:31:19Z ee364b13 $

import re


def idIsAcceptable(ver_id):
    match = re.match("^\s*\w+\s*$", ver_id)
    if match:
        return True
    return False


def processSingle(ver_assignment):
    match = re.match("^\s*\.(\w+)\((\w+)\)\s*$", ver_assignment)
    if not match:
        raise ValueError
    port = match.group(1)
    pin = match.group(2)
    t = (port, pin)
    return t

def processLine(ver_line):
    match = re.match("^\s*(\w+)\s+(\w+)\s*\((.*)\)\s*$", ver_line)
    if not match:
        raise ValueError
    comp = match.group(1)
    inst = match.group(2)
    if (not idIsAcceptable(comp)) or (not idIsAcceptable(inst)):
        raise ValueError
    assign = match.group(3)
    assign_list = [y.strip() for y in assign.split(",")]
    temp = []
    for x in assign_list:
        try:
            k = processSingle(x)
        except (ValueError):
            raise ValueError
        else:
            temp.append(k)
        finally:
            pass

    t = (comp, inst, tuple(temp))
    return t


if __name__ == "__main__":
    pass