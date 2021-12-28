# Modifying HOOMD-blue 

This is a guide to installing the PRoPS group's modifications to HOOMD-blue for particle interaction tracking across Lees-Edwards boundary conditions in colloidal gels. These modifications will allow us to use attractive solid spheres, shear a system with Lees-Edwards boundary conditions, calculate particle interaction lifetimes, and output the decomposed stresses and shear stresses from a simulation.

Before modifying HOOMD-blue you must install the base version HOOMD-blue. See the [HOOMD-blue Installation Guide](/01-HOOMDblue-Install-Guide.md) for information on installing the base version of HOOMD-blue.<br>
**Note: It is recommended that you ALWAYS have two verions of HOOMD-blue installed on your computer, the base HOOMD-blue and a modified HOOMD-blue.**

[Last Update: December 2021]

The modifications to HOOMD-blue were developed by Mohammad (Nabi) Nabizadeh as part of his PhD thesis. This guide was compiled by Rob Campbell.
<br>
<br>
## Modification Background

Our simulations use periodic boundaries so that we can apply our results to the behavior of a larger physical system. Even though our simulation has a relatively small number of particles that would only make up one piece of a larger system, the periodic boundaries allow us to generalize how the particles will behave across a larger region of material with similar structure. 

Our emphasis on tracking particle interactions and colloidal structure is a bit at odds with HOOMD-blue's built-in shearing approach. HOOMD-blue was written to apply shear as a horizontal deformation (tilting) of the simulation box. In 2D this appears as the box first deforming from a square to a parallelogram, and then using this deformation to update the position of the particles. Unfortunately, this tilting process can cause particle interaction information to be lost when a particle crosses the simulation box boundary. The tilting process does not update the positions of particles that cross a periodic simulation box boundary in a way that retains interaction information from before crossing that boundary, effectively breaking all previous interactions at the boundary. 

We have made modifications to HOOMD-blue's C++ base code that allow us to fully track all particle interactions in a simulation. These interactions are calculated with Lees-Edwards boundary conditions for the simulation box boundary, and the effect of shear is calculated as part of the DPD particle interaction step using the Velocity-Verlet integration method (as described in [Boromand, Jamali, and Maia 2015](https://www.sciencedirect.com/science/article/abs/pii/S0010465515002076)).

To briefly summarize, the simulation box is surrounded by copies (images) in the X and Y directions. A shear rate is applied by moving the top and bottom images (+Y and -Y) at opposing velocities (+V and -V) with respect to the simulation box. This velocity is propogated through the simulation box by the dissipative force (i.e. friction) component of the DPD forces that define particle interactions. The effect of the dissipative force (and resulting changes to particle position and velocity) is implemented in the Velocity-Verlet algorithm, a 2-step integration that updates position and velocity of a particle based on the DPD forces. Particle position is completely updated in Step 1, but the velocity is only updated by about one-half timestep (the velocity is scaled by the parameter lambda, which we define as 0.5). This results in a second force calculation step (Step 2), where the forces are calculated again for the second one-half timestep. At the end of this process, one full timestep has occured, particle interactions (bonds) are formed or broken, and the calculation can begin again for the next timestep. This two-step process is an efficient way to smoothe particle motion in the simulation without significantly increasing simulation costs.
<br>
<br>
## Making Modifications

The modifications described above were developed by Mohammad (Nabi) Nabizadeh and are collected in the `Nabi_HOOMDblue-extensions` folder on Discovery. As mentioned above, these modifications allow us to simulate attractive solid spheres, shear a system with Lees-Edwards boundary conditions, calculate particle interaction lifetimes, and output the decomposed stresses and shear stresses from a simulation.

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

## Next Steps

You should now have [installed HOOMD-blue](/01-HOOMDblue-Install-Guide.md), run a [basic DPD simulation of water](/02-Simulating-waterDPD.md), [installed](/03-VMD-Install-Guide.md) and [worked with](/04-Using-VMD.md) VMD to visualize your simulation, [run basic checks on the simulation](/05-Log-Analysis-with-R.md) using R to verify it ran correctly, and modified a version of HOOMD-blue for more advanced simulations.

*Background Reading*<br>
If you haven't already, you should read the following papers:

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

*Running More Complex Simulations*

* See the overview on [gelation and shearing simulations](/07-Gelation-and-Shearing.md) for guidance on running more complex simulations.
