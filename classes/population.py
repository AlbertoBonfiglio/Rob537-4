#!/usr/bin/python3
from classes.individual import Individual

class Population (object):


    def __init__(self, genome, size:100):
        self.individuals = [Individual(genome) for n in range(size)]

        print(self.individuals)


    def create(self, size:100):
        for n in range(size):
            self.individuals.append(Individual())



    def evolve(self, epochs:1000):
        pass



