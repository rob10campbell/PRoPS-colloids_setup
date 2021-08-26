# Using VMD

This is a brief introduction to using [VMD] to visulaize the results of [HOOMD-blue] colloids simulations for research in the [PRoPS Group].

See [Simulating waterDPD](https://github.com/rob10campbell/PRoPS-colloids_setup/blob/main/03-Simulating-waterDPD.md) for more details on running a simulation with HOOMD-blue and the [VMD Installation Guide](https://github.com/rob10campbell/PRoPS-colloids_setup/blob/main/04-VMD-Install-Guide.md) for help installing VMD.

This guide is optimized for MacOS.

[Last Updated: August 2021].

The standard implementation of HOOMD-blue was adapted for our colloids simulations by Mohammad (Nabi) Nabizadeh. This guide was compiled by Rob Campbell.

[VMD]: https://www.ks.uiuc.edu/Research/vmd/
[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/
[PRoPS Group]: https://web.northeastern.edu/complexfluids/
<br>

## Opening a GSD file with VMD

As described at the end of [VMD Installation Guide](https://github.com/rob10campbell/PRoPS-colloids_setup/blob/main/04-VMD-Install-Guide.md), after installing the GSD Plugin you can open the GSD output of a HOOMD-blue simulation, such as `waterDPD.py`, with VMD.

Open VMD by selecting the icon in Launchpad or the VMD application in the Applications/VMD folder.

Go to VMD Main
* Choose "File"
* Choose "New Molecule"
* Click "Browse" next to "Filename" and navigate to the location of your GSD file<br>
(for the waterDPD example that should be `repositories/HOOMDblue/sims/water/Equilibrium.gsd`)
* The "Determine file type" settng should autofill with "HOOMD-blue GSD File"
* Click "Load"

You can close the Molecule File Browser and select the OpenGL Display window to view the visualization.
<br>
<br>
## Understanding the Default Visualization Setting

NAMD and VMD were designed to visualize biomolecular data, integrating molecular modeling of macromolecules with bioinformatics and molecular dynamics (think proteins, drug molecules, and other biomolecular interactions). 

The default vizualisation settings assume that you are viewing a protein or other macromolecule, and start by displaying the "bonds" between each particle (a network of lines).
<br>
<br>
## Overview of VMD Main

VMD Main is the window where you will make changes to the visualization settings, and the OpenDL Display window will reflect those changes.

VMD Main has 7 menus. Generally speaking you will use File, Graphics, and Display the most. The key features of each menu are:

File
* "New Molecule" and "Render"

Molecule
* Not used

Graphics
* "Representations..." and "Colors"

Display
* "Reset View," "Perspective," "Orthographic," "Light" 0-3, "Axes," "Rendermode," and "Display Settings..."

Mouse
* Not used

Extensions
* Rarely used, except possible "Tk Console"

Help
* Great set of help resources!
<br>

## 


