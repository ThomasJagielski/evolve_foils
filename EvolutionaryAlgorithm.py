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

def EvoAlgo(num_generations,num_indiv,top_indiv, num_cross,new_indiv_num,prob_add,prob_subtract):
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
    for i in range(0,num_generations):
        selected = dict(selection(population,top_indiv))
        most_fit_coeff = []
        for key in selected:
            most_fit_coeff.append(list(key))
        population = selected
        for _ in range(0,num_cross):
            # Ensure the top airfoil remains the same from generation to generation
            individual = TwoPointCrossover(most_fit_coeff[random.randint(1,top_indiv-1)],
                                    most_fit_coeff[random.randint(1,top_indiv-1)])           
            for k in range(0,1):
                population[tuple(individual[k])] = classes.evaluate_foil(individual[k])
        for key in population:
            del population[key]
            new_coeff = classes.mutate(list(key),prob_add,prob_subtract)
            population[tuple(new_coeff[0])] = classes.evaluate_foil(new_coeff[0])
        new_indiv = create_pop(new_indiv_num)
        population.update(new_indiv)

        # Run and save the best airfoil as the last one
        selected = dict(selection(population,1))
        # TODO Change to find better way to run key through evaluate_foil
        for key in selected:
            classes.evaluate_foil(key)
            print(key,classes.evaluate_foil(key))


        print(i)

    

    


if __name__ == "__main__":
    EvoAlgo(10,10,2,2,8,0.2,0.8)