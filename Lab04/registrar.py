#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-02-09 14:58:50 -0500 (Tue, 09 Feb 2016) $
#$Revision: 87951 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Lab04/registrar.py $
#$Id: registrar.py 87951 2016-02-09 19:58:50Z ee364b13 $

import os
import sys
import glob
import filecmp

def getDetails():
    details = {}
    infos = {}
    linenum = 0
    with open("files/students.txt",'r') as f:
        for line in f:
            if(linenum < 2):
                linenum += 1
                continue
            info = line.split()
            name = info[0] + " " + info[1] + " " + info[2]
            id = info[-1]
            infos[id] = name
    tupleset = {}
    all_files = glob.glob("files/EECS*.txt")
    for file in all_files:
        courseid = file[10:13]
        with open(file, 'r') as f:
            linenum = 0
            for line in f:
                if(linenum < 2):
                    linenum += 1
                    continue
                text = line.split()
                puid = text[0]
                grade = float(text[1])
                grade = round(grade)
                tuplea = {(courseid, grade)}
                key = infos.get(puid)
                tupleset = details.get(key)
                if(tupleset == None):
                    tupleset = tuplea
                else:
                    tupleset = tuplea | tupleset
                details[key] = tupleset
    return details
def getStudentList(classNumber):
    infos = {}
    linenum = 0
    with open("files/students.txt",'r') as f:
        for line in f:
            if(linenum < 2):
                linenum += 1
                continue
            info = line.split()
            name = info[0] + " " + info[1] + " " + info[2]
            id = info[-1]
            infos[id] = name
    file = "files/EECS" + str(classNumber) + ".txt"
    all_files = glob.glob("files/EECS*.txt")
    if (file not in all_files):
        return []
    list = []
    linenum = 0
    with open(file, 'r') as f:
        for line in f:
            if(linenum < 2):
                linenum += 1
                continue
            puid = line.split()[0]
            list.append(infos.get(puid))
    list.sort()
    return list
def searchForName(studentName):
    result = {}
    dict = getDetails()
    set = dict.get(studentName)
    if (set == None):
        return {}
    for x,y in set:
        result[x] = y
    return result
def searchForID(studentID):
    result = {}

    infos = {}
    linenum = 0
    with open("files/students.txt",'r') as f:
        for line in f:
            if(linenum < 2):
                linenum += 1
                continue
            info = line.split()
            name = info[0] + " " + info[1] + " " + info[2]
            id = info[-1]
            infos[id] = name

    name = infos.get(studentID)

    return searchForName(name)
def findScore(studentName, classNumber):
    all_grades = searchForName(studentName)
    return all_grades.get(classNumber)

def getHighest(classNumber):
    atuple = ()
    file = "files/EECS" + str(classNumber) + ".txt"
    all_files = glob.glob("files/EECS*.txt")
    if (file not in all_files):
        return atuple
    linenum = 0
    high = 0
    recorder = []
    with open(file, 'r') as f:
        for line in f:
            if(linenum < 2):
                linenum += 1
                continue
            text = line.split()
            grade = float(text[1])
            if(grade > high):
                high = round(grade)
                recorder = text[0]

    infos = {}
    linenum = 0
    with open("files/students.txt",'r') as f:
        for line in f:
            if(linenum < 2):
                linenum += 1
                continue
            info = line.split()
            name = info[0] + " " + info[1] + " " + info[2]
            id = info[-1]
            infos[id] = name

    atuple = (infos.get(recorder),high)
    return atuple
def getLowest(classNumber):
    atuple = ()
    file = "files/EECS" + str(classNumber) + ".txt"
    all_files = glob.glob("files/EECS*.txt")
    if (file not in all_files):
        return atuple
    linenum = 0
    low = 999
    recorder = []
    with open(file, 'r') as f:
        for line in f:
            if(linenum < 2):
                linenum += 1
                continue
            text = line.split()
            grade = float(text[1])
            if(grade < low):
                low = round(grade)
                recorder = text[0]

    infos = {}
    linenum = 0
    with open("files/students.txt",'r') as f:
        for line in f:
            if(linenum < 2):
                linenum += 1
                continue
            info = line.split()
            name = info[0] + " " + info[1] + " " + info[2]
            id = info[-1]
            infos[id] = name

    atuple = (infos.get(recorder),low)
    return atuple
def getAverageScore(studentName):
    details = getDetails()
    set = details.get(studentName)
    if (set == None):
        return None
    total = 0
    num = 0
    for x,y in set:
        total = total + y
        num = num + 1
    return (round(total/num, 1))
if __name__ == "__main__":
    pass

#marked done