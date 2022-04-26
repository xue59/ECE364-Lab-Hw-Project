#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-02-06 17:02:25 -0500 (Sat, 06 Feb 2016) $
#$Revision: 87771 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab04/dataStructs.py $
#$Id: dataStructs.py 87771 2016-02-06 22:02:25Z ee364b13 $

import os
import sys
import glob
import filecmp

def getWordFrequency():
    dictionary = {}
    all_files = glob.glob("files/*.txt")
    for file in all_files:
        with open(file, 'r') as f:
            for line in f:
                for word in line.split():
                    if(word[-1]=='.' or word[-1]==',' or word[-1]== '?'
                       or word[-1]== '!' or word[-1]== ':' or word[-1]== ';'):
                        word = word[:-1]
                    if not (word in dictionary):
                        dictionary[word] = 1
                    else:
                        dictionary[word] += 1
    return dictionary

def getDuplicates():
    dictionary = {}
    all_groups = []
    all_files = glob.glob("files/*.txt")

    for file in all_files:
        name = file[6:9]
        found = 0
        for group in all_groups:
            file_in_group = "files/"+group[0]+".txt"
            if(filecmp.cmp(file_in_group, file)):
                group.append(name)
                found = 1
                break
        if found == 0:
            newgroup = [name]
            all_groups.append(newgroup)

    for group in all_groups:
        group.sort()
        word_list = []
        with open("files/"+group[0]+".txt", 'r') as f:
            for line in f:
                for word in line.split():
                    if(word[-1]=='.' or word[-1]==',' or word[-1]== '?'
                       or word[-1]== '!' or word[-1]== ':' or word[-1]== ';'):
                        word = word[:-1]
                    if not (word in word_list):
                        word_list.append(word)
        dictionary[group[0]] = (len(word_list), group)

    return dictionary

def getPurchaseReport():
    inventory = {}
    itemlist = "purchases/Item List.txt"
    line_num = 0
    with open(itemlist, 'r') as f:
        for line in f:
            if line_num < 2:
                line_num += 1
                continue
            contents = line.split()
            contents[1] = round(float(contents[1][1:]),2)
            inventory[contents[0]] = contents[1]

    report = {}
    purchases = glob.glob("purchases/purchase_*.txt")
    for purchase in purchases:
        with open(purchase, 'r') as f:
            id = int(purchase[19:22])
            total = 0.00
            line_num = 0
            for line in f:
                if line_num < 2:
                    line_num += 1
                    continue
                contents = line.split()
                prize = inventory.get(contents[0])
                quantity = int(contents[1])
                total = round((total + prize * quantity), 2)
            report[id] = total
    return report

def getTotalSold():
    report = {}
    itemlist = "purchases/Item List.txt"
    line_num = 0
    with open(itemlist, 'r') as f:
        for line in f:
            if line_num < 2:
                line_num += 1
                continue
            contents = line.split()
            report[contents[0]] = 0
    purchases = glob.glob("purchases/purchase_*.txt")
    for purchase in purchases:
        with open(purchase, 'r') as f:
            line_num = 0
            for line in f:
                if line_num < 2:
                    line_num += 1
                    continue
                contents = line.split()
                quantity = int(contents[1])
                report[contents[0]] += quantity
    return report
if __name__ == "__main__":
    pass