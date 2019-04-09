"""Evolutionary algorithm, attempts to evolve a given message string.

Uses the DEAP (Distributed Evolutionary Algorithms in Python) framework,
http://deap.readthedocs.org

"""

import random
import string
import sys

import numpy    # Used for statistics
from deap import algorithms
from deap import base
from deap import tools
import classes


# -----------------------------------------------------------------------------
#  Global variables
# -----------------------------------------------------------------------------

# Allowable characters include all uppercase letters and space
# You can change these, just be consistent (e.g. in mutate operator)


# Control whether all Messages are printed as they are evaluated
VERBOSE = True



# -----------------------------------------------------------------------------
# DEAP Toolbox and Algorithm setup
# -----------------------------------------------------------------------------

def get_toolbox():
    """Return a DEAP Toolbox configured to evolve given 'text' string."""

    # The DEAP Toolbox allows you to register aliases for functions,
    # which can then be called as "toolbox.function"
    toolbox = base.Toolbox()

    # Creating population to be evolved
    toolbox.register("individual", classes.Individual)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Genetic operators
    toolbox.register("evaluate", classes.evaluate_foil)
    # toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", classes.mutate)
    toolbox.register("select", tools.selTournament, tournsize=3)

    # NOTE: You can also pass function arguments as you define aliases, e.g.
    #   toolbox.register("individual", Message, max_length=200)
    #   toolbox.register("mutate", mutate_text, prob_sub=0.18)

    return toolbox


def evolve():
    """Use an evolutionary algorithm (EA) to evolve 'text' string."""

    # Set random number generator initial seed so that results are repeatable.
    # See: https://docs.python.org/2/library/random.html#random.seed
    #      and http://xkcd.com/221
    # random.seed(4)

    # Get a configured toolbox and create a population of random Messages
    toolbox = get_toolbox()
    pop = toolbox.population(n=20)

    # Collect statistics as the EA runs
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    hof  = tools.HallOfFame(1)

    # Run simple EA
    # (See: http://deap.gel.ulaval.ca/doc/dev/api/algo.html for details)
    pop, log = algorithms.eaSimple(pop,
                                   toolbox,
                                   cxpb=0.5,    # Prob. of crossover (mating)
                                   mutpb=0.2,   # Probability of mutation
                                   ngen=5,
                                   halloffame = hof,    # Num. of generations to run
                                   stats=stats)

    return pop, log, hof


# -----------------------------------------------------------------------------
# Run if called from the command line
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Get goal message from command line (optional)
    # if len(sys.argv) == 1:
    #     # Default goal of the evolutionary algorithm if not specified.
    #     # Pretty much the opposite of http://xkcd.com/534
    #     goal = "SKYNET IS NOW ONLINE"
    # else:
    #     goal = " ".join(sys.argv[1:])

    # Verify that specified goal contains only known valid characters
    # (otherwise we'll never be able to evolve that string)
    # for char in goal:
    #     if char not in VALID_CHARS:
    #         msg = "Given text {goal!r} contains illegal character {char!r}.\n"
    #         msg += "Valid set: {val!r}\n"
    #         raise ValueError(msg.format(goal=goal, char=char, val=VALID_CHARS))

    # Run evolutionary algorithm
    pop, log, hof = evolve()
    classes.evaluate_foil(hof)
