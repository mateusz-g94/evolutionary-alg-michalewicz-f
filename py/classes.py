#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 20:24:01 2021

@author: thatone
"""

import math
import random
import michalewicz_function as func

class Individual:

    def __init__(self, genotype = None, dim = 2, mut_proba = 0.25):
        """

        Parameters
        ----------
        genotype : list, optional
            You can define genotype publicly. If None then genotype will be random The default is None.
        dim : int, optional
            Parameter defines dimension of michalewicz function (lenght of X vector). The default is 2.
        mut_proba : float, optional
            Probability of single gen mutation. The default is 0.25.

        Raises
        ------
        ValueError
            If you specify genotype directly then dimension (dim) have to be the same as dimension of genotype.

        Returns
        -------
        None.

        """
        self.opt_range = (0, math.pi) 
        self.dim = dim
        self.mut_proba = mut_proba
        if not genotype:
            self.genotype = [random.uniform(0.0, math.pi) for _ in range(dim)]
        else:
            if len(genotype) != dim:
                raise ValueError("ERROR: dim parameter is not coressponding to genotype dim.")
            self.genotype = genotype
            
    def get_genotype(self):
        """
        GETTER
        Returns
        -------
        list[float]
            Returns object genotype.
        """
        return self.genotype
    
    def fitness(self):
        """

        Returns
        -------
        float
            Returns the finess value of michalewicz function at point genotype.

        """
        return func.michalewicz_function(self.genotype)
    
    def mutate(self, inplace = True):
        """
        

        Parameters
        ----------
        inplace : bool, optional
            If inplace then modify genotype in object definition else returns new object. The default is True.

        Returns
        -------
        Individual


        """
        new_genotype = []
        for gen in self.genotype:    
            if random.uniform(0,1) < self.mut_proba:
                gen = random.uniform(0.0, math.pi)
            new_genotype.append(gen)
        if inplace:
            self.genotype = new_genotype
            return self
        else:
            return Individual(genotype = new_genotype, dim = self.dim, mut_proba = self.mut_proba)
        
    def crossover(self, ind2):
        """

        Parameters
        ----------
        ind2 : Individual
            The second Individual with which crossover is made.

        Raises
        ------
        ValueError
            Dimensions of both objects have to be the same.

        Returns
        -------
        Individual
            
        """
        if self.dim != ind2.dim:
            raise ValueError("ERROR: Diffrent dims.")
        middle = int(self.dim / 2)
        gen1 = self.genotype[0:middle]
        gen2 = ind2.get_genotype()[middle:]
        gen_new = [*gen1, *gen2]
        return Individual(genotype = gen_new, dim = self.dim, mut_proba = self.mut_proba)
    
class Population:
    
    def __init__(self, population_init, sh_parents = 0.5):
        """

        Parameters
        ----------
        population_init : list[Indiviidual]
        sh_parents : float [0:1], optional
            Parameter defines which part of population should be parents. The default is 0.5.

        Returns
        -------
        None.

        """
        self.population_init = population_init
        self.sh_parents = sh_parents
        self.num_parents = int(len(self.population_init) * self.sh_parents)
        self.num_mates = int(len(self.population_init) - self.num_parents)
        
    def get_best_fitness(self):
        """

        Returns
        -------
        float
            Return finess value of the best object in population.

        """
        self.best = sorted(self.population_init, key = lambda x: x.fitness())[0].fitness()
        return self.best
        
    def get_next_generation(self):
        """
        
        Returns
        -------
        Population
            Function generates the new population in next epoch. Uses mutation and crossover.

        """
        population = sorted(self.population_init, key = lambda x: x.fitness())
        parents = population[0:self.num_parents]
        new_generation = []
        new_generation.extend(parents)
        for _ in range(self.num_mates):
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child = parent1.crossover(parent2)
            child.mutate()
            new_generation.append(child)
        return Population(population_init = new_generation, sh_parents = self.sh_parents)
    

    