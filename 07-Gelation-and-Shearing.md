# Gelation and Shearing of Colloidal Particles

Overview of gelation and shearing.

This is an overview of the workflows for gelation and shearing simulations of colloidal particles with [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/) for research in the [PRoPS Group](https://web.northeastern.edu/complexfluids/).

This guide is optizimed for MacOS. Before running gelation or shearing simulations you should have already [installed HOOMD-blue](/01-HOOMDblue-Install-Guide.md), run a [basic DPD simulation of water](/02-Simulating-waterDPD.md), [installed](/03-VMD-Install-Guide.md) and [worked with](/04-Using-VMD.md) VMD to visualize your simulation, [run basic checks on the simulation](/05-Log-Analysis-with-R.md) using R to verify it ran correctly, and [modified a version of HOOMD-blue](/06-Modifying-HOOMDblue.md) for more advanced simulations.

[Last Update: December 2021]

These workflows were developed by Mohammad (Nabi) Nabizadeh. This guide was compiled by Rob Campbell.
<br>

## Background on Gelation and Shearing Simulations

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
