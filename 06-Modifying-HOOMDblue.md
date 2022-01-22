# Modifying HOOMD-blue 

This is a guide to installing the [PRoPS Group](https://web.northeastern.edu/complexfluids/)'s modifications to [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/) for improved particle interaction tracking across Lees-Edwards boundary conditions in colloidal gels. These modifications will allow you to simulate attractive solid spheres, shear a system with Lees-Edwards boundary conditions, calculate particle interaction lifetimes, and output the decomposed stresses and shear stresses from a simulation.

This guide is optizimed for MacOS.

Before modifying HOOMD-blue you must install the base version HOOMD-blue. See the [HOOMD-blue Installation Guide](/01-HOOMDblue-Install-Guide.md) for information on installing the base version of HOOMD-blue.

**Note: It is recommended that you ALWAYS have two verions of HOOMD-blue installed on your computer, the base HOOMD-blue and a modified HOOMD-blue.**

[Last Update: January 2022]

The modifications to HOOMD-blue were developed by Mohammad (Nabi) Nabizadeh as part of his PhD thesis. This guide was compiled by Rob Campbell.
<br>

## Contents
1. [Why Make Modifications](/06-Modifying-HOOMDblue.md#why-make-modifications)
2. [Installing Our Existing Modifications](/06-Modifying-HOOMDblue.md#installing-our-existing-modifications)
3. [Modifying The Existing Modifications](/06-Modifying-HOOMDblue.md#modifying-the-existing-modifications)
4. [Next Steps](/06-Modifying-HOOMDblue.md#next-steps)

<br>

## Why Make Modifications

Our simulations use periodic boundaries so that we can apply our results to the behavior of a larger physical system. Even though our simulation has a relatively small number of particles that would only make up one piece of a larger system, the periodic boundaries allow us to generalize how the particles will behave across a larger region of material with similar structure. 

Our emphasis on tracking particle interactions and colloidal structure is a bit at odds with HOOMD-blue's built-in shearing approach. HOOMD-blue was written to apply shear as a horizontal deformation (tilting) of the simulation box. In 2D this appears as the box first deforming from a square to a parallelogram, and then using this deformation to update the position of the particles. Unfortunately, this tilting process can cause particle interaction information to be lost when a particle crosses the simulation box boundary. The tilting process does not update the positions of particles that cross a periodic simulation box boundary in a way that retains interaction information from before crossing that boundary, effectively breaking all previous interactions at the boundary. 

We have made modifications to HOOMD-blue's C++ base code that allow us to fully track all particle interactions in a simulation. These interactions are calculated with Lees-Edwards boundary conditions for the simulation box boundary, and the effect of shear is calculated as part of the DPD particle interaction step using the Velocity-Verlet integration method (as described in [Boromand, Jamali, and Maia 2015](https://www.sciencedirect.com/science/article/abs/pii/S0010465515002076)).

To briefly summarize, the simulation box is surrounded by copies (images) in the X and Y directions. A shear rate is applied by moving the top and bottom images (+Y and -Y) at opposing velocities (+V and -V) with respect to the simulation box. This velocity is propogated through the simulation box by the dissipative force (i.e. friction) component of the DPD forces that define particle interactions. The effect of the dissipative force (and resulting changes to particle position and velocity) is implemented in the Velocity-Verlet algorithm, a 2-step integration implemented through modifications to the `TwoStepNVE.cc` file. This algorithm updates the position and velocity of a particle based on the DPD forces. In traditional CFD integration is performed as a single step (from timestep N to N+1). In the Velocity-Verlet 2-step integration particle position is completely updated in Step 1, but the velocity is only updated by about one-half timestep (the velocity is scaled by the parameter lambda, which we define as 0.5). This results in a second force calculation step (Step 2), where the forces are calculated again for the second one-half timestep (and position is unchanged). At the end of both integration steps, one full timestep has occured, particle interactions (bonds) are formed or broken, and the calculation can begin again for the next timestep. This two-step process is an efficient way to smoothe particle motion in the simulation without significantly increasing simulation costs.
<br>
<br>
## Installing Our Existing Modifications

The modifications described above were developed by Mohammad (Nabi) Nabizadeh and are collected in the `Nabi_HOOMDblue_extensions` folder [on Discovery](/09-Slurm-and-Disco.md). As mentioned above, these modifications allow us to simulate attractive solid spheres, shear a system with Lees-Edwards boundary conditions, calculate particle interaction lifetimes, and output the decomposed stresses and shear stresses from a simulation.

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

## Modifying The Existing Modifications

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
