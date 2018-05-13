#!/usr/bin/env python
# coding: UTF-8
#
## @package riversimulator
#  simulates the river along the cycles
#  @author Wellington Oliveira
#  @since 23/02/2018

from river import *
import os
import time


##
#  @param finished controls the tie stop
#  @param trial is a counter
def startSimulation():
    finished = False
    trial = 1
    while not finished:
        sim = RiverSimulator(trial)

        if sim.option is False:
            os.system("cls")
            print("\n\n\n\n\n\n\n\n\n\n")
            print("                                     Thank you for playing River Simulator!!!")
            time.sleep(2)
            finished = True
        else:
            cycles = sim.numCycles()
            numcycle = 1
            ecosystem = sim.initializing()
            print(ecosystem)
            print()
            while numcycle <= cycles:
                print("After cycle {}:".format(numcycle))
                ecosystem.updateRiver()
                print()
                print(ecosystem)
                print()
                numcycle += 1
            print("Final river")
            print()
            print(ecosystem)
            print()
        trial += 1


##
#
#   implementation of simulator
#

class RiverSimulator:
    ##
    #   constructor
    #   @param option receive the user option
    #   @param trial is a counter
    def __init__(self, trial):
        print("River Ecosystem Simulator")
        print("Keys: 1(random river) 2 (file input) 3 (exit)")
        ## trial the counter
        self.trial = trial
        ## the option of user
        self.option = self.ProcessChoice()

    ##
    #   @return a river object
    #   initializes the river with the selected option
    #
    def initializing(self):
        print("Initial river:")
        print()
        return River(self.option)

    ##
    #  @return the user option
    #  validate input
    def choiceUser(self):
        print()
        opt = input("Trial {}: ".format(self.trial))
        while opt not in ("1", "2", "3"):
            print("option Invalid")
            opt = input("Trial {}:".format(self.trial))

        return opt

    ##
    #   @return the size of the river
    #   validade the length of river
    @property
    def choiceLength(self):
        op = input("Enter river length: ")
        while True:
            if not op.isnumeric() or int(op) < 1:
                print("invalid length!")
                op = input("Enter river length: ")
            else:
                break
        return int(op)

    ##
    #   processes the user option
    #   @return op
    #
    def ProcessChoice(self):
        op = self.choiceUser()
        if op == "1":
            print("Random River: ")
            op = self.choiceLength
        elif op == "2":
            print("Archive river:")
            op = input("Input archive name: ")
        else:
            op = False

        return op

    ##
    #  asks the user or number of cycles
    #  @return num
    def numCycles(self):
        while True:
            num = input("Enter the number of the cycles: ")
            if num.isnumeric() and int(num) >= 1:
                break
            else:
                num = input("Enter the number of the cycles: ")
        return int(num)


if __name__ == "__main__":
    startSimulation()
