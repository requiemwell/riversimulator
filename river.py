#!/usr/bin/env python
# coding: UTF-8
#
## @package river
#  ecosystem where fish and bears live
#  @author Wellington Oliveira
#  @since 23/02/2018

from fish import *

from bear import *


##
#
#  constructor
#  @param seed used to replicate results
#  @param args determines whether the
#  river will be generated through an archive
#  or randomly generated
class River(object):
    def __init__(self, args, seed=None):
        ## the river to be populated
        self.river = []
        self.seed = seed
        # random.seed(self.seed)
        if isinstance(args, str):
            self.__readArchive(args)
        else:
            self.createRiver(args)

    ##
    #   creates the river randomly
    #   @param args received by the constructor is a length of the river
    def createRiver(self, args):
        self.river = [None] * args
        random.seed(self.seed)
        for i in range(args):
            option = random.choice([Bear(), Fish(), "---"])
            self.river[i] = option
            if isinstance(self.river[i], Bear):
                self.river[i].age = random.randint(0, 9)
            elif isinstance(self.river[i], Fish):
                self.river[i].age = random.randint(0, 4)

    ##
    # @param args is the name of archive
    # is the name of the file used to generate the river
    def __readArchive(self, args):
        try:
            with open(args)as arq:
                line = arq.readline().split()
                for i in line:
                    if i[0] == "B":
                        if i[1] == "M":
                            self.river.append(Bear(int(i[2]), Gender.MALE))
                        else:
                            self.river.append(Bear(int(i[2]), Gender.FEMALE))
                    elif i[0] == "F":
                        if i[1] == "M":
                            self.river.append(Fish(int(i[2]), Gender.MALE))
                        else:
                            self.river.append(Fish(int(i[2]), Gender.FEMALE))
                    else:
                        self.river.append(i)
        except Exception as e:
            print(e)

    ## @return the length of the river
    @property
    def getLength(self):
        return len(self.river)

    def setSeed(self, seed):
        self.seed = seed

    ##
    #  returns the number of empty cells in the river
    @property
    def numEmpty(self):
        return self.river.count("---")

    ##
    #
    #  if there are empty cells an animal is randomly added
    #  @param a is the type of animal to be added
    def addRandom(self, a):
        random.seed(self.seed)
        if self.numEmpty > 0:
            animal = a(0)
            while True:
                pos = random.randint(0, self.getLength - 1)
                if self.river[pos] == "---":
                    self.river[pos] = animal
                    break
            return True
        else:
            return False

    ##
    # @param animal is a object of type fish or bear
    # @param pos is the current position of the animal on the river
    # @param mov direction of displacement of the animal
    #
    def choiceMov(self, animal, pos, mov):
        ##
        #  is the object adjacent to the animal
        random.seed(self.seed)
        other_animal = self.river[pos + mov]
        if other_animal == "---":
            self.river[pos + mov] = animal
            self.river[pos] = "---"

        elif isinstance(animal, Fish) and isinstance(other_animal, Fish):
            if animal.gender != other_animal.gender:
                self.addRandom(type(animal))
            else:
                return
        elif isinstance(animal, Fish) and isinstance(other_animal, Bear):
            self.river[pos] = "---"
        elif isinstance(animal, Bear) and isinstance(other_animal, Fish):
            self.river[pos + mov] = animal
            self.river[pos] = "---"
        else:
            if isinstance(animal, Bear) and isinstance(other_animal, Bear):
                if animal.gender != other_animal.gender:
                    self.addRandom(type(animal))
                else:
                    if animal.getStrength > other_animal.getStrength:
                        self.river[pos + mov] = animal
                        self.river[pos] = "---"
                    else:
                        self.river[pos] = other_animal
                        self.river[pos + mov] = "---"

        return

    ##
    #
    #  @param i is the cell of the object to be processed
    #  processes the cell object in the cell according to some rules

    def updateCell(self, i):
        random.seed(self.seed)
        mov = random.randint(-1, 1)
        pos = i if i < self.getLength - 1 else -1
        if mov == 0:
            return
        else:
            self.choiceMov(self.river[pos], pos, mov)
            return

    ##
    #   runs a cycle in the simulation going through the
    #   river cells, updating ages, creating and killing animals
    def updateRiver(self):
        """animalcheck is a list with the animals that went through the update"""
        animalcheck = []
        for animal in self.river:
            if not isinstance(animal, str):
                if animal.maxAge():
                    pos = self.river.index(animal)
                    self.river[pos] = '---'
                else:
                    animal.incrAge()
        for i in range(self.getLength):
            if self.getLength < 2:
                return
            elif not isinstance(self.river[i], str) and self.river[i] not in animalcheck:
                animalcheck.append(self.river[i])
                self.updateCell(i)

    ##
    #   write the river to an output file.
    #   may raise IOError
    def write(self):
        try:
            with open("output.txt", "w") as out:
                for i in range(self.getLength):
                    out.write(str(self.river[i]) + " ")
        except Exception as e:
            print(e)

    ##
    #  returns object representation
    def __repr__(self):
        return " ".join(str(element) for element in self.river)
