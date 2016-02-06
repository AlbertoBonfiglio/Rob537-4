#!/usr/bin/python3


class Individual (object):

    def __init__(self, genome, threshold=0.1):
        self.threshold = threshold
        self.genome = genome    #this is the actual data we are evolving weights for
        self.alleles = [0 for n in range(len(genome))] #these are the actual weights we are evolving



    def fitness(self, func=time_to_ground):
        return func()


    #in this instance we calculate fitness based on how long
    #the pendulum stays up
    #returns milliseconds
    def time_to_ground(self):
        #TODO perform calulatoin
        return 0

    #in this instance we calculate fitness based on how long
    #the pendulum stays within plus or minus the threshold
    #returns milliseconds
    def time_to_threshold(self):
        #TODO perform calulatoin
        return 0