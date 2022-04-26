#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-02-02 14:47:58 -0500 (Tue, 02 Feb 2016) $
#$Revision: 87525 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Lab03/simpleTasks.py $
#$Id: simpleTasks.py 87525 2016-02-02 19:47:58Z ee364b13 $

def getPairwiseDifference(vec):
    if(not (type(vec) is list)):
        return None
    if(vec == []):
        return None
    i = 0
    result = []
    while i < len(vec)-1:
        result.append(vec[i+1] - vec[i])
        i += 1
    return result

def flatten(l):
    if(not (type(l) is list)):
        return None
    for subl in l:
        if(not (type(subl) is list)):
            return None
    result = []
    for subl in l:
        for subsubl in subl:
            result.append(subsubl)
    return result

def partition(l,n):
    if(not (type(l) is list)):
        return None
    if(l == []):
        return None
    result = []
    part_re = []
    i = 0
    for num in l:
        if i < n:
            part_re.append(num)
            i += 1
        if i == n:
            i = 0
            result.append(part_re.copy())
            part_re.clear()
    if part_re != []:
        result.append(part_re.copy())
    return result

def rectifySignal(signal):
    if(not (type(signal) is list)):
        return None
    if(signal == []):
        return None
    i = 0
    while i < len(signal):
        if signal[i] < 0:
            signal[i] = 0
        i += 1
    return signal

def floatRange(a,b,s):
    if a >= b:
        return None
    result = []
    a=a+0.0
    while a <= b:
        a = round(a,1)
        result.append(a)
        a += s
    return result

def getLongestWord(sentence):
    if(not (type(sentence) is str)):
        return None
    l = sentence.split()
    print(l)
    if(len(l) <= 1):
        return None
    maxlen = 0
    maxind = 0
    ind = 0
    for i in l:
        if len(i) > maxlen:
            maxlen = len(i)
            maxind = ind
        ind += 1
    return l[maxind]

def decodeNumbers(numList):
    if(not (type(numList) is list)):
        return None
    for num in numList:
        if(not (type(num) is int)):
            return None
    ascii_list = []
    for num in numList:
        ascii_list.append(chr(num))
    return "".join(ascii_list)

def getCreditCard(s):
    if len(s) == 0:
        return None
    creditcard = []
    zero = ord('0')
    nine = ord('9')
    for i in s:
        if((ord(i)>=zero) and (ord(i)<=nine)):
            creditcard.append(ord(i)-zero)
    return creditcard


if __name__ == '__main__':
    pass