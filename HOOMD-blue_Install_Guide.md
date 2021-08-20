# HOOMD-blue Installation Guide

This is a guide to installing [HOOMD-blue] for use in the PRoPS Group's colloid simulations. Our implementation of HOOMD-blue is currently CPU only (no GPU components). 

This guide is optizimed for MacOS and was last updated in August 2021.

Our implementation of HOOMD-blue for colloids simulations was developed by Mohammad (Nabi) Nabizadeh and this guide was compiled by Rob Campbell.

[HOOMD-blue]: https://glotzerlab.engin.umich.edu/hoomd-blue

## Prerequisites

Required for installation
* MacOS or Linux (this guide is optimized for MacOS)
* C++11 capable compiler (tested with gcc 4.8, 5.5, 6.4, 7, 8, 9, clang 5, 6, 7, 8)
* CMake >= 2.8.10.1
* Eigen >= 3.2
* Python >= 3.5
* NumPy >= 1.7
* pybind11 >= 2.2

Both clang and gcc should be included in Xcode on MacOS. MacOS also includes Python 2, but you will need to install Python 3 separately. Python 3 and the other prerequisites can be installed using [Homebrew](https://brew.sh/) or another package manager (NumPy and pybind are also easily installed for Python using pip, see instructions on virtual environments below). Using conda is possible, but not recommended. See the [HOOMD-blue](https://hoomd-blue.readthedocs.io/en/stable/installation.html) installation page for advice on using conda.

## Setting Up Source Repositories

If you do not already have a src folder or other location for repositories:

* Open Terminal
* By default you should be in the home directory. You can check this printing the working directory with pwd, and you should receive the following output
```bash
$ pwd
/Users/your_username
```
* Make a new directory for your repositories
```bash
$ mkdir repositories
```

Make a new directory for your HOOMDblue simulations:

* Move to the repositories directory
```bash
$ cd repositories
```
* Make a new directory for HOOMD-blue
```bash
$ mkdir HOOMDblue
```

## Creating a Python Virtual Environment

If you are running HOOMD-blue on an HPC cluster you will likely need to work in a virtual environment to keep any installed python packages separate from other users installations. Virtual environments are also a good way to manage multiple Python installations on a dedicated workstation (in the case of the default Python 2 that comes with MacOS and Python 3, which we will be using), and to maintain a clean development environment for different projects. There are multiple ways to implement virtual python environments (pyenv, venv, virtualenvwrapper, etc.), but the simplest way (and othe only method tested by HOOMD-blue developers) is with venv.

Note: You may need to reinstall NumPy and other packages for each virtual environment using pip (instructions for that are included in this guide).

* In the HOOMDblue directory, create a virtual python environment to run your simulations
```bash
$ mkdir VirtEnv
```

Before setting which version of python you will use for the virtual environment, check your defaults:

* Check your version of python (unless you changed your default version after installing Python 3, this will be a version of Python 2)
```bash
$ python --version
Python 2.7.16
```
* Check that you can select Pythong 3 by specifying python3
```bash
$ python3 --version
Python 3.9.6
```
* Or by running python 3 (you can exit python with the "quit()" command)
```bash
$ python3
Python 3.9.6 (default, Aug  4 2021, 22:40:34) 
[Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```

Now, without leaving the HOOMDblue directory, set VirtEnv to use python3 (this will create all the base directory files (bin, etc.) in the VirtEnv folder)
```bash
python3 -m venv VirtEnv/ --system-site-packages
```

(You can move into the VirtEnv folder and check that it worked with "python --version")

If you moved to VirtEnv, use "cd .." to go back up one level to the HOOMDblue directory and source to the virtual environment
```bash
source VirtEnv/bin/activate
```

You are now working in the virtual environment!

## Acquiring HOOMD-blue

We use the stable release of HOOMD-blue (v2.9.7), available with installation instructions [here](https://hoomd-blue.readthedocs.io/en/stable/installation.html). In our experience, cloning from Git leads to errors during the installation process. Therefore, it is recommended that you instead download the tar file and manually unzip it.

* Download the tar file using the Terminal
```bash
$ curl -O https://glotzerlab.engin.umich.edu/Downloads/hoomd/hoomd-v2.9.7.tar.gz
```

* Go to the home directory in Finder. 
If you have not already added your home directory to the Finder sidebar it may be difficult to access. To fix this, open a new Finder window and select "Downloads" from the Favorites sidebar. Then, at the top of the Finder window, right click on the current folder name (Downloads) and select the Users folder. You should see a folder named your username. Drag and drop that folder into the Favorites sidebar (it will create a shortcut).

* From your home directory, go to "repositories" and then HOOMDblue
* Double click on the tar file to unzip it
* Leave the new, unzipped folder and drag and drop the tar file to the Trash
* Go back to the Terminal window

## Installing HOOMD-blue

You are now ready to install HOOMD-blue!

* Move to the new hoomd folder
```bash
$ cd hoomd-v2.9.7
```
* Make a build directory and move to it
```bash
$ mkdir build && cd build
```
* Configure as instructed on the [HOOMD-blue installation website](https://hoomd-blue.readthedocs.io/en/stable/installation.html) (ignoring the GPU related steps)
```bash
$ cmake ../ -DCMAKE_INSTALL_PREFIX=`python3 -c "import site; print(site.getsitepackages()[0])"`
```
* Compile
```bash
$ make -j4
```
* And install HOOMD-blue into your Python environment
```bash
make install
```

HOOMD-blue is installed! If needed you can install NumPy or other required Python packages with pip
```bash
$ pip install NumPy
```

See the Guide to Working with Simulations for next steps.

