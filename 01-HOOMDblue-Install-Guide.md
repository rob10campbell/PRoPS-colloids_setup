# HOOMD-blue Installation Guide

This is a guide to installing [HOOMD-blue] for use in the [PRoPS Group]'s colloid simulations. Our implementation of HOOMD-blue is currently CPU only (no GPU components). 

This guide is optizimed for MacOS.

[Last Update: August 2021]

The standard implementation of HOOMD-blue was adapted for our colloids simulations by Mohammad (Nabi) Nabizadeh. This guide was compiled by Rob Campbell.

[HOOMD-blue]: https://glotzerlab.engin.umich.edu/hoomd-blue
[PRoPS Group]: https://web.northeastern.edu/complexfluids/
<br>

## Prerequisites

Required for installation:
* MacOS or Linux (this guide is optimized for MacOS)
* C++11 capable compiler (HOOMD-blue is tested with gcc 4.8, 5.5, 6.4, 7, 8, 9, clang 5, 6, 7, 8)
* CMake >= 2.8.10.1
* Eigen >= 3.2
* Python >= 3.5
* pybind11 >= 2.2
* NumPy >= 1.7

Both clang and gcc should be included with Xcode on MacOS. MacOS also includes Python 2, but you will need to install Python 3 separately. Python 3 and the other prerequisites can be installed using [Homebrew](https://brew.sh/) or another package manager (NumPy and pybind11 are also easily installed for Python using pip, see note on virtual environments below). 

*Note: It is not recommended to install HOOMD-blue prerequisites with conda. See the* [HOOMD-blue](https://hoomd-blue.readthedocs.io/en/stable/installation.html) *installation page for advice on using conda.*
<br>
<br>
## Setting Up Source Repositories

If you do not already have a src folder or other location for repositories, it is recommended that you make one in your home directory.

Open Terminal. By default you should be in the home directory. You can check this by printing the current working directory with `pwd` (you should receive the following output where "your_username" is your computer login user name)
```bash
$ pwd
/Users/your_username
```
You can also review existing directories in the home directory with `ls`
```bash
$ ls
```
Make a new directory for your repositories
```bash
$ mkdir repositories
```
Then move to the repositories directory
```bash
$ cd repositories
```
And make a new directory for HOOMD-blue
```bash
$ mkdir HOOMDblue
```
<br>

## Creating a Python Virtual Environment

If you are running HOOMD-blue on an HPC cluster you will likely need to work in a virtual environment to keep any installed Python packages separate from other users. Virtual environments are also a good way to manage multiple Python installations on a dedicated workstation (i.e. switching between the default Python 2 that comes with MacOS and the Python 3 we will be using), and to ensure a clean development environment when starting a new project. There are multiple ways to implement virtual Python environments (pyenv, venv, virtualenvwrapper, etc.), but the simplest way (and the method used by HOOMD-blue's developers) is with `venv`.

*Note: After setting up the virtual environment you may need to reinstall NumPy and other packages to this environment using pip. This can be done before or after installing HOOMD-blue. This guide includes a reminder about this step after the HOOMD-blue installation.*

In the HOOMDblue directory, create a virtual Python environment to run your simulations. (You can call this virtual environment anything you like, but for simplicity we will call it VirtEnv)
```bash
$ mkdir VirtEnv
```

Before setting which version of Python you will use for the virtual environment, check your defaults:

Check your default version of Python (unless you changed your default version after installing Python 3, this will be the system version of Python 2)
```bash
$ python --version
Python 2.7.16
```
Check that you can specify Python 3 with `python3`
```bash
$ python3 --version
Python 3.9.6
```
Or by running python3 to see which version loads (you can then exit Python with the `quit()` command).
```bash
$ python3
Python 3.9.6 (default, Aug  4 2021, 22:40:34) 
[Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```

Now, without leaving the HOOMDblue directory, set VirtEnv to use Python 3 (this will create all the base directory files (bin, etc.) in the VirtEnv folder)
```bash
$ python3 -m venv VirtEnv/ --system-site-packages
```

And then source to the virtual environemnt to activate it
```bash
$ source VirtEnv/bin/activate
```

You are now working in the virtual environment! This will be reflected in the command prompt.
```bash
(VirtEnv) $
```

You should make sure that VirtEnv is using the correct version of Python:
```bash
(VirtEnv) $ python --version
Python 3.9.6
```

You can exit the virtual environment with the `deactivate` command, but stay in VirtEnv for the installation.
<br>
<br>
## Acquiring HOOMD-blue

We use the stable release of HOOMD-blue (v2.9.7), available with installation instructions [here](https://hoomd-blue.readthedocs.io/en/stable/installation.html). In our experience, cloning from Git leads to errors during the installation process. Therefore, it is recommended that you instead download the tar file and manually unzip it.

In a new Terminal window (i.e. NOT in VirtEnv), download the tar file
```bash
$ curl -O https://glotzerlab.engin.umich.edu/Downloads/hoomd/hoomd-v2.9.7.tar.gz
```

Once the file has downloaded you can close this Terminal window.

Go to the home directory in Finder.<br>
If you have not already added your home directory to the Finder sidebar it may be difficult to access. To fix this, open a new Finder window and select "Downloads" from the Favorites sidebar. Then, at the top of the Finder window, right click on the current folder name (Downloads) and select Users from the drop-down menu to move to the Users folder. You should see a folder with the same name as your computer login username. This is your home directory. Drag and drop that folder into the Favorites sidebar to create a shortcut to your home directory.

Open that folder, then open "repositories" and "HOOMDblue"

You should now see the tar file. Double click on the tar file to unzip it.

Leave the new, unzipped "hoomd-v2.9.7" folder there and drag and drop the tar file to the Trash.

You can now close Finder and go back to the Terminal window where you are using VirtEnv.
<br>
<br>
## Installing HOOMD-blue

You are now ready to install HOOMD-blue! These instructions are from the [HOOMD-blue installation guide for stable v2.9.7](https://hoomd-blue.readthedocs.io/en/stable/installation.html).

**Make sure that you are sourced to the virtual environment before installing.**

Move to the new hoomd-v2.9.7 folder
```bash
(VirtEnv) $ cd hoomd-v2.9.7
```
Make a build directory and move to it
```bash
(VirtEnv) $ mkdir build && cd build
```
Configure (ignoring the GPU requirements)<br>
*Note: This may give you a warning for developers. As long as there are no errors the configuration is successful and you can safely ignore the warning.*
```bash
(VirtEnv) $ cmake ../ -DCMAKE_INSTALL_PREFIX=`python3 -c "import site; print(site.getsitepackages()[0])"`
```
Compile
```bash
(VirtEnv) $ make -j4
```
And install HOOMD-blue into your Python environment
```bash
(VirtEnv) $ make install
```

HOOMD-blue is now installed in VirtEnv!
<br>
<br>

*Note: If prompted, you can install NumPy or other required Python packages with pip*
```bash
$ pip install NumPy
```
<br>

# Creating a Simulations Directory

You should now create a directory to house your future simulations in the HOOMDblue repository.

Exit the virtual environment
```bash
(VirtEnv) $ deactivate
```
Move back up to the HOOMDblue directory
```bash
$ cd ..
$ pwd
/Users/your_username/repositories/HOOMDblue
```
Make a new directory for simulations
```bash
$ mkdir sims
```
<br>

## Next Steps

You are now ready to use HOOMD-blue! See [Simulating waterDPD](/02-Simulating-waterDPD.md) for more information on running simulations and next steps.

