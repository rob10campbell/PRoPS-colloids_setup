import copy
import hoomd
import hoomd.md
import hoomd.deprecated
import hoomd.comm
import numpy
import time
import ctypes
import math
import hoomd.init
import gsd
import gsd.pygsd
import gsd.hoomd
import inspect
import random
import array
import hoomd.example_plugin;
import os
import csv
################           INPUTS             ##############
N_time_steps = 1000;L_X = 10; L_Y = 10; L_Z = 10;
dt_Integration = 0.01; m_S = 1; R_S = 0.5;
r_c = 1; rho = 3; KT = .1; 
###############################
V_total = L_X*L_Y*L_Z;
V_Solvents = V_total; 
N_Solvents = math.floor(rho * V_Solvents);  
simulation_seed =  random.randint(1, 100001)
 #################        Total INITIALIZATION        ##############
hoomd.context.initialize("");
hoomd.deprecated.init.create_random(N=N_Solvents, box=hoomd.data.boxdim(Lx=L_X, Ly=L_Y, Lz=L_Z), name='A', min_dist=0., seed=random.randint(1, 101), dimensions=3)

nl = hoomd.md.nlist.tree();
groupA = hoomd.group.type(name='groupA', type='A');
 
dpd = hoomd.md.pair.dpd(r_cut= 1 * r_c, nlist=nl, kT=KT, seed=simulation_seed);
dpd.pair_coeff.set('A', 'A', r_cut= 1.0 * r_c, A=25, gamma=4.5);

hoomd.md.integrate.mode_standard(dt=dt_Integration);
all = hoomd.group.all();
hoomd.md.integrate.nve(group = all);


hoomd.dump.gsd(filename="Equilibrium.gsd", overwrite=True, period=1, group=all, dynamic=['attribute', 'momentum', 'topology']) 
hoomd.analyze.log(filename='Pressure_xy.log', overwrite=True , 
                  quantities=['pressure_xy','temperature'],period=1)
hoomd.run(N_time_steps); 



