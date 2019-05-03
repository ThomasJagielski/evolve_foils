import random
from collections import OrderedDict

import classes


population = []

def create_pop(num_indiv):
    """
    Function to create a population

    num_indiv - the number of individuals you would like to create in the population
    """  
    # Initialize the dictionary to store the indiviuals of a population
    population = dict()
    # Use for loop to create individuals
    for _ in range(num_indiv):
        individual = classes.Individual()
        # Append the coefficients as a tuple as the key 
        # and the coefficient of lift to drag as the value
        population[tuple(individual)] = classes.evaluate_foil(individual)
    return population

def TwoPointCrossover(parent1, parent2):
    """
    Function to mate two parent strings and generate children

    parent1 - list of coefficients for the first foil
    parent2 - list of coefficients for the second foil
    """
    # Define the childs equal to the parents in order to maintain values while mating
    child1 = parent1
    child2 = parent2
    for i in range(min([len(parent1), len(parent2)])):
        # For each letter in the parent lists, generate a 1 or 0
        # 1 will yield a crossover in the coefficients
        # 0 will keep the child values the same as the parents
        if bool(random.getrandbits(1)):
            child1[i] = parent2[i]
            child2[i] = parent1[i]
    return (child1, child2)

def selection(population,num_indiv):
    """
    Selection is a function that will 

    population - dictionary with the keys as a list of coefficients and values of the fitness (coefficient of lift to drag)
    num_indiv - the number of top individuals you would like to return 
    """
    # Sort the population based on their coefficient of lift to drag (value) from the population dictionary
    sorted_population = sorted(population.items(), key=lambda v:v[1],reverse=True)
    return sorted_population[0:num_indiv]

def EvolutionaryAlgorithm(num_generations,num_indiv,top_indiv, num_cross,new_indiv_num,prob_add,prob_subtract):
    """
    Evolutionary algorithm that will iteratively improve the population of foils based on their coefficient of lift to drag

    num_generations - the number of generations you would like your airfoil to run
    num_indiv - the number of top performers you would like to select from the "selected" function
    top_indiv - select the top individuals
    num_cross - select the number of individuals in the new population you would like to come from mating
    new_indiv_num - the number of new individuals added to the next generation 
    prob_add - the pobability of mutation by adding 
    prob_subtract - the probability of mutation by subtracting
    """
    # Create a population
    population = create_pop(num_indiv)
    for i in range(0,num_generations):
        # Select the top number of individuals from a popultion
        selected = dict(selection(population,top_indiv))
        # Initialize a list of the top performing coefficients
        most_fit_coeff = []
        # for the key 
        for key in selected:
            # Append the top performing foils from a generation and append it to "most_fit_coeff"
            most_fit_coeff.append(list(key))
        # Begin the new population with the top performing individuals
        population = selected
        # Add to the new population by generating foils with mating
        for _ in range(0,num_cross):
            # Ensure the top airfoil remains the same from generation to generation
            individual = TwoPointCrossover(most_fit_coeff[random.randint(1,top_indiv-1)],
                                    most_fit_coeff[random.randint(1,top_indiv-1)]) 
            # Evaluate the new foils          
            for k in range(0,1):
                population[tuple(individual[k])] = classes.evaluate_foil(individual[k])
        # Implement mutation for the foils
        for key in population:
            del population[key]
            # Mutate the coefficients of the foil
            new_coeff = classes.mutate(list(key),prob_add,prob_subtract)
            # Evaluate the new foils
            population[tuple(new_coeff[0])] = classes.evaluate_foil(new_coeff[0])
        # Create new individuals for the population
        new_indiv = create_pop(new_indiv_num)
        # Append the new individuals to population
        population.update(new_indiv)

        # For the last generation, re-run the test for the top performing foil in order to save its data
        if i == num_generations - 1:
            # Run and save the best airfoil as the last one
            selected = dict(selection(population,1))
            for key in selected:
                # Evaluate the foil
                classes.evaluate_foil(key)
                print(key,classes.evaluate_foil(key))
        # Print the generation
        print(i)

if __name__ == "__main__":
    EvolutionaryAlgorithm(10,10,2,2,8,0.2,0.8)