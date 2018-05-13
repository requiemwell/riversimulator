#!/usr/bin/env python
# coding: UTF-8
#
## @package bear
#  the bear class extends the animal class, providing the implementation
#  of the getAge (), maxAge () and incrAge () methods
#  @author Wellington Oliveira
#  @since 23/02/2018

from animal import *


##
#   constructor
#   @param age inherited from animal
#   @param gender inherited from animal

class Bear(Animal):
    def __init__(self, age=None, gender=None):
        super().__init__(age, gender)
        ##  age receives the data returned of the method getAge()
        self.age = self.getAge()

    ##  returns the strength of the bear relative to its age
    @property
    def getStrength(self):
        force = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1, 9: 0}
        return force[self.age]

    ## returns the age randomly
    def getAge(self):
        if self.age is None:
            self.age = random.randint(0, 9)
        return self.age

    ## returns true or false if the bear has reached the maximum age of nine years
    def maxAge(self):
        if self.age == 9:
            return True
        else:
            return False

    ## @return
    # increases the age of the bear
    # return True or False
    def incrAge(self):
        if self.maxAge():
            return False
        else:
            self.age += 1
        return True

    ## return representation of object bear
    def __repr__(self):
        return "B{}{}".format(self.gender.name[0], self.age)
