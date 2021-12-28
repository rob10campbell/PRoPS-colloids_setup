# Gelation and Shearing of Colloidal Particles

This is an overview of the workflows for running gelation and shearing simulations of colloidal particles with [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/) for research in the [PRoPS Group](https://web.northeastern.edu/complexfluids/).

This guide is optizimed for MacOS. Before running gelation or shearing simulations you should have already [installed HOOMD-blue](/01-HOOMDblue-Install-Guide.md), run a [basic DPD simulation of water](/02-Simulating-waterDPD.md), [installed](/03-VMD-Install-Guide.md) and [worked with](/04-Using-VMD.md) VMD to visualize your simulation, [run basic checks on the simulation](/05-Log-Analysis-with-R.md) using R to verify it ran correctly, and [modified a version of HOOMD-blue](/06-Modifying-HOOMDblue.md) for more advanced simulations.

[Last Update: December 2021]

These workflows were developed by Mohammad (Nabi) Nabizadeh. This guide was compiled by Rob Campbell.
<br>

## Background on Gelation and Shearing Simulations

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

[3] \(IF gelation was run in segments) Combine the data from all the gelation simulation restarts and update the particle interaction lifetimes across all gelation simulation restarts

[4] Shear the gel from quasi-steady state (with a Python script using HOOMD-blue)

[5] Check that the sheared gel has reached a new quasi-steady state

[6] \(IF gelation was run in segments) Use the updated lifetimes from step [3] to update the particle interaction lifetimes in the shearing simulation

[7] \(IF shearing was run in segments) Use the updated lifetimes from step [6] to update the particle interaction lifetimes in the remaining shearing simulation restarts
<br>

## Gelation

About gelation simulations.

## Shearing

About shearing simulations.
