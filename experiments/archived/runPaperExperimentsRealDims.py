import numpy as np
from os.path import join
import subprocess
import os
import shutil
import pandas as pd
import sys
import random
"""
Generates the command line parameters and runs the agent-based model, NeuralCrestCpp

Created: August 2020
Author: Dylan Feldner-Busztin
"""

slurm_array_task = sys.argv[1]

# Path to executable
EXE_DIR = os.path.dirname(os.path.realpath(__file__)).replace('experiments','')


Nc = 4
zeta_mag = 0.003
cellradius = 0.13
PMZwidth = 1
CEwidth = 0.4
CMwidth = CEwidth
Clength = 0.62 # 1 - 0.24/2 taking into account the middle zone
#middle_zone_space = 0.24
PMZheight = 0.26

t_max = 30
dt = 0.1
output_interval = 0.25
chainShape = 2
realTimePlot = 1

follower_k = 0.000003
follower_De = 3e-06
follower_autonomousMag = 5e-07 * 3 * 2
follower_interactionThreshold = 1
follower_gradientSensitivity = 0

leader_k = follower_k
leader_De = 9e-06
leader_autonomousMag = 1e-07 * 9
leader_interactionThreshold = follower_interactionThreshold
leader_gradientSensitivity = 0
leader_size = cellradius

runMany = True

granularity = 3

#lamaglist = np.linspace(follower_autonomousMag, follower_autonomousMag * 3, granularity)
amaglist = np.linspace(follower_autonomousMag, follower_autonomousMag * 3 *1.6666666666666, granularity*2)
Delist = np.linspace(follower_De/ 27, follower_De* 27, granularity)
klist = np.linspace(follower_k/ 27, follower_k*27, granularity)


if runMany == True:

    for i in range(1):

        for lamag in amaglist:
            for famag in amaglist:

                for lDe in Delist:
                    for fDe in Delist:

                        for lk in klist:
                            for fk in klist:

                                for 

                                for ET in [17, 19, 20, 23]:#

                                    #slurm_array_task = 1
                                    run = int(random.uniform(0,5000))


                                    # Create the executable
                                    EXE = '/NeuralCrest {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(
                                        Nc,
                                        zeta_mag,
                                        cellradius,
                                        PMZwidth,
                                        PMZheight,
                                        CEwidth,
                                        CMwidth,
                                        Clength,
                                        t_max,
                                        dt,
                                        output_interval,
                                        chainShape,
                                        realTimePlot,
                                        ET,
                                        lk,
                                        lDe,
                                        lamag,
                                        leader_interactionThreshold,
                                        leader_gradientSensitivity,
                                        leader_size,
                                        fk,
                                        fDe,
                                        famag,
                                        follower_interactionThreshold,
                                        follower_gradientSensitivity,
                                        slurm_array_task,
                                        run
                                        )

                                    print(EXE)


                                    completed_run = subprocess.run([EXE_DIR+EXE],
                                                                    shell=True,
                                                                    cwd= EXE_DIR)


else:


    for lamag in lamaglist:

        for fDe in fDelist:

            for lk in lklist:


                for ET in [19, 20, 25, 23]:#

                    run = int(random.uniform(0,5000))


                    # Create the executable
                    EXE = '/NeuralCrest {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(
                        Nc,
                        zeta_mag,
                        cellradius,
                        PMZwidth,
                        PMZheight,
                        CEwidth,
                        CMwidth,
                        Clength,
                        t_max,
                        dt,
                        output_interval,
                        chainShape,
                        1,
                        ET,
                        lk,
                        fDe,
                        lamag,
                        leader_interactionThreshold,
                        leader_gradientSensitivity,
                        leader_size,
                        follower_k,
                        follower_De,
                        follower_autonomousMag,
                        follower_interactionThreshold,
                        follower_gradientSensitivity,
                        slurm_array_task,
                        run,
                        middle_zone_space
                        )

                    print(EXE)


                    completed_run = subprocess.run([EXE_DIR+EXE],
                                                    shell=True,
                                                    cwd= EXE_DIR)

