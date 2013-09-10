import random

WEIGHT = 2

class Employee:
    weight = 0
    name = ''
    def __init__(self, name):
        self.name = name
    def addWeight(self, num):
        self.weight += num
    def __cmp__(self, other):
        if abs(self.weight) == abs(other.weight):
            if self.weight == other.weight:
                return -1 if self.name < (other.name) else 1;
            else:
                return other.weight - self.weight
        else:
            return -1 if abs(self.weight) < abs(other.weight) else 1;
    def __repr__(self):
        return self.name #+ ": " + str(self.weight)

class EmployeeList:
    employeeList = []
    def __init__(self, nameList):
        self.employeeList = [Employee(x) for x in nameList]
    def addWeights(self):
        for i in xrange(len(self.employeeList)):
            self.employeeList[i].addWeight(getWeight(i, len(self.employeeList)))            
    def run(self):
        self.addWeights();
        s = sorted(self.employeeList)
        for emp in s:
            self.moveEmployee(emp)
    def moveEmployee(self, emp):        
        for i in range(abs(int(emp.weight))):
            if emp.weight > 0:
                self.__empUp__(emp)
            else:
                self.__empDown__(emp)
    def __empUp__(self, emp):
        empIndex = self.employeeList.index(emp)
        if(empIndex > 0):
            self.employeeList[empIndex] = self.employeeList[empIndex - 1]
            self.employeeList[empIndex - 1] = emp
            empIndex -= 1
    def __empDown__(self, emp):
        empIndex = self.employeeList.index(emp)
        if(empIndex < len(self.employeeList) - 1):
            self.employeeList[empIndex] = self.employeeList[empIndex + 1]
            self.employeeList[empIndex + 1] = emp
            empIndex += 1
    def __repr__(self):
        return "EL: " +  self.employeeList.__repr__()
                    
                    
    

def getWeight(index, length):
    return ((index * 1.0 / ((length - 1) * 1.0 / 2.0)) * WEIGHT * 1.0) - WEIGHT

#testing
e = EmployeeList( ['a', 'b', 'c', 'e', 'd', 'f', 'g'] )  ## create instance

def test(num):
    for i in xrange(num):
        e.run()
        print(e)



    
