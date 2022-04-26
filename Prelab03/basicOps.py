#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-01-31 21:17:26 -0500 (Sun, 31 Jan 2016) $
#$Revision: 87354 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab03/basicOps.py $
#$Id: basicOps.py 87354 2016-02-01 02:17:26Z ee364b13 $

def addNumbers(num):
    i = 0
    sum = 0
    while i <= num:
        sum += i
        i += 1
    return sum


def addMultiplesOf(num):
    i = 0
    sum = 0
    while i <= 1000:
        sum += i
        i += num
    return sum

def getNumberFrequency(num):
    body = "The value of Pi is 3 . 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7 4 9 4 4 5 9 2 3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8 2 5 3 4 2 1 1 7 0 6 7 9 8 2 1 4 8 0 8 6 5 1 3 2 8 2 3 0 6 6 4 7 0 9 3 8 4 4 6 0 9 5 5 0 5 8 2 2 3 1 7 2 5 3 5 9 4 0 8 1 2 8 4 8 1"
    freq = 0
    for i in body:
        if i == str(num):
            freq += 1
    return freq

def getDigitalSum(din):
    sum = 0
    for i in din:
        sum += int(i)
    return sum

def getSequenceWithoutDigit(num):
    strList = ["736925233695599303035509581762617623184956190649483967300203776387436934399982",
                "943020914707361894793269276244518656023955905370512897816345542332011497599489",
                "627842432748378803270141867695262118097500640514975588965029300486760520801049",
                "153788541390942453169171998762894127722112946456829486028149318156024967788794",
                "981377721622935943781100444806079767242927624951078415344642915084276452000204",
                "276947069804177583220909702029165734725158290463091035903784297757265172087724",
                "474095226716630600546971638794317119687348468873818665675127929857501636341131"]
    strList = "".join(strList)
    start = 0
    ind = 0
    mystr = ""
    maxlen = 0
    for i in strList:
        if i == str(num):
            tempstr = strList[start:ind]
            if len(tempstr) > maxlen:
                mystr = tempstr
                maxlen = len(tempstr)
            start = ind + 1
        ind += 1
    return mystr


def capitalizeMe(userString):
    ind = 0
    newStr= ""
    while ind < len(userString):
        if (ind == 0) or (ind == len(userString) - 1):
            newStr += userString[ind].upper()
        elif (userString[ind - 1] == " ") or (userString[ind + 1] == " "):
            newStr += userString[ind].upper()
        else:
            newStr += userString[ind]
        ind += 1
    return newStr

if __name__ == '__main__':
    pass