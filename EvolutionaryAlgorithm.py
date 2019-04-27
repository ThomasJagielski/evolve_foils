import random
import classes
from collections import OrderedDict


population = []

def create_pop(num_indiv):
    """
    Function to create a population
    """  
    population = dict()
    for _ in range(num_indiv):
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

def EvoAlgo(num_population,num_indiv,top_indiv, num_cross,new_indiv_num,prob_mutate):
    #operators, mu, lambda_, cxpb, mutpb, ngen):
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
    population = create_pop(num_indiv)
    for i in range(0,num_population):
        selected = dict(selection(population,top_indiv))
        most_fit_coeff = []
        for key in selected:
            most_fit_coeff.append(list(key))
        population = selected
        for _ in range(0,num_cross):
            individual = TwoPointCrossover(most_fit_coeff[random.randint(0,top_indiv-1)],
                                    most_fit_coeff[random.randint(0,top_indiv-1)])
            for k in range(0,1):
                population[tuple(individual[k])] = classes.evaluate_foil(individual[k])
        
        new_indiv = create_pop(new_indiv_num)
        population.update(new_indiv)
        #classes.mutate
        print(i)
        print(population)
    

    


if __name__ == "__main__":
    #selected = dict(selection(create_pop(10),2))
    #print(type(selected))
    EvoAlgo(10,10,2,2,8,0.2)