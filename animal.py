#!/usr/bin/env python
# coding: UTF-8
#
## @package animal
#  Partial implementation of the animal
#  @author Wellington Oliveira
#  @since 23/02/2018

import random
from gender import Gender
from abc import ABCMeta, abstractmethod


##
#  consists of an abstract class for bears and fish
#

class Animal(metaclass=ABCMeta):
    ##
    #   constructor
    #   @param age the age of animal
    #   @param gender the gender of animal
    def __init__(self, age=None, gender=None):
        ## if the gender is not passed, then the gender is chosen randomly
        if gender is None:
            self.gender = Gender.FEMALE if random.randint(0, 1) == 0 else Gender.MALE
        else:
            self.gender = gender
        ## The age of animal
        self.age = age

    ##  abstract method for implementation in subclasses
    #
    ##  get the age
    @abstractmethod
    def getAge(self):
        pass

    ##  the maximum age of the animal
    @abstractmethod
    def maxAge(self):
        pass

    ##  increases the age of the animal
    @abstractmethod
    def incrAge(self):
        pass
