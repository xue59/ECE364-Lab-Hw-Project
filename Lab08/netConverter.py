#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-03-08 14:31:19 -0500 (Tue, 08 Mar 2016) $
#$Revision: 89545 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Lab08/netConverter.py $
#$Id: netConverter.py 89545 2016-03-08 19:31:19Z ee364b13 $

from HardwareTasks import *

def verilog2vhdl(ver_line):
    err = "Error: Bad Line."
    try:
        cia = processLine(ver_line)
    except (ValueError):
        return err
    else:
        c, i ,at = cia
        string = i + ": " + c + " PORT MAP("
        list = []
        for a in at:
            list.append(a[0]+"=>"+a[1])
        i = 0
        for x in list:
            if i == (len(list) - 1):
                string += list[i] + ");"
            else:
                string += list[i] + ", "
            i += 1
        return string
    finally:
        pass
    return None


def convertNetlist(sourceFile, targetFile):
    vhdl = []
    with open(sourceFile, "r") as f:
        for l in f:
            vhdl.append(verilog2vhdl(l) + "\n")
    g = open(targetFile, "w")
    vhdl[-1] = vhdl[-1].strip()
    for mike in vhdl:
        g.write(mike)


if __name__ == "__main__":
    pass