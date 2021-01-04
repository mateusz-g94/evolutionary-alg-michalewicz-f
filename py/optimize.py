#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 01:19:48 2021

@author: thatone

"""

import sys

from classes import *

if __name__ == '__main__':
      
    # PARAMS
    if len(sys.argv) == 6:
        DIM = int(sys.argv[1]) 
        N_EPOCHS = int(sys.argv[2])
        POP_N = int(sys.argv[3])
        SH_PARENTS_NEXT = float(sys.argv[4])
        VERBOSE = int(sys.argv[5])
        
    if len(sys.argv) == 5:
        DIM = int(sys.argv[1]) 
        N_EPOCHS = int(sys.argv[2])
        POP_N = int(sys.argv[3])
        SH_PARENTS_NEXT = float(sys.argv[4])
        VERBOSE = 1
        
    if len(sys.argv) == 4:
        DIM = int(sys.argv[1]) 
        N_EPOCHS = int(sys.argv[2])
        POP_N = int(sys.argv[3])
        VERBOSE = 1
        SH_PARENTS_NEXT = 0.5
        
    ### MAIN ###
    # Population initialization
    # population_init is a list of Individual objects, sh_parents - parameter specyfying how many 
    # Individual objects will be parents (share in percentage)
    population = Population(population_init = [Individual(dim = DIM) for _ in range(POP_N)], sh_parents = SH_PARENTS_NEXT)
    
    # Main loop    
    for epoch in range(N_EPOCHS):
        population = population.get_next_generation() # this method returns new population with crossover and mutation     
        if VERBOSE > 1:
            print("EPOCH", epoch + 1, "fitness: ", population.get_best_fitness())
            
    if VERBOSE > 0:
        print("")
        print(" -- END -- ")
        print("Minimum:", round(population.get_best_fitness(), 4), 'Dim:', DIM)
        print(" --     --")