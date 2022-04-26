#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-01-31 22:34:54 -0500 (Sun, 31 Jan 2016) $
#$Revision: 87361 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab03/moreBasics.py $
#$Id: moreBasics.py 87361 2016-02-01 03:34:54Z ee364b13 $

def getAverage(l):
    return sum(l)/len(l)

def getHeadAverage(l, n):
    return sum(l[0:n])/n

def getTailMax(l, m):
    l2 = l[-m:-1]
    l2.append(l[-1])
    return max(l2)

def getNumberAverage(l):
    return sum(l)/len(l)

def getFormattedSSN(n):
    four = n % 10000
    two = int(((n - four) / 10000) % 100)
    three = int((n - two * 10000 - four) / 1000000)
    ssn = ""
    if three < 100:
        ssn += "0"
    if three < 10:
        ssn += "0"
    ssn += str(three) + "-"
    if two < 10:
        ssn += "0"
    ssn += str(two) + "-"
    if four < 1000:
        ssn += "0"
    if four < 100:
        ssn += "0"
    if four < 10:
        ssn += "0"
    ssn += str(four)
    return ssn

def findName(l, s):
    for i in l:
        new = i.split()
        for k in new:
            if k == s:
                return i
    return None

def getColumnSum(mat):
    result = [sum([row[i] for row in mat]) for i in range(0, len(mat[0]))]
    return result

def getFormattedNames(ln):
    i = 0
    while i < len(ln):
        ln[i] = ln[i][2] + ', ' + ln[i][0] + ' ' + ln[i][1] + '.'
        i = i + 1
    return ln

def getElementwiseSum(l1, l2):
    i = 0
    limit = len(l1)
    ll = l1
    l3 = l2
    if len(l2) < len(l1):
        limit = len(l2)
        ll = l2
        l3 = l1
    while i < limit:
        l3[i] = l3[i] + ll[i]
        i = i + 1
    return l3

def removeDuplicates(l):
    l2 = []
    for i in l:
        if not(i in l2):
            l2.append(i)
    return l2

def getMaxOccurrence(l):
    lnd = removeDuplicates(l)
    lfq = [0] * len(lnd)
    for i in l:
        if i in lnd:
            lfq[lnd.index(i)] += 1
    return max(lfq)

def getMaxProduct(l):
    max = 0
    i = 0
    while i < len(l) - 2:
        product = l[i] * l[i+1] * l[i+2]
        if product > max:
            max = product
        i += 1
    return max

if __name__ == '__main__':
    pass