#!/usr/bin/env python
# coding: UTF-8
#
## @package fish
#  the fish class extends the animal class, providing the implementation
#  of the getAge (), maxAge () and incrAge () methods
#  @author Wellington Oliveira
#  @since 23/02/2018

from animal import *


##
#   constructor
#   @param age inherited from animal
#   @param gender inherited from animal
#
class Fish(Animal):
    def __init__(self, age=None, gender=None):
        super().__init__(age, gender)
        ##  age receives the data returned of the method getAge()
        self.age = self.getAge()

    ##
    # returns the age of animal randomly
    def getAge(self):
        if self.age is None:
            self.age = random.randint(0, 4)
        return self.age

    ##
    # returns true or false if the fish has reached the maximum age of four years
    def maxAge(self):
        if self.age == 4:
            return True
        else:
            return False

    ##
    # increases the age of the fish
    # return True or False
    def incrAge(self):
        if self.maxAge():
            return False
        else:
            self.age += 1
        return True

    ##  representation of object fish
    def __repr__(self):
        return "F{}{}".format(self.gender.name[0], self.age)
