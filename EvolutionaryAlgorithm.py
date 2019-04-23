import random
import classes
from collections import OrderedDict


population = []

def create_pop(num_indiv):
    """
    Function to create a population
    """  
    population = dict()
    for i in range(num_indiv):
        individual = classes.Individual()

        population[tuple(individual)] = classes.evaluate_foil(individual)


    
    return population

def TwoPointCrossover(parent1, parent2):
    """Function to mate two parent strings"""
    child1 = parent1
    child2 = parent2
    for i in range(min([len(parent1), len(parent2)])):
        if bool(random.getrandbits(1)):
            child1[i] = parent2[i]
            child2[i] = parent1[i]
    return (child1, child2)

def selection(population,num_indiv):
    """
    population - dictionary with the keys as a list of coefficients and values of the fitness (coefficient of lift to drag)
    """
    sorted_population = sorted(population.items(), key=lambda v:v[1],reverse=True)
    return sorted_population[0:num_indiv]

def EvoAlgo(num_population, operators, mu, lambda_, cxpb, mutpb, ngen):
    """
    Evolutionary algorithm that returns the most fit individual
        -- Follows the input format of eaMuPlusLambda algorithm in the DEAP package --
        https://github.com/DEAP/deap/blob/master/deap/algorithms.py

    parameters:
    population - list of individuals that form the first generation
    operators - list of operators depending on the type of evolutionary algorithm
    mu - number of individuals to be taken from nth generation to the (n+1)th generation
    lambda_ - number of offs
    """

    assert cxpb + mutpb <= 1.0

    # TODO: Finish Implementation

    if random.Random()< mutpb:
        pass
    if random.Random()< cxpb:
        pass

if __name__ == "__main__":
    selected = dict(selection(create_pop(10),2))