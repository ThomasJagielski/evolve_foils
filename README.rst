:Name: Evolving Hydrofoils using DEAP - Software Design, Olin College
:Authors: Colin Snow, Sparsh Bansal, Thomas Jagielski
:Version: 1.0

Evolving Hydrofoils is an application of Evolutionary Algorithms offered in the DEAP to evolve hydrofoils, analysed on the basis of the ratio of Coefficient of Drag (Cd) with Coefficient of Lift (Cl). The physical quantities are determined using  a FORTRAN based script, XFOIL, a subsonic airfoil development system. This is the final project whcih was developed by the authors during Software Design, a class at Olin College of Engineering.

============

Evolving Hydrofoils Version 1.0 requires the following Python packages

A. classes.py

.. code-block:: python

    import random
    import string
    import sys
    import numpy as np   # Used for statistics
    from deap import algorithms
    from deap import base
    from deap import tools
    
============    

B. editAirfoil.py

.. code-block:: python

    import subprocess as sp
    import shutil
    import sys
    import string
    import time
    import pandas as pd
    import os
    import evaluateFoil
    import random
    import numpy as np
    
============

C. evaluateFoil.py

.. code-block:: python

    import subprocess as sp
    import shutil
    import sys
    import string
    import time
    import pandas as pd
    import os

============

D. evolveAirfoil.py

.. code-block:: python

    import random
    import string
    import sys
    import numpy    # Used for statistics
    from deap import algorithms
    from deap import base
    from deap import tools
    import classes

Installation
============

The easiest and fastest way to get the packages up and running:

.. code-block:: python

    sudo apt-get install python-opencv
    sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-noseimport requests

In order to install timidity, input the following on the command line:
    sudo apt-get install timidity

In order for the player to work, the envrionment must be set. The base location is included in the code. If your MIDI player is in a different location, it must be updated for this code to function.

Set location:
     environment.set('midiPath', '/path/location/')
Default location:
     'usr/bin/timidity' 
  
Documentation
=============

We have added comments for every line of code that we felt could be beneficial for someone to understand the program

Note: We haved added comments especially on the imported packages and code so that we can fully understand the code written by someone else. We have cited the sources wherever appropriate. 

More documentation can be found in the file documentation.txt

Contributing Works
==================

We used information from:

:i: Think Python - Allen Downey

:ii: SciPy.org

:iii: OpenCV

:iiii: User's Guide, music21 (MIT)

Source URLs:
======
Think Python:
https://www.greenteapress.com/thinkpython/thinkpython.pdf

Music21:
https://web.mit.edu/music21/doc/usersGuide/index.html
