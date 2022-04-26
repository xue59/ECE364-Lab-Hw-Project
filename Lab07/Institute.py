#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-03-01 14:49:00 -0500 (Tue, 01 Mar 2016) $
#$Revision: 89171 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Lab07/Institute.py $
#$Id: Institute.py 89171 2016-03-01 19:49:00Z ee364b13 $

import os
import sys
import re

# This line indicates I finished
class Simulation:
    def __init__(self, simnNo, simDate, chipName, chipCount, chipCost):
        self.simulationNumber = simnNo
        self.simulationDate = simDate
        self.chipName = chipName
        self.chipCount = chipCount
        self.chipCost = chipCost
        self.simulationCost = round(chipCount * chipCost, 2)

    def __str__(self):
        number = "{0:03d}".format(self.simulationNumber)
        cost = "{0:06.2f}".format(self.simulationCost)
        return self.chipName+": "+ number + ", "+ self.simulationDate + ", $"+ cost

class Employee:
    def __init__(self, employeeName, employeeID):
        self.employeeName = employeeName
        self.employeeID = employeeID
        self.simulationsDict = {}

    def addSimulation(self, sim):
        if self.simulationsDict.get(sim.simulationNumber):
            self.simulationsDict[sim.simulationNumber] = sim
        else:
            self.simulationsDict.update({sim.simulationNumber:sim})

    def getSimulation(self, simNo):
        if simNo not in self.simulationsDict:
            return None
        return self.simulationsDict.get(simNo)

    def __str__(self):
        return self.employeeID+", "+self.employeeName+": "+ "{0:02d}".format(len(self.simulationsDict)) + " Simulations"

    def getWorkload(self):
        result = str(self)
        vector_x = []
        for x in self.simulationsDict:
            vector_x.append(str(self.simulationsDict.get(x)))
        vector_x.sort()
        for y in vector_x:
            result += "\n" + y
        return result

    def addWorkload(self, filename):
        with open(filename, "r") as f:
            ind = 0
            for line in f:
                if ind < 2:
                    ind+= 1
                    continue
                list = line.split()
                simnNo = int(list[0])
                date = list[1]
                chipName = list[2]
                chipCount = int(list[3])
                chipCost = float(list[4][1:])
                obj = Simulation(simnNo, date, chipName, chipCount, chipCost)
                self.simulationsDict.update({simnNo:obj})

class Facility:
    def __init__(self, facilityName):
        self.facilityName = facilityName
        self.employeesDict = {}

    def addEmployee(self, employee):
         if self.employeesDict.get(employee.employeeName):
            self.employeesDict[employee.employeeName] = employee
         else:
            self.employeesDict.update({employee.employeeName:employee})

    def getEmployees(self, *args):
        return list(self.employeesDict.get(name) for name in args)

    def __str__(self):
        number = len(self.employeesDict)
        string = self.facilityName + ": {0:02} Employees".format(number)
        vector_x = []
        for x in self.employeesDict:
            vector_x.append(str(self.employeesDict.get(x)))
        vector_x.sort()

        for x in vector_x:
            string += "\n" + x
        return string

    def getSimulation(self, simNo):
        for key in self.employeesDict:
            for x in self.employeesDict.get(key).simulationsDict:
                if x == simNo:
                    return self.employeesDict.get(key).simulationsDict.get(x)
        return None


if __name__ == "__main__":
    pass
