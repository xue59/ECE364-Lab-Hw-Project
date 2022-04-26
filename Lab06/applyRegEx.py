#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-02-23 14:46:17 -0500 (Tue, 23 Feb 2016) $
#$Revision: 88737 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Lab06/applyRegEx.py $
#$Id: applyRegEx.py 88737 2016-02-23 19:46:17Z ee364b13 $

import os
import sys
import re

def getRejectedUsers():
    filename = "SiteRegistration.txt"
    users = []
    with open(filename, 'r') as f:
        for line in f:
            rejected_natural = re.match("^([A-Za-z]+)\s([A-Za-z]+)(\W*)$",line)
            rejected_formal = re.match("^([A-Za-z]+),\s([A-Za-z]+)(\W*)$",line)
            if rejected_natural:
                name = rejected_natural.group(1) + " " + rejected_natural.group(2)
                users.append(name)
            if rejected_formal:
                name = rejected_formal.group(2) + " " + rejected_formal.group(1)
                users.append(name)
    users.sort()
    return users

def getUsersWithEmails():
    filename = "SiteRegistration.txt"
    dictionary = {}
    with open(filename, 'r') as f:
        for line in f:
            info_n = re.match("([A-Za-z]+)\s([A-Za-z]+)\W*([\w.-]+)@([\w.-]+)",line)
            info_f = re.match("([A-Za-z]+),\s([A-Za-z]+)\W*([\w.-]+)@([\w.-]+)",line)
            if info_n:
                name = info_n.group(1) + " " + info_n.group(2)
                email = info_n.group(3)+ "@" + info_n.group(4)
                dictionary[name] = email
            if info_f:
                name = info_f.group(2) + " " + info_f.group(1)
                email = info_f.group(3)+ "@" + info_f.group(4)
                dictionary[name] = email
    return dictionary

def getUsersWithPhones():
    filename = "SiteRegistration.txt"
    dictionary = {}
    with open(filename, 'r') as f:
        for line in f:
            info_n = re.match("([A-Za-z]+)\s([A-Za-z]+).*(\d\d\d).*(\d\d\d).*(\d\d\d\d)",line)
            info_f = re.match("([A-Za-z]+),\s([A-Za-z]+).*(\d\d\d).*(\d\d\d).*(\d\d\d\d)",line)
            if info_n:
                name = info_n.group(1) + " " + info_n.group(2)
                phone = "(" + info_n.group(3)+ ") " + info_n.group(4) + "-" + info_n.group(5)
                dictionary[name] = phone
            if info_f:
                name = info_f.group(2) + " " + info_f.group(1)
                phone = "(" + info_f.group(3)+ ") " + info_f.group(4) + "-" + info_f.group(5)
                dictionary[name] = phone
    return dictionary

def getUsersWithStates():
    filename = "SiteRegistration.txt"
    dictionary = {}
    with open(filename, 'r') as f:
        for line in f:
            info_n = re.match("^([A-Za-z]+)\s([A-Za-z]+).*([A-Z][a-z]+\s\w*)$",line.strip())
            info_f = re.match("^([A-Za-z]+),\s([A-Za-z]+).*([A-Z][a-z]+\s\w*)$",line.strip())

            info_n_ns = re.match("^([A-Za-z]+)\s([A-Za-z]+).*([A-Z][a-z]+)$",line.strip())
            info_f_ns = re.match("^([A-Za-z]+),\s([A-Za-z]+).*([A-Z][a-z]+)$",line.strip())

            if info_n_ns:
                name = info_n_ns.group(1) + " " + info_n_ns.group(2)
                states = info_n_ns.group(3)
                dictionary[name] = states
            if info_f_ns:
                name = info_f_ns.group(2) + " " + info_f_ns.group(1)
                states = info_f_ns.group(3)
                dictionary[name] = states

            if info_n:
                name = info_n.group(1) + " " + info_n.group(2)
                states = info_n.group(3)
                dictionary[name] = states
            if info_f:
                name = info_f.group(2) + " " + info_f.group(1)
                states = info_f.group(3)
                dictionary[name] = states
    return dictionary

def getUsersWithoutEmails():
    email = getUsersWithEmails()
    phone = getUsersWithPhones()
    states = getUsersWithStates()

    result = []

    for name in phone:
        if (name not in result) and (name not in email):
            result.append(name)
    for name in states:
        if (name not in result) and (name not in email):
            result.append(name)

    result.sort()
    return result

def getUsersWithoutPhones():
    email = getUsersWithEmails()
    phone = getUsersWithPhones()
    states = getUsersWithStates()

    result = []

    for name in email:
        if (name not in result) and (name not in phone):
            result.append(name)
    for name in states:
        if (name not in result) and (name not in phone):
            result.append(name)

    result.sort()
    return result

def getUsersWithoutStates():
    email = getUsersWithEmails()
    phone = getUsersWithPhones()
    states = getUsersWithStates()

    result = []

    for name in email:
        if (name not in result) and (name not in states):
            result.append(name)
    for name in phone:
        if (name not in result) and (name not in states):
            result.append(name)

    result.sort()
    return result


def getUsersWithCompleteInfo():
    email = getUsersWithEmails()
    phone = getUsersWithPhones()
    states = getUsersWithStates()

    result = {}

    for name in email:
        if name in phone:
            if name in states:
                result[name] = (email.get(name), phone.get(name), states.get(name))
    return result

if __name__ == "__main__":
    getUsersWithoutEmails()