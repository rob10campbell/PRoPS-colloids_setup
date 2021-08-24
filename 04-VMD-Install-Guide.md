## VMD Installation Guide

This is a guide to installing the  Visual Molecular Dynamics ([VMD]) software, and associate plugins, for use with [HOOMD-blue] simulations of colloids in the [PRoPS Group].

This guide is for optimized for MacOS. 

[Last Update: August 2021]

The standard implementation of HOOMD-blue was adapted for our colloids simulations by Mohammad (Nabi) Nabizadeh. This guide was compiled by Rob Campbell.

[VMD]: https://www.ks.uiuc.edu/Research/vmd/
[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/
[PRoPS Group]: https://web.northeastern.edu/complexfluids/
<br>

## Prerequisites

Required for installation:
* MacOS or Linux (this guide is optimized for MacOS)
* HOOMD-blue (see HOOMD-blue Installation Guide)
* A completed simulation (see Simulating waterDPD)
<br>

## Acquiring VMD

VMD is freely available for download with a registered account.

Go to the [VMD website](https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD) and select the latest version appropriate for your operating system.<br>
*Note: There are two different MacOS versions, "11.x, ARM64" for computers with Apple silicon (i.e. the M1 chip), and "10.15, x86_84" for computers with Intel processors.*

You will be prompted to create a username and password to register with VMD. Register for 1 user.

Select and download the version appropriate for your operating system (for MacOS versions this will download a DMG file (e.g. `vmd194a51-macx86_64.dmg`) to your Downloads folder).

Open the DMG file. This will mount the DMG file as a virtual disk and open a new window with a VMD file (called something like `VMD 1.9.4a51-x86_64-Rev9`) and a PDF of the VMD User's Guide.

Open a new Finder window and go to Applications.

In Applications, make a new folder called "VMD"<br>
*Note: In order to manually add a plugin to VMD, which we will do later, you must use this filename or the default filepath will be incorrect. This installation does not currently work for alternate filepaths.*

Copy and paste the VMD file and the user's guide from the DMG folder into the Applications/VMD folder.<br>
You can now close the DMG window and eject the virtual disk.

In the Applications/VMD folder, ctrl+click on the VMD file (hold down the `control` key and then click on the file) and select "Open" from the menu. This will open VMD with command overrides, so that you can run the program even though it was not installed through the Apple App Store.<br>
**You will get an error saying the software is not from a known provider** and the software will not open. Click Cancel.

Open System Preferences from either the Launchpad, the Applications folder, or the Dock. Go to "Security and Privacy" 

At the bottom of the Security and Privacy window you will see a message that VMD was prevented from opening. Click the "Open Anyway" button<br>
*Note: You may need to click the padlock at the bottom left of the screen and enter your username and password when prompted to unlock these settings and save these changes*

Clicking the "Open Anyway" button should immediately open VMD. VMD is now installed and authorized by your computer to open! And you should be able to open VMD normally from the Applications/VMD folder from this point on.

VMD opens as 3 separate windows: a Terminal that launches the program with a `startup.command`, the OpenGL Display for viewing visualizations, and VMD Main. VMD Main is where most of the controls are. 

For now quit VMD by going to the VMD Main window, selecting File, and then Quit.
When prompted whether or not to Really Quit, click Yes.<br>
The OpenGL Display and VMD Main windows will both close and the `startup.command` Terminal window will say `[Process completed]` but remain open. You can close this Terminal window.

*Note: You will probably get an error message from your compuer the first time you quit VMD (and occasionally other times after that) saying that VMD quit unexpectedly. This is has to do with how VMD is opened and closed by the `startup.command` and is not a problem with VMD, but a slight incompatibility with how MacOS expects programs to work. You don't need to worry about it. Hit Ignore.*
<br>
<br>
## Prepare VMD for Manually Installing Plugins

We will be using VMD to open GSD files; however, GSD is a not one of the filetypes that VMD natively supports. We will need to manually install a plugin to allow VMD to open GSD files, and in order to do that we need to access the Contents of the VMD file.

In a Finder window, go to Applications/VMD

Right-click (or two-finger click) on the VMD file and select "Show Package Contents" from the menu. This will open a new Finder window of the VMD file, revealing a single folder called "Contents"

Copy the Contents folder, go back to the Applications/VMD folder, and paste the Contents folder alongside the VMD file and the user's guide.

*Note: It would be much easier to install the plugin directly to the original Contents folder in the VMD file, unfortunately the plugin configuration process for manual installation can not read the original directory's file path. This an issue unique to MacOS, and that is why we do this step.*

Inside the Contents folder is a directory called vmd. Open a new Terminal window and navigate to the vmd directory inside the new Contents folder.<br>
*Note: You need to leave your home directory and go to the main Applications folder. You do NOT want the Applications folder in your home directory, you want the Applications folder in your root directory.*
```bash
$ cd ..
$ cd ..
$ cd Applications/VMD/Contents/vmd
```
or
```bash
$ cd /Applications/VMD/Contents/vmd
```
<br>

## Installing the GSD Plugin

To install the GSD plugin, go to the [gsd-vmd Github page](https://github.com/mphowardlab/gsd-vmd), click the bright green "Code" button and select "Download ZIP"

Open your Downloads folder in Finder and unzip the file. Leave it in the Downloads folder.

Go back to the Terminal window (in Applications/VMD/Contents/vmd) and copy the new folder there with
```bash
$ cp -r ~/Downloads/gsd-vmd-main .
```

Move to the new folder
```bash
$ cd gsd-vdm-main
```
Make a build directory and move to it
```bash
$ mkdir build && cd build
```
Run cmake to configure the plugin
```bash
cmake ..
```
And then install the plugin
```bash
$ make install
```

You can now run vmd and access the GSD plugin from the version in the duplicate Contents folder by opening the Unix executable file `vmd_MACOSXX86_64` at Applications/VMD/Contents/vmd/vmd_MACOSXX86_64

This is functional, but not ideal.

## Merging the Duplicate VMD Versions

You now have two versions of VMD
1. The original download, without the GSD plugin
2. A version with the GSD plugin that requires navigating to a Unix executable file to open

If you want to get rid of the duplicate and keep the original, you can copy the new, configured GSD plugin to the original version of VMD. This will also allow you to open VMD with the GSD plugin enabled from the VMD file icon.

Open a new Terminal window and move to the VMD application molfile directory where plugins are stored
```bash
$ cd /Applications/VMD/VMD\ 1.9.4a51-x86_64-Rev9.app/Contents/vmd/plugins/MACOSXX86_64/molfile/  
```
Copy the GSD plugin from the duplicate Contents folder's molfile directory (where it was configured) to the original Contents folder's molfile directory (where you are currently located)
```bash
$ cp /Applications/VMD/Contents/vmd/plugins/MACOSXX86_64/molfile/gsdplugin.so .
```

Your original version of VMD should now have the GSD plugin needed to open GSD files! You can open VMD from Applications/VMD or Launchpad by selecting the VMD application icon.
***NOTE: Unfortunately you cannot keep VMD in the Dock.*** *Right-clicking on the icon and selecting "Keep in Dock" will appear to work, but after you close VMD the path will break and only direct to the VMD icon, not the VMD application.*

Before you delete the duplicate Contents folder, make sure that you can open a GSD file in the original version of the application:<br>
* If you have not already done so, run the `waterDPD.py` example simulation, or another simulation that produces a GSD file (see Simulating waterDPD for details)
* Open VMD by selecting the icon in Launchpad or the VMD file in Applications/VMD
* Go to VMD Main
* Choose "File"
* Choose "New Molecule"
* Click "Browse" next to "Filename" and navigate to the location of your GSD file (for the waterDPD example that should be `repositories/HOOMDblue/sims/water/Equilibrium.gsd`)
* The "Determine file type" setting should have autofilled with "HOOMD-blue GSD File" and you can click "Load"

The GSD file should now open! You can close the Molecule File Browser and select the OpenGL Display to view the default visualization of "bonds" between your particles.
<br>
<br>
See the guide to Using VMD for an overview of simple visualization techniques. 

