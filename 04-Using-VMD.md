# Using VMD

This is a brief introduction to using [VMD] to visulaize the results of [HOOMD-blue] colloids simulations for research in the [PRoPS Group].

This guide is optimized for MacOS. See [Simulating waterDPD](/02-Simulating-waterDPD.md) for more details on running a simulation with HOOMD-blue and the [VMD Installation Guide](/03-VMD-Install-Guide.md) for help installing VMD.

[Last Updated: January 2022].

Our VMD workflow was developed by Mohammad (Nabi) Nabizadeh. This guide was compiled by Rob Campbell.

[VMD]: https://www.ks.uiuc.edu/Research/vmd/
[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/
[PRoPS Group]: https://web.northeastern.edu/complexfluids/

## Contents
1. [The VMD Interface](/04-Using-VMD.md#the-vmd-interface)
2. [Opening a GSD file with VMD](/04-Using-VMD.md#opening-a-gsd-file-with-vmd)
3. [Understanding the Default Visualization](/04-Using-VMD.md#understanding-the-default-visualization)
4. [Changing Lines to Spheres](/04-Using-VMD.md#changing-lines-to-spheres)
5. [Simulation Playback in **VMD Main**](/04-Using-VMD.md#simulation-playback-in-vmd-main)
6. [Rotation and Zoom](/04-Using-VMD.md#rotation-and-zoom)
7. [Modifying Visualization Graphics](/04-Using-VMD.md#modifying-visualization-graphics)
8. [Changing the Background Color](/04-Using-VMD.md#changing-the-background-color)
9. [Rendering an Image](/04-Using-VMD.md#rendering-and-image)
10. [More Visualization Display Settings](/04-Using-VMD.md#more-visualization-display-settings)
11. [Other Tools](/04-Using-VMD.md#other-tools)
12. [Some Recommended Visualization Styles](/04-Using-VMD.md#some-recommended-visualization-styles)
13. [Next Steps](/04-Using-VMD.md#next-steps)
<br>

## The VMD Interface

VMD opens as 3 separate windows: a Terminal window that launches and runs the program with a `startup.command`, the **OpenGL Display** window for viewing visualizations, and the control window called **VMD Main**.

You should keep the Terminal window open, but you do not need to interact with it. Closing the window will terminate the `startup.command` that runs VMD. If you need to use Terminal while using VMD you should open a new window for that, and it is recommended to minimize the VMD `startup.command` window so you do not accidentally enter commands there and interupt the program.

**VMD Main** is the window where you will make changes to the visualization and access additional settings. The **OpenGL Display** window displays the files you have open using the settings chosen via **VMD Main**.
<br>
<br>
## Opening a GSD file with VMD

As described at the end of the [VMD Installation Guide](/03-VMD-Install-Guide.md), after installing the GSD Plugin you can open the GSD output of a HOOMD-blue simulation (such as the `Equilibrium.gsd` file produced by `waterDPD.py`) with VMD.

Open VMD by selecting the icon in Launchpad or the VMD application in the Applications/VMD folder.

Go to **VMD Main**
* Select the "File" menu
* Choose "New Molecule"
* In the **Molecule File Browser** window, click the "Browse..." button next to "Filename:" and navigate to the location of your GSD file<br>
(for the waterDPD example that should be `repositories/HOOMDblue/sims/water/Equilibrium.gsd`)
* The "Determine file type" settng should autofill with "HOOMD-blue GSD File"
* Click the "Load" button

You can close the **Molecule File Browser** and view your file in the **OpenGL Display** window.
<br>
<br>
## Understanding the Default Visualization

NAMD and VMD were designed to visualize biomolecular data, integrating molecular modeling, bioinformatics and molecular dynamics (think proteins, drug molecules, ther macromolecules and biomolecular interactions). 

The default vizualisation settings assume that you are viewing a protein or other macromolecule, and start by displaying the "bonds" between each particle. For the `Equilibrium.gsd` file, this displays a cube-shaped network of lines.
<br>
<br>
## Changing Lines to Spheres

To change the visualization settings to better match our simulation, go to **VMD Main** and open the "Graphics" menu and select "Representations..."

At the bottom of the **Graphical Representations** window is a tab called "Draw style" where you will see the option "Drawing Method" is set to "Lines"

To change the "Drawing Method" to spheres, choose "VDW" from the "Drawing Method" dropdown menu.

The change should take place automatically, but you can also apply changes with the "Apply" button at the bottom of the window.

*Note: For large simulations (with large numbers of particles) the "VDW" representation will be quite slow. It is important to check the simulation in "VDW" to make sure that there are no non-physical overlaps between particles; however, once you've checked that you can switch to "Points" for faster rendering if desired.*

You can leave the **Graphical Representations** window open, since we will come back to it soon.
<br>
<br>
## Simulation Playback in **VMD Main**

Now that we have changed the "Graphics" settings to display spheres instead of lines you can explore the visualization

On the bottom of **VMD Main** there are playback controls for the simulation. You can click the arrow (>) on the bottom right to start playing the simulation forward in time, or click the opposite arrow (<) at the bottom left to play the simulation backward in time. Click the same arrow again to pause playback. 

The (|>) and (<|) arrow buttons step forwards and backwords one timestep.

The "zoom" checkbox increases playback speed. You can also change the speed with the "speed" slider, increase or decrease the "step" size between each frame, and choose between playing the simulation "Once," starting an endless "Loop," or "Rock" back and forth (where after playing in one direction the simulation reverses, and continues like that in a loop).
<br>
<br>
## Rotation and Zoom

In the **OpenGL Display** you can hold-click and press the R key to enter rotation mode (locking the movement of your mouse/trackpad to rotating the visualization). Click again to exit rotation mode.

You can also hold-click and press the S key to enter zoom mode (locking the movement of your mouse/trackpad to zooming in and out on the visualization). Click again to exit zoom mode.

There are a number of other keyboard shortcuts that you can explore with VMD's documentation. If you get trapped in a viewing mode at any time, you can go back to **VMD Main** and go to the "Display" menu to select "Reset View."
<br>
<br>
## Modifying Visualization Graphics

Back in the **Graphical Representations** window there are several other changes you can make in the "Draw style" tab:

To change the size and shape of the spheres, adjust "Sphere Scale" and "Sphere Resolution" (use (<<) and (>>) for large jumps, and (<) and (>) for smaller changes).

Change the color of your particles with the "Coloring Method" dropdown menu. 
* For example, if your file includes velocity outputs you can color code the particles accordingly by going to "Trajectory" and choosing "Velocity" (for `Equilibrium.gsd` there is no velocity output, so all the particles will be white, signifying 0 velocity). 
* You can also go to "Position" and choose "X" to have the particles in `Equilibrium.gsd` at -5 rendered blue, while the particles at +5 are rendered red. 
* To select a uniform color for your particles, choose "ColorID" and a new dropdown menu with numbers will appear. When you open it you will see VMD's numbered color options.
* Later we will program VMD to render color based on other outputs as well, such as stress.

Use the "Material" dropdown menu to change the quality of the rendering. For example, sometimes you want to show the water molecules in your simulation, but youdon't want them to distract from the colloidal particles. To highlight the colloidal materials you can change the water molecule "Material" to "Glass1" and the colloidal particle "Material" to "AOChalky" (we will cover more on how to render different particles from a simulation with different settings later on).
<br>
<br>
## Changing the Background Color

The default background color is black, but many of our simulations show up better on white. To change the background color go to **VMD Main** and open the "Graphics" menu and choose "Colors..."

In the **Color Controls** window go to the "Categories" list and select "Display," then go to the "Names" list and select "Background," and the "Colors" list and select "8 white"

If you like, you can change the default color for a given setting by clicking the "Default" button at the bottom of the screen after making your selection.
<br>
<br>
## Rendering an Image

Rendering your visualization allows you to save a snapshot of it. For a test rendering, go to the **Graphical Representations** window and set the "Coloring Method" to "ColorID" (any color of your choice) and the "Material" to "AOChalky" (you can also adjust the "Sphere Scale" and "Sphere Resolution" to your liking)

Go to the **OpenGL Display** window and adjust the visualization to your favorite angle and zoom level

Now go to **VMD Main** and open the "File" menu and select "Render"

In the **File Render Controls** window go to the "Render the current scene using:" dropdown menu and select "Tachyon (internal, in-memory rendering)"

Any filename is fine. Click "Start Rendering"

When the rendering is finished it will automatically open your new file with the Preview application. And voila! You have created a visualization of your work with VMD!

If you zoom in on the image in Preview you will see that the base settings produce a fairly low-resolution image (it becomes pixelated quite quickly when you zoom in); however, you can adjust the settings in VMD to render really high-resolution images that control for every particle and every attribute, and you can also export very smooth movies that show clustering, stress measurement, other properties, etc. It's a really versatile rendering tool!

The default file type is TGA (a raster graphics file format). You can save or export to other filetypes from Preview.

If you did not change the default destination your file will have saved to your home folder. <br>
***Note: Re-rendering a file with the same name will overwrite an existing file without warning.***

VMD is best at rendering a single image, rather than exporting video, so generally speaking the best way to make a high-quality video of a VMD visualization is to save each frame as an image and then assemble the animation with QuickTime Player's built-in "Open Image Sequence" option.

**Pro Tip**: Whenever you're working on something in VMD and get a view that seems visually pleasing, render it and save it! Just in case. Visualizations are extremely useful for presentations and papers, but they can be time consuming to recreate. Better to have something ready to show off, just in case you need it.
<br>
<br>
## More Visualization Display Settings

There are a number of other useful changes you can make from **VMD Main** in the "Display" menu:
* Change the viewing angle between "Perspective" and "Orthographic" *NOTE: you will want to use the Orthographic viewing angle most of the time*
* Adjust the lighting angle by turing on/off "Light 0" "Light 1" "Light 2" and "Light 3"
* Change the location of the axes, or turn them off, in the "Axes" menu
* Switch the "Rendermode" to "GLSL" for higher resolution images (try it with the "Sphere Scale" set back to "1.0" in the **Graphical Representations** window)

Selecting "Display Settings" will open the **Display Settings** window for additional options to control lighting effects:
* Change "Cue Mode" to "Linear" and then lower the "Cue End" value to decrease contrast on the edge of the image and highlight the center (similar to "Vignette" on Instagram)
* Change the "Ray Tracing Options" - turn on "Shadows," "Amb. Occl." (Ambient Occlusion), and "DoF" (Depth of Field)
<br>

## Other Tools

There are many useful Extensions available for VMD, but none are particularly necessary for our work. Generally it's easier (and more flexible) for us to add specific functions with a MATLAB or Python script.

One useful feature in the **VMD Main** "Extensions" menu is the "Tk Console" which allows you to program directly into VMD with the **VMD TkConsole** window. The syntax is very different from the command line, so it is difficult to get started using, but you won't need to use it very much and it's there if you need it! There is excellent documentation (and tutorials) for the Tk Console in the VMD community if you need it.

In general the VMD community is quite large, so there are a lot of resources available if you need help.
<br>
<br>
## Some Recommended Visualization Styles

Some recommended visualizations for colloid particles are:
* Set the "Coloring Method" to "Velocity" to visualize shear flow
* Use the "Periodic" tab in the **Graphical Representations** window to add 1 or 2 copies of the simulation box in the "+X" and "-X" direction to visualize flow 
* Adust visualization settings in the "Z" axis and modify the lighting position to more accurately reprensent the volume fraction of a sample (i.e. add depth to the image). Set the coloring method to "Position/Z" and adjust the opacity and/or brightness of the particles along this axis. 
	* After selecting "Position/Z" for coloring method, go back to the **VMD Main** window and the "Graphics" drop down menu. Select "Colors" to open the **Color Controls** window, and switch to the "Color Scale" tab. In the "Method" drop down menu select "BlkW" to have the particle fade to black as they go deeper into the Z-plane.
<br>

## Next Steps

See the guide to [log analysis in R](/05-Log-Analysis-with-R.md) for an introduction to other ways to analyze a completed simulation.
