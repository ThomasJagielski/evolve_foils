import random


population = []

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
    pass
    
    # TODO: Finish Implementation
    if random.random() < mutpb:
        pass

    if random.random() < cxpb:
        pass

if __name__ == "__main__":
    pass
