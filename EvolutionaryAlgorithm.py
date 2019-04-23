import random


population = []

def TwoPointCrossover(parent1, parent2):
    """Function to mate two parent strings"""
    child1 = parent1
    child2 = parent2
    for i in range(min([len(parent1), len(parent2)])):
        if bool(random.getrandbits(1)):
            child1[i] = parent2[i]
            child2[i] = parent1[i]
    return (child1, child2)

def EvoAlgo(population, operators, mu, lambda_, cxpb, mutpb, ngen):
    """
    Evolutionary algorithm that returns the most fit individual
        -- Follows the input format of eaMuPlusLambda algorithm in the DEAP package --
        https://github.com/DEAP/deap/blob/master/deap/algorithms.py

    parameters:
    population - list of individuals that form the first generation
    operators - list of operators depending on the type of evolutionary algorithm
    mu - number of individuals to be taken from nth generation to the (n+1)th generation
    lambda_ - number of offsprings to be produced at each generation
    cxpb - probability of an 
    """
    assert cxpb + mutpb <= 1.0

    # TODO: Finish Implementation
    if random.random() < mutpb:
        pass

    if random.random() < cxpb:
        pass

if __name__ == "__main__":
    pass
