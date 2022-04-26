__author__ = 'ee364d08'
from pprint import pprint as pp
import re,os,sys,math
def getInvalidUsers():
    f = open('UserData.txt', 'r')
    lines = f.readlines()
    name=[]
    state=''
    invalidl=[]
    for line in lines:
        num=re.search(r'\d\d\d..\d{1,}.\d{1,}', line)
        email=re.search(r'[a-zA-Z0-9._-]{1,}@purdue.com', line)
        x=re.findall(r'[A-Z][a-z]{1,}..?[a-zA-Z]{1,}',line)
        name=x[0]
        commaflag = re.search(r'[,]', name)
        if commaflag is not None:
            a = re.findall(r'\w+', name)
            name = a[1] + ' ' + a[0]
        if len(x) is 2:
            state=x[1]
        if num is None and email is None and state is '':
            invalidl.append(name)
        state =''
    invalidl.sort()
    return invalidl
def getValidUsers():
    f = open('UserData.txt', 'r')
    lines = f.readlines()
    name=[]
    state=''
    validl=[]
    for line in lines:
        num=re.search(r'\d\d\d..\d{1,}.\d{1,}', line)
        if num is not None:
            a = re.findall(r'\d\d\d', num.group())
            b = re.findall(r'(?<=......)\d\d\d\d', num.group())
            num = '(' + a[0] +') ' + a[1] + '-' + b[-1]
        email=re.search(r'[a-zA-Z0-9._-]{1,}@purdue.com', line)
        x=re.findall(r'[A-Z][a-z]{1,}..?[a-zA-Z]{1,}',line)
        name=x[0]
        commaflag = re.search(r'[,]', name)
        if commaflag is not None:
            a = re.findall(r'\w+', name)
            name = a[1] + ' ' + a[0]
        if len(x) is 2:
            state=x[1]
        if num is not None and email is not None and state is not '':
            validl.append((name, email.group(), num, state))
        state =''
    validl.sort()
    return validl
def getUsersWithEmails():
    f = open('UserData.txt', 'r')
    lines = f.readlines()
    name=[]
    state=''
    validl=[]
    for line in lines:
        num=re.search(r'\d\d\d..\d{1,}.\d{1,}', line)
        if num is not None:
            a = re.findall(r'\d\d\d', num.group())
            b = re.findall(r'(?<=......)\d\d\d\d', num.group())
            num = '(' + a[0] +') ' + a[1] + '-' + b[-1]
        email=re.search(r'[a-zA-Z0-9._-]{1,}@purdue.com', line)
        x=re.findall(r'[A-Z][a-z]{1,}..?[a-zA-Z]{1,}',line)
        name=x[0]
        commaflag = re.search(r'[,]', name)
        if commaflag is not None:
            a = re.findall(r'\w+', name)
            name = a[1] + ' ' + a[0]
        if len(x) is 2:
            state=x[1]
        if num is None and email is not None and state is '':
            validl.append((name, email.group()))
        state =''
    validl.sort()
    return validl
def getUsersWithPhones():
    f = open('UserData.txt', 'r')
    lines = f.readlines()
    name=[]
    state=''
    validl=[]
    for line in lines:
        num=re.search(r'\d\d\d..\d{1,}.\d{1,}', line)
        if num is not None:
            a = re.findall(r'\d\d\d', num.group())
            b = re.findall(r'(?<=......)\d\d\d\d', num.group())
            num = '(' + a[0] +') ' + a[1] + '-' + b[-1]
        email=re.search(r'[a-zA-Z0-9._-]{1,}@purdue.com', line)
        x=re.findall(r'[A-Z][a-z]{1,}..?[a-zA-Z]{1,}',line)
        name=x[0]
        commaflag = re.search(r'[,]', name)
        if commaflag is not None:
            a = re.findall(r'\w+', name)
            name = a[1] + ' ' + a[0]
        if len(x) is 2:
            state=x[1]
        if num is not None and email is None and state is '':
            validl.append((name, num))
        state =''
    validl.sort()
    return validl
def getUsersWithStates():
    f = open('UserData.txt', 'r')
    lines = f.readlines()
    name=[]
    state=''
    validl=[]
    for line in lines:
        num=re.search(r'\d\d\d..\d{1,}.\d{1,}', line)
        if num is not None:
            a = re.findall(r'\d\d\d', num.group())
            b = re.findall(r'(?<=......)\d\d\d\d', num.group())
            num = '(' + a[0] +') ' + a[1] + '-' + b[-1]
        email=re.search(r'[a-zA-Z0-9._-]{1,}@purdue.com', line)
        x=re.findall(r'[A-Z][a-z]{1,}..?[a-zA-Z]{1,}',line)
        name=x[0]
        commaflag = re.search(r'[,]', name)
        if commaflag is not None:
            a = re.findall(r'\w+', name)
            name = a[1] + ' ' + a[0]
        if len(x) is 2:
            state=x[1]
        if num is None and email is None and state is not '':
            validl.append((name, state))
        state =''
    validl.sort()
    return validl
def getUsersWithEmailsAndPhones():
    f = open('UserData.txt', 'r')
    lines = f.readlines()
    name=[]
    state=''
    validl=[]
    for line in lines:
        num=re.search(r'\d\d\d..\d{1,}.\d{1,}', line)
        if num is not None:
            a = re.findall(r'\d\d\d', num.group())
            b = re.findall(r'(?<=......)\d\d\d\d', num.group())
            num = '(' + a[0] +') ' + a[1] + '-' + b[-1]
        email=re.search(r'[a-zA-Z0-9._-]{1,}@purdue.com', line)
        x=re.findall(r'[A-Z][a-z]{1,}..?[a-zA-Z]{1,}',line)
        name=x[0]
        commaflag = re.search(r'[,]', name)
        if commaflag is not None:
            a = re.findall(r'\w+', name)
            name = a[1] + ' ' + a[0]
        if len(x) is 2:
            state=x[1]
        if num is not None and email is not None and state is  '':
            validl.append((name,  email.group(), num))
        state =''
    validl.sort()
    return validl

def getUsersWithEmailsAndStates():
    f = open('UserData.txt', 'r')
    lines = f.readlines()
    name=[]
    state=''
    validl=[]
    for line in lines:
        num=re.search(r'\d\d\d..\d{1,}.\d{1,}', line)
        if num is not None:
            a = re.findall(r'\d\d\d', num.group())
            b = re.findall(r'(?<=......)\d\d\d\d', num.group())
            num = '(' + a[0] +') ' + a[1] + '-' + b[-1]
        email=re.search(r'[a-zA-Z0-9._-]{1,}@purdue.com', line)
        x=re.findall(r'[A-Z][a-z]{1,}..?[a-zA-Z]{1,}',line)
        name=x[0]
        commaflag = re.search(r'[,]', name)
        if commaflag is not None:
            a = re.findall(r'\w+', name)
            name = a[1] + ' ' + a[0]
        if len(x) is 2:
            state=x[1]
        if num is None and email is not None and state is not '':
            validl.append((name, email.group(), state))
        state =''
    validl.sort()
    return validl

def getUsersWithPhonesAndStates():
    f = open('UserData.txt', 'r')
    lines = f.readlines()
    name=[]
    state=''
    validl=[]
    for line in lines:
        num=re.search(r'\d\d\d..\d{1,}.\d{1,}', line)
        if num is not None:
            a = re.findall(r'\d\d\d', num.group())
            b = re.findall(r'(?<=......)\d\d\d\d', num.group())
            num = '(' + a[0] +') ' + a[1] + '-' + b[-1]
        email=re.search(r'[a-zA-Z0-9._-]{1,}@purdue.com', line)
        x=re.findall(r'[A-Z][a-z]{1,}..?[a-zA-Z]{1,}',line)
        name=x[0]
        commaflag = re.search(r'[,]', name)
        if commaflag is not None:
            a = re.findall(r'\w+', name)
            name = a[1] + ' ' + a[0]
        if len(x) is 2:
            state=x[1]
        if num is not None and email is None and state is not '':
            validl.append((name, num, state))
        state =''
    validl.sort()
    return validl

