# Gelation and Shearing of Colloidal Particles

This is an overview of the workflows for running gelation and shearing simulations of colloidal particles with [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/) for research in the [PRoPS Group](https://web.northeastern.edu/complexfluids/).

This guide is optizimed for MacOS. Before running gelation or shearing simulations you should have already [installed HOOMD-blue](/01-HOOMDblue-Install-Guide.md), run a [basic DPD simulation of water](/02-Simulating-waterDPD.md), [installed](/03-VMD-Install-Guide.md) and [worked with](/04-Using-VMD.md) VMD to visualize your simulation, [run basic checks on the simulation](/05-Log-Analysis-with-R.md) using R to verify it ran correctly, and [modified a version of HOOMD-blue](/06-Modifying-HOOMDblue.md) for more advanced simulations.

[Last Update: December 2021]

These workflows were developed by Mohammad (Nabi) Nabizadehi as part of his PhD thesis. This guide was compiled by Rob Campbell.
<br>
<br>
## Overview 

Details [about simulating the gelation of colloidal particlese](/07-Gelation-and-Shearing.md#about-gelation-simulations) and [shearing a colloidal gel](/07-Gelation-and-Shearing.md#about-shearing-simulations) are described in separate sections, below.

There are 7 steps to making a colloidal gel and shearing it:

[1]- [Run the gelation simulation](/07-Gelation-and-Shearing.md#1-running-a-gelation-simulation) (with a Python script using HOOMD-blue)

[2]- [Check that the simulation](/07-Gelation-and-Shearing.md#2-checking-gelation) reached a quasi-steady state without errors 

[3]- \(*IF gelation was run in segments*) [Update the particle interaction lifetimes](/07-Gelation-and-Shearing.md#3-updating-lifetimes) across all gelation simulation restarts and combine any additional simulation data needed for analysis

[4]- [Shear the gel](/07-Gelation-and-Shearing.md#4-running-a-shearing-simulation) from quasi-steady state (with a Python script using HOOMD-blue)

[5]- [Check that the sheared gel](/07-Gelation-and-Shearing.md#5-checking-shearing) has reached a new quasi-steady state

[6]- \(*IF gelation was run in segments*) Use the updated lifetimes from step [3] to [update the particle interaction lifetimes](/07-Gelation-and-Shearing.md#6-7-updating-shear-lifetimes) in the shearing simulation

[7]- \(*IF shearing was run in segments*) Use the updated lifetimes from step [6] to [update the particle interaction lifetimes](/07-Gelation-and-Shearing.md#6-7-updating-shear-lifetimes) in the remaining shearing simulation restarts
<br>
<br>
## About Gelation Simulations

Our gelation simulations are meso-scale simlations of attractive colloidal particles in a given volume fraction (phi), with a typical colloid particles radius of ~1micron. We do not do molecular dynamics. We also do not do continuum simulations, our solvent is also simulated as particles (typically representing small groups of molecules). 

Less that 0.5% of the simulation cost goes to simulating colloidal particles; by far the largest factor in simulation cost is the **number of solvent particles**. Simulations with high volume fractions of colloidal particles will therefore have LOWER simulation costs (and typically gel faster).

Our simulatuions capture local interactions that also represent large scale system properties. We ensure this relationship between local and large-scale properties by using:
* Lees-Edwards boundary conditions (as discussed when [describing our modifications to HOOMD-blue](/06-Modifying-HOOMDblue.md))
* a large number of colloidal particles (500-25,000; typically we use ~10,000)
* a simulation box of at least side-length 30 units (we typically use between L = 50 and L = 60 to balance a robust analysis and efficient simulation cost)
* relative parameters (e.g. defining relative viscosity, etc.)
* and a unit energy normalized by the system temperature kT (i.e. Boltzman constant times temperature)

The simulation advances through time in intervals defined by a DPD timestep (dt). The choice of kT and dt are interconnected. Particle motion (and therefore particle interaction) varies with the magnitude of the Brownian forces (as calculated from temperature kT). The magnitude of this motion will affect the timestep that is needed to capture meaningful changes in the system. For general particle simulations researchers usually use kT = 0.5, but for colloids a lower kT = 0.1 is a bit better. If you're simulating a Newtonian fluid like water, then kT = 1 would be okay. You can even go as high as kT = 10 for some simulations, but at that point you usually have to start decreasing the timestep in order to capture enough interaction details.

Interparticle attraction is set by the parameters "D0" and "alpha" in the Morse Potential energy function. This could represent a variety of attraction types, and the simulation does not depend on a specific physical mecahnicsm (electrostatics, depletion, etc.). People report gels at D0 values as low as 4kT, but for faster simulation times we start higher (at 6kT). *NOTE: 6kT already requires around twice the simulation time as higher kT values, and we expect 4kT would be even longer* 

Our code therefore requires the following inputs:
* Volume fraction "phi"
* "D0" (normalized by kT) and "alpha" from the Morse Potential energy function
* The unit energy (normalized by system temperature) kT
* The DPD timestep dt (typically 0.01)
* The cut off distance for particle interaction "r_cut" (typically ~0.1)
* The number of particles in a unit volume: number density "rho" (typically set to 3)
* The colloidal radius (typically set to 1, for a particle volume of 4/3 pi r cubed, or ~4.18879)
* Two DPD parameters: "A" (the conservative coefficient) and "gamma" (for dissipative force) *NOTE: Our DPD force is a combination of conservative force, dissipative force, and random force. We do not need to set parameters for the random force because it is Brownian (i.e. calculated directly from temperature)*

We also need to define the particle types. A basic colloidal simulation has two "types" of particles, "type A" (solvent) particles and "type B" (colloid particles). In addition to using these type classes to define different interparticle interactions, they can also be used in VMD to load segments of the total simulation (reducing the cost of visualization and allowing for greater clarity visualizing only colloid-colloid interactions, etc.). You can add additional particle types for multi-component systems, to build walls in the system, etc. 

Our simulations typically use water as a solvent, with each type A particle representing 3 water molecules loosely bound together in a sphere. This is important to note because it does allow type A particles to overlap slightly at the surface of one and other (and with the surface of colloidal particles) without the simulation becoming non-physical. Any small part of the type A sphere that overlaps with another surface can be explained as the space between water molecules. That said, these particles should not cluster inside the center of colloidal particles, which is non-physical and would indicate an error in the simulation. 

Type B particles are simulated as hard spheres that do not overlap with other particles. As noted above, our colloids are typically ~1 micron in diameter, although we define size within the simulation relativistically.

If you'd like to make changes to specific particles (for example, fix their position to form a wall or change mass, velocity, diameter, etc.), an easy way to do this is to define the system as variable you can interact with. For example, for the `waterDPD.py` system, you would set
```python
system = hoomd.deprecated.init.create_random(N=N_Solvents, box=hoomd.data.boxdim(Lx=L_X, Ly=L_Y, Lz=L_Z), name='A', min_dist=0., seed=random.randint(1, 101), dimensions=3)
```
You can use other parameters to extract specific types of information from the system. For example, to access position, use `getPosition`
```python
pos = system.particles.pdata.getPosition 
```
and further specify a specific coordinate with
```python
x = pos.x
y = pos.y
z = pos.z
```
To change position of a particle to the origin, use `setPosition`
```python
system.particles.pdata.setPosition(0, pos, True)
```
*Note: we use the `set` and `get` commands to access these parameters because in C++ `system` is defined as a private class (to prevent these attributes from being easily/accidentally changed by the user)*
<br>
<br>
## [1] Running a Gelation Simulation

A gelation simulation follows roughly the same format as our [DPD simulation of water](/02-Simulating-waterDPD.md): 
* Initialize a simulation box with a random distribution of particles (allowing particles to overlap)
	* This step occurs for both the solvent particles and the colloid particles. In both steps the system is run briefly to equilibrium, to resolve any non-physical particle overlaps generated by the initial random distribution
* Initialize a neighboring list (the neighboring list method will vary with your choice of system; for our simulations we found that the tree method offers significant speed improvements over the cell method)
* [*NEW*] Set the different particle types (i.e. "type A", "type B", etc.) with `hoomd.group.type()` 
* Use DPD (as set by `A`, `gamma`, and the cutoff-radius `r_cut`) to calculate the interactions between particles. *NOTE: Our DPD model uses a combination of conservative force, dissipative force, and random force. We do not need to set parameters for the random force because it is Brownian (i.e. calculated directly from temperature)*
	* This step will now specify the interactions between multiple sets of particle types (i.e. A-A, A-B, and B-B)
* Choose what to happens after one timestep (i.e. standard integration or Velocity-Verlet integration `nve`) and set the time interval for this (dt = 0.01)
* Define the outputs (e.g. GSD, LOG, etc.)
* Run the simulation!

***A Note on Parallelization***<br>
HOOMD-blue supports some parallelization options; unfortunately, it seems that our modifications currently break them. We have attempted to fix this but as of yet it is NOT possible to run these simulations in parallel and accurately track all particle interactions. All of our simulations MUST be run serially; therefore, large gelation simulations will take upwards of 1-2 months to run on the Discovery cluster. To do that, we must run the simulation in segments. Each gelation simulation is run for about 3 days, generating 11 frames of data, and then stopped. The next day the simulation can be restarted from frame 10 (giving us a potential comparison between frame 11 and frame 2 to verify that the simulation is continuing from where it left off without error). This process is repeated for the number of restarts needed to reach a quasi-steady state (typically somewhere between 9-13). Once all of the restarts are completed and the gel is confirmed to have 

You can output a variety of parameters depending on the simulation goal. Typically we output:
* A list of simulation configuration parameters
* A GSD file with particle position information
* A LOG file with Pressure_xy (negative shear stress) and temperature information
* Static colloid-colloid pair data from each timestep
	* Unique tags for each particle in the simulation
	* Unique tags for each bond formed between particles; however, these tags are NOT always retained accurately (a bug somewhere in the code causes these values to duplicate)
	* particle interaction (bond) lifetime (the number of timesteps 2 given particles have been in contact); if a bond breaks the lifetime resets to zero
	* virial stresses for each particle interaction
* A dynamic record of bond formation and breaking between timesteps (HistoryBin.csv)
* A record of the simulation progress (to verify there were no errors or other interruptions, and the simulation ran compeltely)
<br>

## [2] Checking Gelation

To check if a gelation simulation has reached a quasi-steady state (and formed a space spanning gel), plot the average coordination number \<Z> (AKA contact number, the number of other particles a given particle is interacting with) over time. At a quasi-steady state this number should be near constant, usually around \<Z> = 6 (octahedral structure) or sometimes \<Z> = 12 (close-packing: fcc or hcp) at very high volume fractions. The average coordination number will not reach a true plateau because there will always be some changes (i.e. "bond" breaking, "bond" formation, and lower Z values) at the gel surface, where free colloid particles behave more like a part of the Newtonian solvent. Instead it should reach a very gradual (near-plateau) slope, with minimal changes for several simulation times. You can also check the system by plotting the contact distribution (probability vs. contact number), which should produce a roughly Gaussian curve. Both of these checks are usually done in R.

Our past work found that small improvements in gelation do not affect the rheology, so if the average contact number appears more-or-less stable for 3 or more simulation restarts (~9 days of simulation time!) you can be pretty confident that gelation is completed and the system will not change significantly with more simulation time.

In addition to checking that the colloidal particles have formed a gel, you should check that the simulation has maintained equilibrium, i.e. average system temperature throughout the simulation should be constant, and the and the average pressure in the x-y direction (the negative shear stress) should be zero. See [Log Analysis with R](/05-Log-Analysis-with-R.md) for more details on making these checks.
<br>
<br>
## [3] Updating Lifetimes

After a gel has reached a quasi-steady state it is important to make sure that the lifetime data is correct. If a gel has been created in a single simulation, without restarts, then this step will not be necessary; howevere, since most of our gels are created in sequential simulation restarts on the Discovery cluster (where the lifetime of the system resets to zero at the start of each restart), you usually will need to update the lifetime data from one restart to the next. This is easiest to do in one step after all the restarts have been completed. This analysis is typically done in R.

If you are recording other timestep-dependent information (like a HistoryBin.csv file), those lifetimes will ALSO need to be updated.

There are several considerations to be made when updating the lifetimes:
1. Data from the last simulation restart may not be correctly numbered. 
	* In a simulation witout restarts, data is saved to a generic file (i.e. GelationData.csv). At the start of a restart, this data is copied to a labeled file (GelationData_After_Gelation_0.csv) to make room for the new data; therefore, there will usually be a file "missing" from the last restart (saved as GelationData.csv and not yet relabeled). If you want to use this data in your analysis you should copy it to a new file named correctly in sequence (for easy addition).
2. There is data from extra timesteps. We need to remove these.
	* Each gelation simulation runs for one frame longer than needed (so we have a comparison frame if we need to re-verify that the simulation has picked up where it left off); therefore we usually remove the data from this last frame. *NOTE: This number of frames may vary if the simulation was interrupted, so you should use Python and HOOMD-blue to check how many frames are in the GSD file from each restart before doing this step*
3. There are issues with the bond-labeleing step in our simulations, therefore you should always update bonds using the tags for the individual particles involved, not the bond-tag.
4. We only need to update the lifetimes of particle interactions that did not break between frames, and this needs to be done sequentially through all the frames of a restart.
<br>

## About Shearing Simulations

A shearing simulation starts from the final simulation restart of a gelation simulations (i.e. a quasi-steady state gel). You must load the entire gelation simulation ("type A" solvent particles AND "type B" colloid particles, typically saved as `all_particles.gsd`) to make sure that there are no non-physical overlaps between particles when the system is initialized.

Once initialized, the simulation applies a velocity equal to the shear rate at the upper and lower (+Y and -Y) boundaries of the simulation box, and the shear is then propogated through the gel via the interparticle interactions (DPD forces) using the Velocity-Verlet algorithm. This requires [the modifications we made to HOOMD-blue](/06-Modifying-HOOMDblue.md) to ensure that all particle interaction infomration is correctly tracked across all the periodic boundaries of the simulation box.

Although we do not "tilt" the simulation box to generate shear, HOOMD-blue (through the neighboring list calculation) is still built to interpret data as if the system is being tilted. We've turned off the part where the position gets updated with the box resize from tilting, BUT we keep the neighboring list calculation as is, so you will see the particle positions in VMD represented as if the simulation box has been "tilted". We also count the number of strains a system undergoes as conceptually equivalent to the number of times a box is fully tilted. We have verified that this visual tilting does not happen in the simulation (and you can verify it too!) because the *stresses* in the system are correct. Without the modifications to HOOMD-blue, the stresses have discontinuities from where the cross-boundary interactions reached a certain point and were lost, rather than being correctly updated across the boundary. Our simulation stresses do not have discontinuities, so we know that the particles are interacting correctly accross the boundaries of the simulation box. 

By tracking these particle interactions we get to track and detangle the contributions of kinetic energy (flow) and the virials (inter-particle interaction) on the overall bulk reponse of the material. At high volume fraction we know that the behavior is KE (flow) dominant, and at low volume fraction we know that the behavior is virial (interaction) dominant; but at intermediate states (where both are involved) we can begin to clarify what the componetns are.

A shearing simulation requires the same inputs as the gelation simulation, plus
* a shear rate 
* the number of strains, N_strains (usually N_strains = 1 for yielding behavior and N_strains = 10 to reach quasi-steady state)

Typically all other parameters will be kept the same between gelation and shearing simulations, but there may be times (for example, at very high shear rates) where you need to lower the DPD timestep (dt) to accomodate larger forces. This shouldn't physically change with shear rate, but practically the simulation becomes too noisy to effectively average between timesteps ] (i.e. lubrication forces get too large from velocity differences (shear rate), and you need more data (more particles) to balance that out and decrease the noise).
<br>

## [4] Running a Shearing Simulation

A shearing simulation follows the same DPD steps as a gelation simulation, with a modified run command to account for our changes to the `box_resize` function:
* Initialize the system from the quasi-steady state gel
* Initialize a neighboring list (the neighboring list method will vary with your choice of system; for our simulations we found that the tree method offers significant speed improvements over the cell method)
* Set the different particle types (i.e. "type A", "type B", etc.) with `hoomd.group.type()` 
* Use DPD (as set by `A`, `gamma`, and the cutoff-radius `r_cut`) to calculate the interactions between particles, and specify these parameters for the different sets of particle interactions (A-A, A-B, B-B, etc.)
* Choose what to happens after one timestep (i.e. standard integration or Velocity-Verlet integration `nve`) and set the time interval for this (dt = 0.01)
* Define the outputs (e.g. GSD, LOG, etc.)
* Run the system in a loop that accounts for our changes to the `box_resize` function

Typically we output the same files as from a gelation simulation, with the possible addition of isolated virial and kinetic energy values from each timestep.
<br>
<br>
## [5] Checking Shearing

To check if a shearing simulation has reached a quasi-steady state you should see how the system has evolved over time, plotting stress (the negative of pressure in the x-y direction) vs. strain, the velocity profile over time, the average coordination number (\<Z>) vs. strain, and the coordination number distribution vs. strain.

Here strain is the shear rate times time (where time is the number of timesteps times the DPD timestep, dt).

To reduce the noise from Brownian motion in the system, you should calculate local averages for sections of the system, rather than work with all the particles individually.

For the stress-strain curve, average the pressure for a subset of timesteps. For example, in a system with 10,000 colloidal particles that reached one strain (N_strains = 1) after 400,000 timesteps, you might want to average the pressure data for every 10,000 timesteps). A plot of the negative pressure (shear stress) vs. strain should then show yielding within the first strain time (N_strains = 1) and then eventually reach a constant (steady state) value (usually after ~N_strains = 10).

For the velocity profile, divide the system into a series of horizontal layers (slices of the y-plane) and average the information for all the particles in each of these layers. It is a good idea to have an odd number of layers, in case you need to check for simulation errors at the center of the simulation box. Then plotting velocity vs. y-position (now layer number) for all timesteps. This should lead to a linear profile (straight line sloping upwards) for Newtonian fluids, and a more S-like curve (curving convexly upwards from the base to the center, before curving concavely to the top of the box) for non-Newtonian colloidal systems.

Until the gel is broken up, the average coordination number should remain close to where it started, and the coordination number distribution should not vary significantly from the steady state gel. 
<br>
<br>
## [6]-[7] Updating Shear Lifetimes

Similar to the gelation simulation restarts in [step [3]](/07-Gelation-and-Shearing.md#3-updating-lifetimes), the shearing simulation starts from t=0, and any particle interaction lifetime information will need to be updated to account for the "bond" lifetimes that were present at start of the simulation (when the gel had reached a quasi-steady state). This process is roughly the same as updating the lifetimes across restarts, except the initial data comes from the quasi-steady state gel simulation data used to initialize the shearing simulation.

If the shearing simulation you are working with was long enough that it also needed to be run in restarts, then once you update the first restart of the shearing simulation you will need to use that data to update the lifetimes of the remaining restarts.
<br>
<br>
## Next Steps

This covers the basic outline of colloidal gel simulations! The rest is up to you and your research.

*HPC Computing:*
* See the remaining guides for information about [accessing](//08-Accessing-Discovery.md) Northeastern's HPC cluster, "Discovery," and [working with](/09-Slurm-and-Disco.md) HPC simulations.

*Background Reading:* For more background on DPD simulations of colloidal gel rheology, see the following papers
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


