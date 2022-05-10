# Colloids Simulation Setup Guide

This is a how-to guide for getting setup to do colloids simulations in the [PRoPS Group] using [HOOMD-blue]v3.1 and [MPI]

**WARNING: This guide is in the process of being updated for v3.1, IT IS INCOMPLETE. Contact Rob before using for information about what is ready to use**

[PRoPS Group]: https://web.inortheastern.edu/complexfluids/
[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/
[MPI]: https://www.open-mpi.org/

[Last Update: May 2022]
<br>
<br>
## Before you Begin

The [System Setup folder](/System-Setup) contains information for choosing a laptop or other workstation and steps for setting up a new MacOS computer before installing HOOMD-blue.

The [Programming Resources folder](/Programming-Resources) contains a variety of resources that can help you with the command line, VIM, Python, R, C++, Git/Github, and other skills that are useful for our work.

Once you have received your computer, the remaining files should help you install HOOMD-blue and VMD and give you the information you need to get started with colloids simulations!
<br>
<br>
## Installing Software and Running Simulations

These guides are numbered to follow the steps for getting set up with HOOMD-blue, VMD, and other related tools for running and analyzing simulation data:

*NOTE: This guide is written for HOOMD-blue v3.1*

1. [The HOOMD-blue Installation Guide](/01-HOOMDblue-Install-Guide.md)

2. An introduction to running HOOMD-blue simulations: [Simulating waterDPD](/02-Simulating-waterDPD.md)

3. [The VMD Installation Guide](/03-VMD-Install-Guide.md)

4. An introdcution to visualizing `.gsd` files in VMD: [Using VMD](/04-Using-VMD.md)

5. The guide to analyzing `.log` files in R: [Log Analysis with R](/05-Log-Analysis-with-R.md)

6. A guide to installing our modifications to HOOMD-blue: [Modifying HOOMD-blue](/06-Modifying-HOOMDblue.md)

7. An overview of the steps involved in colloid gelation and shearing: [Gelation and Shearing](/07-Gelation-and-Shearing.md)

8. [The Guide to Accessing "Discovery"](/08-Accessing-Discovery.md) (Northeastern's HPC cluster)

9. An [introduction to running HPC simulations](/09-Slurm-and-Disco.md)
