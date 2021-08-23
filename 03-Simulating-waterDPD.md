## Simulating waterDPD

This is a guide for running a simple particle simulation with [HOOMD-blue] for research in the [PRoPS Group].

See the HOOMD-blue Installation guide for prerequisites.

This guide is optimized for MacOS and was last updated August 2021.

The standard implementation of HOOMD-blue was adapted for our colloids simulations by Mohammad (Nabi) Nabizadeh. Nabi also created the waterDPD.py file. This guide was compiled by Rob Campbell.

[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/
[PRoPS Group]: https://web.northeastern.edu/complexfluids/
<br>

# Getting the waterDPD.py file

A good way to start working with colloids simulations in HOOMD-blue is to run a dissipative particle dynamics (DPD) simulation of a random distribution of water particles. You will need the waterDPD.py file provided in this repository to run this simulation.

If you haven't already, clone this repository (or a fork of this repository) to your "repositories" directory.
```bash
$ cd repositories/
$ git clone https://github.com/rob10campbell/PRoPS-colloids_setup.git
```
Move to your "HOOMDblue" repository's simulations directory and make a directory for the water simulation
```bash
$ cd ~/repostiories/HOOMDblue/sims/
$ mkdir water
```
Move to the water directory and copy the waterDPD.py file from the cloned copy of this repository to the HOOMDblue/sims/water directory
```bash
$ cd water
$ cp ~/repositories/PRoPS-colloids_setup/waterDPD.py waterDPD.py
$ ls
waterDPD.py
```
<br>

# Running a simulation

Go back to the HOOMDblue directory and activate the virtual environment
```bash
$ cd ..
$ cd ..
$ pwd
/Users/your_username/repositories/HOOMDblue
$ source VirtEnv/bin/activate
(VirtEnv) $
```
You can now move back to the directory for the water simulation and run the file<br>
*Note: The waterDPD.py file intentionally imports several packages when it is run. You will likely be prompted to install some of these packages before you can run the file (e.g. to install gsd, "pip install gsd"). After you have installed any missing packages, try running the file again.*
```bash
(VirtEnv) $ cd sims/water/
(VirtEnv) $ python3 waterDPD.py
```
This should launch HOOMD-blue, display the file, and then run the file. <br>
Successfully running the file will add two new output files to the directory, "Equilibrium.gsd" and "Pressure_xy.log"
```bash
(VirtEnv) $ ls
Equilibrium.gsd	Pressure_xy.log	waterDPD.py
```
You can open Pressure_xy.log with vim or another text editor to see the recorded temperature and pressure at each timestep. 
```bash
(VirtEnv) $ vim Pressure_xy.log
```
The gsd file will generate a visualization of the particles, which we will view in VMD.
<br>
<br>
See the VMD Installation Guide for next steps. 
