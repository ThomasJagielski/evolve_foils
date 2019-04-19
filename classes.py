"""
File for definitition of the fitness function, Individual class, ViewIndividual class, Mutate, Evaluate, and Mate functions

These are functions used in the evolutionary algorithm.
"""

import random
import string
import sys

import numpy as np   # Used for statistics
from deap import algorithms
from deap import base
from deap import tools

import evaluateFoil
import createCosineSpacing

# X_COORD = np.linspace(1,0,50).tolist()
# X_COORD.extend(np.linspace(0,1,50).tolist()[1:])
X_COORD = createCosineSpacing.create_x() # Implement cosine spacing in order to define the front and back of the hydrofoils better
                                         # This is useful for a higher success rate with xfoil
# for i in range(len(X_COORD)):
#     X_COORD[i] = round(X_COORD[i],6)


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
        """
        Create a new foil using the NACA airfoils function definition
        """
    # Want to minimize a single objective: distance from the goal message
        self.fitness = FitnessMinimizeSingle()

        # Otherwise, select an initial length between min and max
        # and populate Message with that many random characters
        # def point(t,a,b,c,d,e,n):
        #     point = 500*t*(a*(n/50)**1/2+b*(n/50)+c*(n/50)**2+d*(n/50)**3+e*(n/50)**4)
        #     return point
        # for i in range(50):
        #     self.append(point(1,.2969,-.126,-.3516, .2843,-.1015,X_COORD[i]))

        '''
        For NACA 0016:
        def point(t,a,b,c,d,e,n):
            point = 5*.16*t*(a*(n)**(1/2)+b*(n)+c*(n)**2+d*(n)**3+e*(n)**4)
            return point
        for i in range(50):

            point = point(1,.2969,-.126,-.3516, .2843,-.1015,X_COORD[i])
            point = abs(point)
            self.append(point)
        '''

        # NACA Airfoil function:
        # 5*.16*t*(a*(n)**(1/2)+b*(n)+c*(n)**2+d*(n)**3+e*(n)**4)

        a = random.uniform(0.1,.5) # Define the 'a' coefficient for the NACA airfoil function
        b = random.uniform(-.5,0) # Define the 'b' coefficient for the NACA airfoil function
        c = random.uniform(-.5,0) # Define the 'c' coefficient for the NACA airfoil function
        d = random.uniform(0,.5) # Define the 'd' coefficient for the NACA airfoil function
        e = random.uniform(-.5,0) # Define the 'e' coefficient for the NACA airfoil function
        
        self.append(round(a,4)) # Round 'a' to the nearest 4 decimals for quicker computations
        self.append(round(b,4)) # Round 'b' to the nearest 4 decimals for quicker computations
        self.append(round(c,4)) # Round 'c' to the nearest 4 decimals for quicker computations
        self.append(round(d,4)) # Round 'd' to the nearest 4 decimals for quicker computations
        self.append(round(e,4)) # Round 'e' to the nearest 4 decimals for quicker computations

class ViewIndividual(list):
    

    def __init__(self, data):
        
        for i in range(len(data)):
            self.append(data[i])  # Assume that height shiould not be more than 2 times length
            # self.append(.1)

def mutate(indiv, prob_add, prob_sub):
    """
    Randomly add or subtract a value between 0 and 0.50 with a probability of mutpb
    
    Argument(s):
    indiv - individual represented by points
    mutpb - mutation probability
    prob_add - probability of addition to the individual
    prob_sub - probability of substitution in the individual

    Returns a mutated individual as a list
    """
    index = random.randint(0,4) # Choose a random index (coefficient) for mutating (a, b, c, d, or e)
    # Shows which coefficients must be positive/negative
    # 1 is positive
    # 0 is negative
    pos_neg_coeff = [1,0,0,1,0] # The indicies coorespond to the coefficients a, b, c, d, and e respectively

    # Set the bounds for possible coefficients
    pos_max = 0.5
    neg_max = -0.5

    # Mutation Value
    mut = random.uniform(0,0.5)
    
    if random.uniform(0,1) < prob_add:
        indiv[index] += mut

        # Ensure the value is the correct sign
        if pos_neg_coeff[index] == 1 and indiv[index] < 0:
            indiv[index] = abs(indiv[index])
        if pos_neg_coeff[index] == 0 and indiv[index] > 0:
            indiv[index] = -indiv[index]

        # Ensure the value is within the accepted bounds for a coefficient
        if indiv[index] > pos_max:
            indiv[index] = pos_max
        if indiv[index] < -neg_max:
            indiv[index] = -neg_max
        
    if random.uniform(0,1) < prob_sub:
        indiv[index] -= mut

        # Ensure the value is the correct sign
        if pos_neg_coeff[index] == 1 and indiv[index] < 0:
            indiv[index] = abs(indiv[index])
        if pos_neg_coeff[index] == 0 and indiv[index] > 0:
            indiv[index] = -indiv[index]

        # Ensure the value is within the accepted bounds for a coefficient
        if indiv[index] > pos_max:
            indiv[index] = pos_max
        if indiv[index] < -neg_max:
            indiv[index] = -neg_max

    # Ensure that 'a' is greater than 0.1 to eliminate the 'pencil' hydrofoil cases
    if index == 0 and indiv[index] < 0.1:
        indiv[index] = 0.1

    return (indiv,)
    
    


def evaluate_foil(indiv):
    """
    Function to evaluate each individual with xfoil 

    Argument: 
    indiv - individual represented by points

    Returns a single length tuple object as the result
    """

    def point(t,a,b,c,d,e,n):
        point = 5*t*(a*(n)**(1/2)+b*(n)+c*(n)**2+d*(n)**3+e*(n)**4)
        return point

    
    indiv_y = []

    a = indiv[0]
    b = indiv[1]
    c = indiv[2]
    d = indiv[3]
    e = indiv[4]





    # for i in range(50):

    #     y_coord = point(.16,a,b,c,d,e,X_COORD[i])
    #     if y_coord <= .01:
    #         y_coord = .01
    #     indiv_y.append(y_coord)
    

    
    # Convert the x and y coordinates to strings



    # for i in range(50):
    #     indiv_y[i] = round(indiv_y[i],6)
    
    # full_string = ''
    # for j in range(len(X_COORD)):
    #     if j == 0 or j == len(X_COORD)-1 or j == 49:
    #         full_string += ( ' ' + str(X_COORD[j]) + ' ' + str(0) + '\n')
    #     elif j <= 48:
    #         full_string += ( ' ' + str(X_COORD[j]) + ' ' + str(indiv_y[j]) + '\n')
    #     elif j > 48:
    #         full_string += (' ' + str(X_COORD[j]) + ' ' + str(-indiv_y[len(X_COORD)-j-1]) + '\n')


    for i in range(int(len(X_COORD)/2)):
        y_coord = point(.16,a,b,c,d,e,X_COORD[i])
        if y_coord <= .01:
            y_coord = .01
        indiv_y.append(y_coord)

    
    for i in range(int(len(X_COORD)/2)):
        indiv_y[i] = round(indiv_y[i],6)
    


    full_string = ''
    for j in range(len(X_COORD)):

        if j < len(X_COORD)/2:
            full_string += ( ' ' + str(X_COORD[j]) + ' ' + str(indiv_y[j]) + '\n')
        else:
            full_string += (' ' + str(X_COORD[j]) + ' ' + str(-indiv_y[len(X_COORD)-j-1]) + '\n')

    
    
    # Write the x and y coordinates to a text file with two columns
    # The left column as the x and the right column as the y
    file = open('sample16-2.dat','w')

    file.write(full_string)
    
    file.close()
    
    
    # Save the data to sample16-2.dat
    # Ensure the foil converged and works with xfoil
    # If it does not, assign a fitness score of zero to this foil
    try:
        cl,cd = evaluateFoil.call_xfoil()
    except TypeError:
        result = 0
        return(result,)

    try:
        # result = abs(float(cl))/abs(float(cd))  # Fitness evaluation, could consider another option
        result = abs(float(cl)/float(cd))
    except (ValueError, ZeroDivisionError):
        result = 100
    
    try:
        if float(cl) > 1 or float(cd) <.0005 :
            result = 0
        # print(result)
        return (result,)
    except ValueError:  # Error occurs when xfoil returns a malformatted string because the value is either too high or does nto exist
        return(0,)


#CONSIDER USING DEAP 
def mate(indiv, matpb):
    pass

if __name__ == "__main__":
    sample_individual = Individual()
    print(evaluate_foil(sample_individual))
