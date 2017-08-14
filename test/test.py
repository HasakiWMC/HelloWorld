#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary, dictionary, json):
        self.name = name
        self.salary = salary
        self.dictionary = dictionary
        self.json = json
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

    def __str__(self):
        return str(self.__dict__)


if __name__ == '__main__':
    e = Employee("wmc", 6500, [12, 432.23, "243432"], {"23": 12, "aaa": "aa", "bb": 23.2})
    # e.displayCount()
    # e.displayEmployee()
    print e.__str__()
