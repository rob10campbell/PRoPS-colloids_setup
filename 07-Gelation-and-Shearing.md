# Gelation and Shearing of Colloidal Particles

This is an overview of the workflows for running gelation and shearing simulations of colloidal particles with [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/) for research in the [PRoPS Group](https://web.northeastern.edu/complexfluids/).

This guide is optizimed for MacOS. Before running gelation or shearing simulations you should have already [installed HOOMD-blue](/01-HOOMDblue-Install-Guide.md), run a [basic DPD simulation of water](/02-Simulating-waterDPD.md), [installed](/03-VMD-Install-Guide.md) and [worked with](/04-Using-VMD.md) VMD to visualize your simulation, [run basic checks on the simulation](/05-Log-Analysis-with-R.md) using R to verify it ran correctly, and [modified a version of HOOMD-blue](/06-Modifying-HOOMDblue.md) for more advanced simulations.

[Last Update: December 2021]

These workflows were developed by Mohammad (Nabi) Nabizadeh. This guide was compiled by Rob Campbell.
<br>

## Background

For more background on these simulations, see:

* Background on DPD
	* "[Viscosity measurement techniques in Dissipative Particle Dynamics]" (2015)
	* "[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation]" (1997)

* Background on simulating colloidal gel rheology
	* "[Microstructural Rearrangements and their Rheological Implications in a Model Thixotropic Elastoviscoplastic Fluid]" (2017)
	* "[Time-rate-transformation framework for targeted assembly of short-range attractive colloidal suspensions]" (2020)
	* "[Life and death of colloidal bonds control the rate-dependent rheology of gels]" (2021)

[Viscosity measurement techniques in Dissipative Particle Dynamics]:https://doi.org/10.1016/j.cpc.2015.05.027
[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation]:https://doi.org/10.1063/1.474784
[Microstructural Rearrangements and their Rheological Implications in a Model Thixotropic Elastoviscoplastic Fluid]:https://doi.org/10.1103/PhysRevLett.118.048003
[Time-rate-transformation framework for targeted assembly of short-range attractive colloidal suspensions]:https://doi.org/10.1016/j.mtadv.2019.100026
[Life and death of colloidal bonds control the rate-dependent rheology of gels]:https://doi.org/10.1038/s41467-021-24416-x

## Overview 

There are 7 steps to making a colloidal gel and shearing it:

[1] Run the gelation simulation (with a Python script using HOOMD-blue)

[2] Check that the simulation reached a quasi-steady state (see [Log Analysis with R](/05-Log-Analysis-with-R.md))

[3] \(*IF gelation was run in segments*) Combine the data from all the gelation simulation restarts and update the particle interaction lifetimes across all gelation simulation restarts

[4] Shear the gel from quasi-steady state (with a Python script using HOOMD-blue)

[5] Check that the sheared gel has reached a new quasi-steady state

[6] \(*IF gelation was run in segments*) Use the updated lifetimes from step [3] to update the particle interaction lifetimes in the shearing simulation

[7] \(*IF shearing was run in segments*) Use the updated lifetimes from step [6] to update the particle interaction lifetimes in the remaining shearing simulation restarts
<br>

## [1] Gelation simulations

Our gelation simulations are meso-scale, with a typical colloid particles radius of ~1micron (we do not do molecular dynamics). These simulatuions capture local interactions that can be used to represent large scale system properties.We achieve this by using:
* Lees-Edwards boundary conditions (as discussed when [describing our modifications to HOOMD-blue](/06-Modifying-HOOMDblue.md))
* a large number of colloidal particles (500-25,000; typically we use ~10,000)
* a simulation box of at least side-length 30 units (we typically use between L=50 and L=60 for a robust analysis and efficient simulation cost)
* relative parameters (e.g. relative viscosity, etc.)
* and a unit energy normalized by the system temperature (i.e. Boltzman constant types temperature) kT

The choice of kT and the DPD timestep (dt) used to advance the system are interconnected, as particle motion (and therefore particle interaction) varies with the magnitude of the Brownian forces. For general particle simulations researchers usually use kT = 0.5, but for colloids a lower kT = 0.1 is a bit better. If you're simulating a Newtonian fluid like water, then kT = 1 would be okay. You can even go as high as kT = 10 for some simulations, but at that point you usually have to start decreasing the timestep in order to capture enough interaction detail.

Our code requires the following inputs:
* Volume fraction "phi"
* "D0" (normalized by kT) and "alpha" from the Morse Potential energy function
* The cut off distance for particle interaction "r_cut" (typically ~0.1)
* The number of particles in a unit volume: number density "rho" (set to 3)
* The colloidal radius (usually set to 1, for a volume of 4/3 pi r cubed, or ~4.18879)
* Two DPD parameters: "A" (the conservative coefficient) and "gamma" 
* The unit energy normalized by system temperature k

People report gels at D0 values as low as 4kT, but for faster simulation times we start higher (at 6kT). *NOTE: 6kT already requires around twice the simulation time as higher kT values, and we expect 4kT would be even longer* 

We also need to define the particle types.A basic colloidal simulation has two "types" of particles, "type A" (solvent) particles and "type B" (colloid particles). In addition to using these type classes to define different interparticle interactions, they can also be used in VMD to load segments of the total simulation (reducing the cost of visualization and allowing for greater clarity visualizing only colloid-colloid interactions). You can add additional particle types for multi-component systems, to build walls in the system, etc. Our simulations typically use water as a solvent, with each "type A" particle representing 3 water molecules loosely bound together in a sphere. This is important to note because it does allow type A particles to overlap slightly at the surface of one and other (and with the surface of colloidal particles) without the simulation becoming non-physical. Any small part of the type A sphere that overlaps with another surface can be explained as the space between water molecules. That said, these particles should not cluster inside the center of colloidal particles, which is non-physical and would indicate an error in the simulation. Type B particles are simulated as hard spheres that do not overlap with other particles. They are typically ~1 micron in diameter, although we define our particle sizes relativistically, and in relation to the cut-off distance.

Less that 0.5 percent of the simulation cost is the colloidal particles; by far the largest factor in simulation cost is the **number of solvent particles**. Simulations with high volume fractions of colloidal particles will have to LOWER simulation costs (and typically gel faster).

A gelation simulation follows roughly the same format as our [DPD simulation of water](/02-Simulating-waterDPD.md): 
* Initialize a simulation box with a random distribution of particles (allowing particles to overlap)
* Initialize a neighboring list (the neighboring list method will vary with your choice of system; for our simulations we found that the tree method offers significant speed improvements over the cell method)
* Use DPD (as set by `A`, `gamma`, and the cutoff-radius `r_cut`) to calculate the interactions between particles. *NOTE: Our DPD model uses a combination of conservative force, dissipative force, and random force. We do not need to set parameters for the random force because it is Brownian (i.e. calculated directly from temperature)*
* Choose what to happens after one timestep (i.e. Velocity-Verlet integration `nve`) and set the time interval for this (dt = 0.01)
* Define the outputs (e.g. GSD, LOG, etc.)
* Run the simulation!



## Shearing

About shearing simulations.
