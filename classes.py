import random
import string
import sys

import numpy as np   # Used for statistics
from deap import algorithms
from deap import base
from deap import tools

import evaluateFoil

X_COORD = np.linspace(1,0,50).tolist()
X_COORD.extend(np.linspace(0,1,50).tolist()[1:])
for i in range(len(X_COORD)):
    X_COORD[i] = round(X_COORD[i],6)
print(X_COORD)

class FitnessMinimizeSingle(base.Fitness):
    """
    Class representing the fitness of a given individual, with a single
    objective that we want to maximize (weight = 1)
    """
    weights = (1.0,)


class Individual(list):
    """An individual Message within the population to be evolved.

    We represent the foil as a list of points (x,y) so it can
    be more easily manipulated by the genetic operators.
    """

    def __init__(self):
        """Create a new Message individual.

        If starting_string is given, initialize the Message with the
        provided string message. Otherwise, initialize to a random string
        message with length between min_length and max_length.
        """
        # Want to minimize a single objective: distance from the goal message
        self.fitness = FitnessMinimizeSingle()

        # Otherwise, select an initial length between min and max
        # and populate Message with that many random characters
        for i in range(50):
            self.append(random.random()/2+.01)  # Assume that height shiould not be more than 2 times length


    # TODO Add print method later if we want it
    # def __repr__(self):
    #     """Return a string representation of the Message."""
    #     # Note: __repr__ (if it exists) is called by __str__. It should provide
    #     #       the most unambiguous representation of the object possible, and
    #     #       ideally eval(repr(obj)) == obj
    #     # See also: http://stackoverflow.com/questions/1436703
    #     template = '{cls}({val!r})'
    #     return template.format(cls=self.__class__.__name__,     # "Message"
    #                            val=self.get_text())
    








def mutate(indiv, mutpb):
    """
    Randomly add or subtract a value between 0 and 0.50 with a probability of mutpb
    
    Argument(s):
    indiv - individual represented by points
    mutpb - mutation probability

    Returns a mutated individual as a list
    """
    
    op = random.randint(0,51)/100
    pb = random.randint(0,101)/100
    co = random.randint(0,101)/100
    
    if pb >= mutpb:
        r1 = random.randint(0,1)
        if r1 == 0:
            indiv[co] += op
            if indiv[co] > 0.51:
                indiv[co] = 0.51
        else:
            indiv[co] -= op
            if indiv[co] < 0.01:
                indiv[co] = 0.01 
        return indiv
    else:
        return indiv
    
    pass

def evaluate_foil(indiv):
    """
    Function to evaluate each individual with xfoil 

    Argument: 
    indiv - individual represented by points

    Returns a single length tuple object as the result
    """

    for i in range(50):
        indiv[i] = round(indiv[i],6)
    
    full_string = ''
    for j in range(len(X_COORD)):
        if j < 50:
            full_string += ( ' ' + str(X_COORD[j]) + ' ' + str(indiv[j]) + '\n')
        else:
            full_string += (' ' + str(X_COORD[j]) + ' ' + str(-indiv[len(X_COORD)-j]) + '\n')
    
    file = open('sample16-2.dat','w')

    file.write(full_string)
    
    file.close()
    
    
    # Save the data to sample16-2.dat
    cl,cd = evaluateFoil.call_xfoil()
    print(cl,cd)
    result = cl/cd  # Fitness evaluation, could consider another option
    return (result,)


#CONSIDER USING DEAP 
def mate(indiv, matpb):
    pass

if __name__ == "__main__":
    sample_individual = Individual()
    print(evaluate_foil(sample_individual))
