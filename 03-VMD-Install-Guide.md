## VMD Installation Guide

This is a guide to installing the  Visual Molecular Dynamics ([VMD]) software, and associated plugins, for use with [HOOMD-blue] simulations of colloids in the [PRoPS Group].

This guide is for optimized for MacOS. 

[Last Update: August 2021]

The standard implementation of HOOMD-blue and it's associate visualizations were adapted for our colloids simulations by Mohammad (Nabi) Nabizadeh. This guide was compiled by Rob Campbell.

[VMD]: https://www.ks.uiuc.edu/Research/vmd/
[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/
[PRoPS Group]: https://web.northeastern.edu/complexfluids/
<br>

## Prerequisites

Required for installation:
* MacOS or Linux (this guide is optimized for MacOS)
* HOOMD-blue (see the [HOOMD-blue Installation Guide](/01-HOOMDblue-Install-Guide.md))
* A completed simulation (see [Simulating waterDPD](/02-Simulating-waterDPD.md))
<br>

## Acquiring VMD

VMD is freely available for download with a registered account.

Go to the [VMD website](https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD) and select the latest version appropriate for your operating system.<br>
*Note: There are two different MacOS versions, "ARM64" for computers with Apple silicon (i.e. the M1 chip) and "x86_84" for computers with Intel processors.*

You will be prompted to create a username and password to register with VMD. Register for 1 user.

Select and download the version appropriate for your operating system. For MacOS versions this will download a DMG file (e.g. `vmd194a51-macx86_64.dmg`) to your Downloads folder.
<br>
<br>
## Installing VMD

Open the DMG file. This will mount the DMG file as a virtual disk and open a new window with a VMD application (called something like `VMD 1.9.4a51-x86_64-Rev9`) and a PDF of the VMD User's Guide.

Open a new Finder window and go to Applications. In Applications, make a new folder called "VMD"<br>
*Note: In order to manually add a plugin to VMD, which we will do later, you must use this filename or the default filepath will be incorrect. This installation does not currently work for alternate filepaths.*

Copy and paste the VMD file and the user's guide from the DMG window into the Applications/VMD folder.

You can now close the DMG window and eject the virtual disk.

In the Applications/VMD folder, ctrl+click on the VMD file (hold down the `control` key and then click on the file) and select "Open" from the menu. This will open VMD with command overrides, so that you can run the program even though it was not installed through the Apple App Store. **You will get an error saying the software is not from a known provider** and the software will not open. Click Cancel.

Open System Preferences from either the Launchpad, the Applications folder, or the Dock. Go to "Security and Privacy" 

At the bottom of the Security and Privacy window you will see a message that VMD was prevented from opening. Click the "Open Anyway" button<br>
*Note: You may need to click the padlock at the bottom left of the screen and enter your username and password when prompted to unlock these settings before you can save these changes*

Clicking the "Open Anyway" button should immediately open VMD. VMD is now installed and authorized by your computer to open! And you should no longer need to ctrl-click to open VMD, you can open the application normally.
<br>
<br>
## The VMD Interface

VMD opens as 3 separate windows: a Terminal that launches the program with a `startup.command`, the OpenGL Display for viewing visualizations, and the control window called VMD Main. 

Keep the Terminal window open but ignore it, you should not need to interact with it while using VMD.

For now, quit VMD by going to the VMD Main window, selecting File, and then Quit. When prompted whether or not to Really Quit, click Yes. The OpenGL Display and VMD Main windows will both close and the `startup.command` Terminal window will display `[Process completed]` but remain open. You can now close this Terminal window.

*Note: You will probably get an error message from your compuer the first time you quit VMD (and occasionally other times after that) saying that VMD quit unexpectedly. This has to do with how VMD is opened and closed by the `startup.command` and is not a problem with VMD, but a slight incompatibility with how MacOS expects programs to work. You don't need to worry about it. Hit Ignore.*
<br>
<br>
## Prepare VMD for Manually Installing Plugins

We will be using VMD to open GSD files; however, GSD is a not one of the filetypes that VMD natively supports. We will need to manually install a plugin to allow VMD to open GSD files, and in order to do that we need to access the Contents inside the VMD application.

*Note: This step is unique to MacOS. Unfortunately, the plugin configuration process for manual installation is optimized for Linux, and cannot read the filepath to the VMD application's Contents on MacOS without the following modifications. If you are using Linux you should not need to do this.*

In a Finder window, go to Applications/VMD

Right-click (or two-finger click) on the VMD application and select "Show Package Contents" from the menu. This will open a new Finder window for the VMD application, revealing a single folder called "Contents"

Copy the Contents folder. Go back to the Applications/VMD folder, and paste the duplicate Contents folder alongside the VMD aplication and the user's guide.
<br>
<br>
## Acquiring the GSD Plugin

To acquire the GSD plugin, go to the [gsd-vmd Github page](https://github.com/mphowardlab/gsd-vmd), click the bright green "Code" button, and select "Download ZIP"

Open your Downloads folder in Finder and unzip the file. Leave it in the Downloads folder.
<br>
<br>
## Installing the GSD Plugin

The Contents folder contains a directory called "vmd" where we will configure the gsd-vmd plugin for installation.

Open a new Terminal window and move to the /Contents/vmd directory
*Note: There are at least two Applications folders on your computer, one in your home directory and one in your root directory. You do NOT want the Applications folder in your home directory (*`~/Applications/`*), you want the Applications folder in your root directory (*`/Applications/`, *where most applications are installed).*
```bash
$ cd ..
$ cd ..
$ cd Applications/VMD/Contents/vmd
```
Or, jump their directly with
```bash
$ cd /Applications/VMD/Contents/vmd
```
Copy the downloaded `gsd-vmd-main` folder to this directory with
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
$ cmake ..
```
And then install the plugin
```bash
$ make install
```
<br>
You can now run VMD (with the GSD plugin installed) from the duplicate Contents folder. To open this version of VMD, select the Unix executable file vmd_MACOSXX86_64 located in the Applications/VMD/Contents/vmd/ folder.

This is functional, but not ideal.
<br>
<br>
## Adding the GSD Plugin to the Original VMD Application

You now have two versions of VMD
1. The original download, without the GSD plugin
2. A copy with the GSD plugin installed, which requires navigating to a Unix executable file to open

If you want to open VMD from an application icon, rather than the Unix executable file, you can copy the new, configured GSD plugin to the original version of VMD.

Open a new Terminal window and move to the VMD application molfile directory (where plugins are stored)
```bash
$ cd /Applications/VMD/VMD\ 1.9.4a51-x86_64-Rev9.app/Contents/vmd/plugins/MACOSXX86_64/molfile/  
```
Copy the GSD plugin from where it was installed in the duplicate Contents folderto this molfile directory (where you are currently located)
```bash
$ cp /Applications/VMD/Contents/vmd/plugins/MACOSXX86_64/molfile/gsdplugin.so .
```

Your should now be able to open GSD files with the original VMD application! You can open the VMD application from the Applications/VMD folder or from Launchpad.<br>
***NOTE: Unfortunately you cannot keep VMD in the Dock.*** *Right-clicking on the icon and selecting "Keep in Dock" will work once, but after you close VMD the path will break and direct to the VMD icon file, not the VMD application. Bummer.*

Before you delete the duplicate Contents folder, the gsd-vmd-main folder in your Downloads, and the gsd-vmd-main.zip file you should test to make sure that you can open GSD files with VMD.
<br>
<br>
## Opening GSD Files with VMD

If you have not already done so, run the `waterDPD.py` example simulation, or another simulation that produces a GSD file (see [Simulating waterDPD](/02-Simulating-waterDPD.md) for details).

Open VMD by selecting the icon in Launchpad or the VMD application in the Applications/VMD folder.

Go to VMD Main
* Choose "File"
* Choose "New Molecule"
* Click "Browse" next to "Filename" and navigate to the location of your GSD file<br>
(for the waterDPD example that should be `repositories/HOOMDblue/sims/water/Equilibrium.gsd`)
* The "Determine file type" setting should autofill with "HOOMD-blue GSD File"
* Click "Load"

The GSD file should now open! 

You can close the Molecule File Browser and select the OpenGL Display window to view the default visualization setting (which displays "bonds" between your particles).
<br>
<br>
See the guide to [Using VMD](/05-Using-VMD.md) for an overview of visualization options. 

