#! /usr/bin/env python3.4
#
#$Author $
#$Date: 2016-02-16 15:12:36 -0500 (Tue, 16 Feb 2016) $
#$Revision: 88227 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Lab05/practical1.py $
#$Id: practical1.py 88227 2016-02-16 20:12:36Z ee364b13 $

import os
import sys
import glob
import filecmp

def rowSumIsValid(mat):
    i = 0
    row_sum = [0] * len(mat)
    for row in mat:
        row_sum[i] = sum(row)
        i += 1
    sum1 = row_sum[0]
    for j in row_sum:
        if not j == sum1:
            return False
    return True

def columnSumIsValid(mat):
    col_sum = [0] * len(mat)
    for row in mat:
        ind = 0
        for i in row:
            col_sum[ind] += i
            ind += 1
    sum1 = col_sum[0]
    for j in col_sum:
        if not j == sum1:
            return False
    return True
def magicSquareIsValid(filePath):
    mat = []
    with open(filePath, 'r') as f:
        ind = 0
        for line in f:
            line_list = line.split()
            i = 0
            for char in line_list:
                line_list[i] = int(char)
                i += 1
            mat.append(line_list)
            ind += 1
    return rowSumIsValid(mat) and columnSumIsValid(mat)

def getTotalCost(itemSet):
    files = glob.glob("Stores/*")
    result_dict = {}
    for file in files:
        store = file[7:-4]
        if result_dict.get(store) == None:
            result_dict[store] = 0
        with open(file, 'r') as f:
            num = 0
            for line in f:
                if num < 3:
                    num += 1
                    continue
                line_list = line.split()
                itemname = line_list[0] + " " + line_list[1]
                price = line_list[-1][1:]
                itemprice = float(price)
                for name, quantity in itemSet:

                    if itemname == name:
                        result_dict[store] += quantity * itemprice
                        result_dict[store] = round(result_dict.get(store),2)
    return result_dict
def getBestPrices(cpuSet):
    result_dict = {}

    files = glob.glob("Stores/*")
    for file in files:
        store = file[7:-4]
        with open(file, 'r') as f:
            num = 0
            for line in f:
                if num < 3:
                    num += 1
                    continue
                line_list = line.split()
                itemname = line_list[0] + " " + line_list[1]
                price = line_list[-1][1:]
                itemprice = float(price)

                for cpu in cpuSet:
                    if cpu == itemname:
                        if result_dict.get(cpu) == None:
                            result_dict[cpu] = (itemprice,store)
                        else:
                            p,s  = result_dict.get(cpu)
                            if itemprice < p:
                                result_dict[cpu] = (itemprice,store)

    return result_dict
def getMissingItems():
    result_dict = {}
    buffer_arr = []
    stores = []
    files = glob.glob("Stores/*")
    for file in files:
        store = file[7:-4]
        stores.append(store)
        result_dict[store] = set()
        with open(file, 'r') as f:
            num = 0
            for line in f:
                if num < 3:
                    num += 1
                    continue
                line_list = line.split()
                itemname = line_list[0] + " " + line_list[1]
                buffer_arr.append((store, itemname))
    for key in stores:
        thislist = []
        for store, item in buffer_arr:
            if key == store:
                thislist.append(item)
        for store, item in buffer_arr:
            if key != store:
                if item not in thislist:
                    result_dict[key] = result_dict.get(key) | {item}
    return result_dict
if __name__ == "__main__":
    pass