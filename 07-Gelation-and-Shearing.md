# Gelation and Shearing of Colloidal Particles

This is an overview of the workflows for running gelation and shearing simulations of colloidal particles with [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/) for research in the [PRoPS Group](https://web.northeastern.edu/complexfluids/).

This guide is optizimed for MacOS. Before running gelation or shearing simulations you should have already [installed HOOMD-blue](/01-HOOMDblue-Install-Guide.md), run a [basic DPD simulation of water](/02-Simulating-waterDPD.md), [installed](/03-VMD-Install-Guide.md) and [worked with](/04-Using-VMD.md) VMD to visualize your simulation, [run basic checks on the simulation](/05-Log-Analysis-with-R.md) using R to verify it ran correctly, and [modified a version of HOOMD-blue](/06-Modifying-HOOMDblue.md) for more advanced simulations.

[Last Update: December 2021]

These workflows were developed by Mohammad (Nabi) Nabizadeh. This guide was compiled by Rob Campbell.
<br>

## Background

For more background on these simulations, see the following papers:

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

Gelation (see [About Gelation Simulations](/07-Gelation-and-Shearing.md#about-gelation-simulations) for details)

[1]- [Run the gelation simulation](/07-Gelation-and-Shearing.md#1-running-a-gelation-simulation) (with a Python script using HOOMD-blue)

[2]- [Check that the simulation](/07-Gelation-and-Shearing.md#2-checking-gelation) reached a quasi-steady state without errors 

[3]- \(*IF gelation was run in segments*) [Update the particle interaction lifetimes](/07-Gelation-and-Shearing.md#3-updating-lifetimes) across all gelation simulation restarts and combine any additional simulation data for analysis

Shearing (see [About Shearing Simulations](/07-Gelation-and-Shearing.md#about-shearing-simulations) for details)

[4]- [Shear the gel](/07-Gelation-and-Shearing.md#4-running-a-shearing-simulation) from quasi-steady state (with a Python script using HOOMD-blue)

[5]- [Check that the sheared gel](/07-Gelation-and-Shearing.md#5-checking-shearing) has reached a new quasi-steady state

[6]- \(*IF gelation was run in segments*) Use the updated lifetimes from step [3] to [update the particle interaction lifetimes](/07-Gelation-and-Shearing.md#6-7-updating-shear-lifetimes) in the shearing simulation

[7]- \(*IF shearing was run in segments*) Use the updated lifetimes from step [6] to [update the particle interaction lifetimes](/07-Gelation-and-Shearing.md#6-7-updating-shear-lifetimes) in the remaining shearing simulation restarts
<br>

## About Gelation Simulations

Our gelation simulations are meso-scale simlations of attractive colloidal particles in a given volume fraction (phi), with a typical colloid particles radius of ~1micron. We do not do molecular dynamics. We also do not do continuum simulations, our solvent is also simulated as particles (typically representing small groups of molecules). Less that 0.5% of the simulation cost goes to simulating colloidal particles; by far the largest factor in simulation cost is the **number of solvent particles**. Simulations with high volume fractions of colloidal particles will therefore have LOWER simulation costs (and typically gel faster).

Our simulatuions capture local interactions that also represent large scale system properties. We ensure this relationship between local and large-scale properties by using:
* Lees-Edwards boundary conditions (as discussed when [describing our modifications to HOOMD-blue](/06-Modifying-HOOMDblue.md))
* a large number of colloidal particles (500-25,000; typically we use ~10,000)
* a simulation box of at least side-length 30 units (we typically use between L = 50 and L = 60 to balance a robust analysis and efficient simulation cost)
* relative parameters (e.g. defining relative viscosity, etc.)
* and a unit energy normalized by the system temperature kT (i.e. Boltzman constant times temperature)

The simulation advances through time in intervals defined by a DPD timestep (dt). The choice of kT and dt are interconnected. Particle motion (and therefore particle interaction) varies with the magnitude of the Brownian forces (as calculated from temperature kT). The magnitude of this motion will affect the timestep that is needed to capture meaningful changes in the system. For general particle simulations researchers usually use kT = 0.5, but for colloids a lower kT = 0.1 is a bit better. If you're simulating a Newtonian fluid like water, then kT = 1 would be okay. You can even go as high as kT = 10 for some simulations, but at that point you usually have to start decreasing the timestep in order to capture enough interaction details.

Our particles' attractiveness is set by the parameters "D0" and "alpha" in the Morse Potential energy function. People report gels at D0 values as low as 4kT, but for faster simulation times we start higher (at 6kT). *NOTE: 6kT already requires around twice the simulation time as higher kT values, and we expect 4kT would be even longer* 

Our code therefore requires the following inputs:
* Volume fraction "phi"
* "D0" (normalized by kT) and "alpha" from the Morse Potential energy function
* The unit energy (normalized by system temperature) kT
* The cut off distance for particle interaction "r_cut" (typically ~0.1)
* The number of particles in a unit volume: number density "rho" (typically set to 3)
* The colloidal radius (typically set to 1, for a particle volume of 4/3 pi r cubed, or ~4.18879)
* Two DPD parameters: "A" (the conservative coefficient) and "gamma" (for dissipative force) *NOTE: Our DPD force is a combination of conservative force, dissipative force, and random force. We do not need to set parameters for the random force because it is Brownian (i.e. calculated directly from temperature)*=

We also need to define the particle types. A basic colloidal simulation has two "types" of particles, "type A" (solvent) particles and "type B" (colloid particles). In addition to using these type classes to define different interparticle interactions, they can also be used in VMD to load segments of the total simulation (reducing the cost of visualization and allowing for greater clarity visualizing only colloid-colloid interactions). You can add additional particle types for multi-component systems, to build walls in the system, etc. 

Our simulations typically use water as a solvent, with each type A particle representing 3 water molecules loosely bound together in a sphere. This is important to note because it does allow type A particles to overlap slightly at the surface of one and other (and with the surface of colloidal particles) without the simulation becoming non-physical. Any small part of the type A sphere that overlaps with another surface can be explained as the space between water molecules. That said, these particles should not cluster inside the center of colloidal particles, which is non-physical and would indicate an error in the simulation. 

Type B particles are simulated as hard spheres that do not overlap with other particles. As noted above, our colloids are typically ~1 micron in diameter, although we define size within the simulation relativistically.
<br>

## [1] Running a Gelation Simulation

A gelation simulation follows roughly the same format as our [DPD simulation of water](/02-Simulating-waterDPD.md): 
* Initialize a simulation box with a random distribution of particles (allowing particles to overlap)
* Initialize a neighboring list (the neighboring list method will vary with your choice of system; for our simulations we found that the tree method offers significant speed improvements over the cell method)
* Use DPD (as set by `A`, `gamma`, and the cutoff-radius `r_cut`) to calculate the interactions between particles. i
*NOTE: Our DPD model uses a combination of conservative force, dissipative force, and random force. We do not need to set parameters for the random force because it is Brownian (i.e. calculated directly from temperature)*
* Choose what to happens after one timestep (i.e. Velocity-Verlet integration `nve`) and set the time interval for this (dt = 0.01)
* Define the outputs (e.g. GSD, LOG, etc.)
* Run the simulation!

***A Note on Parallelization***<br>
HOOMD-blue supports some parallelization options; unfortunately, it seems that our modifications currently break them. We have attempted to fix this but as of yet it is NOT possible to run these simulations in parallel and accurately track all particle interactions. All of our simulations MUST be run serially; therefore, large gelation simulations will take upwards of 1-2 months to run on the Discovery cluster. To do that, we must run the simulation in segments. Each gelation simulation is run for about 3 days, generating 11 frames of data, and then stopped. The next day the simulation can be restarted from frame 10 (giving us a potential comparison between frame 11 and frame 2 to verify that the simulation is continuing from where it left off without error). This process is repeated for the number of restarts needed to reach a quasi-steady state (typically somewhere between 9-13). Once all of the restarts are completed and the gel is confirmed to have 

## [2] Checking Gelation

A gel is completed when 
(see [Log Analysis with R](/05-Log-Analysis-with-R.md))

## [3] Updating Lifetimes

## About Shearing Simulations

About shearing simulations.

## [4] Running a Shearing Simulation

## [5] Checking Shearing

## [6]-[7] Updating Shear Lifetimes
