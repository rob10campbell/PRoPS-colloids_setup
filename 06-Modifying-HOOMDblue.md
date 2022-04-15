# Modifying HOOMD-blue 

This is a guide to installing the [PRoPS Group](https://web.northeastern.edu/complexfluids/)'s modifications to [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/)v2.9 for tracking the lifetime of DPD particle interactions across Lees-Edwards boundary conditions. These modifications will allow you to simulate the formation of space spanning networks (gels) from attractive solid spheres. You can also use these modifications to track the particle interactions during shearing of a colloidal gel and output the decomposed stresses of the system; however, there are some non-physical errors in the stresses that are not yet fully resolved.

This guide is optizimed for macOS. 

Before modifying HOOMD-blue you must install the base version HOOMD-blue. See the [HOOMD-blue Installation Guide](/01-HOOMDblue-Install-Guide.md) for information on installing the base version of HOOMD-blue.

**Note: It is recommended that you ALWAYS have two verions of HOOMD-blue installed on your computer, the base HOOMD-blue and a modified HOOMD-blue.**

[Last Update: January 2022]

The modifications to HOOMD-blue were developed by Mohammad (Nabi) Nabizadeh as part of his PhD thesis. This guide was compiled by Rob Campbell.
<br>

## Contents
1. [Why Make Modifications](/06-Modifying-HOOMDblue.md#why-make-modifications)
2. [What a Modified Simulation Does](/06-Modifying-HOOMDblue.md#what-a-modified-simulation-does)
3. [Installing Our Existing Modifications](/06-Modifying-HOOMDblue.md#installing-our-existing-modifications)
4. [Working with the Existing Modifications](/06-Modifying-HOOMDblue.md#working-with-the-existing-modifications)
5. [Next Steps](/06-Modifying-HOOMDblue.md#next-steps)

<br>

## Why Make Modifications

Our simulations use periodic boundaries so that we can apply our results to the behavior of a larger physical system. The particles at the edge of the simulation box interact with a duplicate image of the particles at the other side of the box. This allows particles to cross the boundary without leaving the system (re-entering the simulation box from the opposite side). These type of boundaries are common and easily implemented in HOOMD-blue, but the way that we want to use them is different from HOOMD-blue's defaults and has caused some problems, especially when shearing the system.

We want to apply shear to the simulation box by dragging the top and bottom images across the Y-axis boundaries at a velocity equal to the shear rate. HOOMD-blue was not written to apply shear this way, instead it controls shear by changing the physical shape of the simulation box (a horizontal deformation) to update particle positions. In 2D this appears as the box "tilting," deforming from a square to a parallelogram, for 1 strain. The positions in the "tilted" parallelogram box are then used to update the position of the particles that have crossed the simulation box boundaries. 

This is extremely efficient for calculating a particle's new position when cross a Y-axis boundary of the simulation box; however, we need to make some changes to this process to be able to track the interactions with particles that cross a boundary like this.

To achieve this, Nabi made modifications to HOOMD-blue's C++ base code. These modifications have not been updated for HOOMD-blue v3.0 and can not be run using MPI or other parallelized approaches, but they do effectively track all the particle interactions (formation and breaking of bonds, etc.).
<br>
<br>
## What a Modified Simulation Does

Our simulations use Lees-Edwards boundary conditions for the simulation box boundary. The effect of shear flow is propogated through the system by each particle interaction (calculated as part of the DPD particle interaction step using the Velocity-Verlet integration method, as described in [Boromand, Jamali, and Maia 2015](https://www.sciencedirect.com/science/article/abs/pii/S0010465515002076)).

This means that the simulation box is surrounded by copies (images) in the X and Y directions. A shear rate is applied by moving the top and bottom images (+Y and -Y) at opposing velocities (+V and -V) with respect to the simulation box. This velocity is propogated through the simulation box by the dissipative force (i.e. friction) component of the DPD forces that define particle interactions. 

The effect of the dissipative force (and resulting changes to particle position and velocity) is then implemented in the Velocity-Verlet algorithm, a 2-step integration implemented through modifications to the `TwoStepNVE.cc` file. This algorithm updates the position and velocity of a particle based on the DPD forces. In traditional CFD integration is performed as a single step (from timestep N to N+1). In the Velocity-Verlet 2-step integration particle position is completely updated in Step 1, but the velocity is only updated by about one-half timestep (the velocity is scaled by the parameter lambda, which we define as 0.5). This results in a second force calculation step (Step 2), where the forces are calculated again for the second one-half timestep (and position is unchanged).

At the end of both integration steps, one full timestep has occured, particle interactions (bonds) are formed or broken, and the calculation can begin again for the next timestep. This two-step process is an efficient way to smoothe particle motion in the simulation without significantly increasing simulation costs.
<br>
<br>
## Installing Our Existing Modifications

The modifications described above were developed by Mohammad (Nabi) Nabizadeh and are collected in the `Nabi_HOOMDblue_extensions` folder [on Discovery](/09-Slurm-and-Disco.md).

These file are written in C++. If you are new to C/C++, you will notice that there are `.cc` and `.h` files with the same names. A `.cc` file contains an implementation that is then called by the header (`.h`) file. Technically the `.cc` file is optional and everything can be included in the header, but the separation of a code into `.cc` and `.h` files is frequently considered best practice. You will need both the `.cc` and `.h` files to modify your version of HOOMD-blue.

**Note: It is recommended that you ALWAYS have two verions of HOOMD-blue installed on your computer, the base HOOMD-blue and a modified HOOMD-blue.**

To install the modifications:

You will need to copy two sets of modified files into two different folders in the version of HOOMD-blue that you are modifying. This can be easily done in either Terminal or Finder.*NOTE: Some of these files are new, some of them overwrite exisiting `.cc` and `.h` files*

* Go to the version of HOOMD-blue that you want to update (e.g. the `hoomd-v2.9.7/` directory).

* Copy all the files in the `Nabi_HOOMDblue-extensions/hoomd` directory into your version of HOOMD-blue's `hoomd` directory (e.g. `hoomd-v2.9.7/hoomd`).

* Inside your version of HOOMD-blue's `hoomd` directory you will also find the `md` directory. Copy all the files in the `Nabi_HOOMDblue-extensions/md` direcotry into your version of HOOMD-blue's `md` directory (e.g. `hoomd-v2.9.7/hoomd/md`).

After copying these files, you will need to recomple (make -j4) and reinstall (make install) HOOMD-blue. These steps are shown below, you can also revist them in the [HOOMD-blue Installation Guide](/01-HOOMDblue-Install-Guide.md#installing-hoomd-blue). <br>
*Note: You will likely receive several warnings about pybind11 during the compilation and installation steps; however, these warnings can safely be ignored (only worry about any errors!)*

To finish installing the modifications, use Terminal to go to the installation of HOOMD-blue that you just copied files to. Source to your virtual envrionment, then `cd` into the HOOMD-blue installation (e.g. the `hoomd-v2.9.7/` directory) and `cd` again into the `build` directory before compiling and installing the modified version of HOOMD-blue.

```bash
% pwd
/Users/your-username/repositories/HOOMDblue-mod/
% source VirtEnv/bin/activate
(VirtEnv) % cd hoomd-v2.9.7/
(VirtEnv) % cd build
(VirtEnv) % make -j4
(VirtEnv) % make install
```
<br>

## Working with the Existing Modifications

The modifications expect a **default code** written for a **specific type of system**. We assume that there are NO wall particles and NO charged particles (the only interactions are between A-A, A-B, and B-B particles types). If you need to add either of these features, then the modifications to HOOMD-blue will need to be updated, accordingly (mainly by adjusting the way aliases are called in the `PotentialPairDPDThermo.h` file)

The modifications were written so that the entire simulation is run from a **single** Python file. Unfortunately, due to some difficult-to-resolve errors with pybind11, several new classes used in the modified C++ code could not be saved as true C++ classes. Until this is resolved or the simulations are modified to run from 2 input files, the new (custom) DPD classes are given aliases. 

Most of these aliases are saved as interaction parameters for dummy particles (particles that otherwise do not exist, or do not interact, in our simulations). For example, the modifications may need to call the interaction potential, which we set in our Python code as `D0`. To make this value accessible from the C++ without defining a new C++ class, we save `D0` as a parameter in the `dpd.pair.coeff.set()` for a particle interaction that does not occur in our simulations. That interaction parameter (in this case, `A`) is then used as an alias for `D0` in HOOMD-blue's code.

Below is a full list of the aliases used to call different parameters:
* shear_Rate: called as the charge of particle zero (d_charge.data[0]) [This change is made in the C++ code only]
* start_lifetime_write_timestep (the start point for recording lifetimes): saved as the DPD parameter `gamma` for particle types C-D
* eta0: (the solvent AKA background viscosity): saved as the DPD parameter `A` for particle types A-W
* N_Wall (the number of wall particles): saved as the DPD parameter `gamma` for particle types A-W
* D0 (the attraction strength): saved as the DPD parameter `A` for particle types B-W
* alpha (AKA "a" or "kappa" the range of attraction, used with D0 in the Morse Potential calculation): saved as the DPD parameter `gamma` for particle types B-W
* r0 (the minimum inter-particle distance): saved as the DPD parameter `A` for particle types C-W
* LIFETIME_FileWrite_Period (the interval at which we record particle-interaction (bond) lifetimes): saved as the DPD parameter `gamma` for particle types C-W
* Write_Energy_Period_DPD (the interval at which to record the energy component of shear stress): saved as the DPD parameter `A` for particle types D-W
* Write_One_Time_Virial_Lifetime (the interval for recording the virial component of shear stress): saved as the DPD parameter `gamma` for particle types D-W
* Contact_Force (used to set colloid-colloid hard-sphere interactions): saved as the DPD parameter `A` for particle types W-W
* BDPeriod (the interval to record bond data): saved as the DPD parameter `gamma` for particle types W-W
<br>
<br>
If you would like to make additional modifications to the files (or make similar modification to another program), it may be useful to know what has been changed. You can see what the changes are by comparing the modified files with their original equivalents in HOOMD-blue v2.9. A basic outline of what has been changed is given below/

There are 15 files (5 that belong in the `hoomd/` directory and 10 that belong in the `hoomd/md/` direcotry). Line numbers correspond to the *modified* files:
* hoomd/
	* **`BoxResizeUpdater.cc`**: modify the box-wrapping (Line 105-106, 115120)
	* **`BoxResizeUpdater.h`**: no change (included for consistency)
	* **`ComputeThermo.cc`**: add `h_pos` and `d_charge` variables during thermo calculation (Line 211), add flags (Line 235), use slabbed positions (Line 238-259,281-314)
	* **`ComputeThermo.h`**: include `writeKE.h` and use it in the temperature calculation step (Line 69)
	* **`writeKE.h`**: a new file that creates the "KineticEnergy.csv" output (KE of each contact number (1-2) and for all solvents, as well as counters) 
* hoomd/md
	* **`BondDataCSV.h`**: a new file that creates the "BondData#.csv" file
	* **`EvaluatorPairDPDLJThermo.h`**: makes changes to notify you if our new flags are updated during `evalForceEnergyThermo()` (Line 181-183)
	* **`EvaluatorPairDPDThermo.h`**: makes changes to notify you if our new flags are updated during `evalForceEnergyThermo()` (Line 175-177), accounts for resolving particle overlaps (Line 205-229, 231-236, 238-240), adds colloid-colloid specific calculations (Line 242-259) lifetime calculations (Line 260-262) and hydrodynamics calculations (Line 263-304)
	* **`PotentialPairDPDThermo.h`**: includes all the new header files that have been created, initialized the lifetime parameters (Line 69-77), counts colloids and initialized a lifetime object (Line 103-121), adds `h_diameter` and `d_charge` to the force arrays (Line 181-182), sets contact number (Line 192-202), resets the virial and contact number list before looping (Line 203-245), initializes diameter and radisu (Line 265-266), sets boundary conditions and seed (Line 295-303), modifies `dx` for surface-surface calculations (Line 307-356), changes the force and potential energy calculations (Line 367-372), removes special potential pair requirements (Line 378-380), adds new parameters to `evalForceEnergyThermo()` (Line 387-388), changes the virial calculation (Line 393-442), and adds `writeSingleTimeTagList()` (Line 472-499)
	* **`TwoStepNVE.cc`**: adds `d_charge` and `Boxdims` (Line 89-91), initializes additional counters (Line 95-110), creates a new `MY_typej` for position calculations (Line 114-163), adds additional limits on particle movement for crossing boundaries (Line 193-219), and removes `getBoxdims` (Line 221)
	* **`TwoStepNVE.h`**: no change (included for consistency)
	* **`distanceModification.h`**: a new file for converting inter-particle distances to surface-surface measurements and resolving overlaps
	* **`forceContribution.h`**: a new file for creating the "IsolatedVirial.csv" file
	* **`lifeTime.h`**: a new file for creating output files related to inter-particle interaction lifetimes
	* **`writeVirials.h`**: a ew file for creating the "Virials.csv" file 
<br>

## Next Steps

You should now have [installed HOOMD-blue](/01-HOOMDblue-Install-Guide.md), run a [basic DPD simulation of water](/02-Simulating-waterDPD.md), [installed](/03-VMD-Install-Guide.md) and [worked with](/04-Using-VMD.md) VMD to visualize your simulation, [run basic checks on the simulation](/05-Log-Analysis-with-R.md) using R to verify it ran correctly, and modified a version of HOOMD-blue for more advanced simulations.

*Background Reading:* If you haven't already, you should read the following papers:

* Background on DPD
	* "[Viscosity measurement techniques in Dissipative Particle Dynamics]" (2015)
	* "[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation]" (1997)

* Background on more advanced simulations
	* "[Microstructural Rearrangements and their Rheological Implications in a Model Thixotropic Elastoviscoplastic Fluid]" (2017)
	* "[Time-rate-transformation framework for targeted assembly of short-range attractive colloidal suspensions]" (2020)
	* "[Life and death of colloidal bonds control the rate-dependent rheology of gels]" (2021)

[Viscosity measurement techniques in Dissipative Particle Dynamics]:https://doi.org/10.1016/j.cpc.2015.05.027
[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation]:https://doi.org/10.1063/1.474784
[Microstructural Rearrangements and their Rheological Implications in a Model Thixotropic Elastoviscoplastic Fluid]:https://doi.org/10.1103/PhysRevLett.118.048003
[Time-rate-transformation framework for targeted assembly of short-range attractive colloidal suspensions]:https://doi.org/10.1016/j.mtadv.2019.100026
[Life and death of colloidal bonds control the rate-dependent rheology of gels]:https://doi.org/10.1038/s41467-021-24416-x
<br>
*Running More Complex Simulations:*

* See the overview on [gelation and shearing simulations](/07-Gelation-and-Shearing.md) for guidance on running more complex simulations.
