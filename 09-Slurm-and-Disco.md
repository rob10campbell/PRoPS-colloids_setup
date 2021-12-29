# Running Simulations on Discovery

This is a guide to the basics of running colloids simulations on Discovery, Northeastern University's HPC cluster, for research in the [PRoPS Group](https://web.northeastern.edu/complexfluids/).

This guide is optimized for MacOS. See the [Guide to Accessing Discovery](/08-Accessing-Discovery.md) and for prerequisites. This guide also assumes that you are familiar with the other content in this repository and know how to run DPD simulations of colloids.

[Last Update: December 2021]

This guide was compiled by Rob Campbell.

## Installing HOOMD-blue on Discovery

Before running simulations on Discovery your should install your own version of HOOMD-blue. If shared-storage space on `/work/props` becomes an issue we may switch to common installations, but for now you are free to install your own in your folder on `/work/props`.
***NOTE: This installation process can take several hours***

Go to the your folder on the `work` directory and create a new folder for your installation of HOOMD-blue.
```bash
[yourusername@login-00 ~]$ cd /work/props/yourname/HOOMD-blue
[yourusername@login-00 HOOMD-blue]$ 
```
Before installing HOOMD-blue you will need to load some software. Check your currently loaded software first. You should see the module needed to interact with discovery and any other software you have already loaded
```bash
[yourusername@login-00 HOOMD-blue]$ module list
  1) discovery/2021-10-6
```
As discussed in the [HOOMD-blue Installation Guide](/01-HOOMDblue-Install-Guide.md), we will need Python 3 and cmake. Load the latest version of both (unless you know a different version will be necessary for your code). At the time of writing, these are Python 3.8.1 and cmake 3.18.1
```bash
[yourusername@login-00 HOOMD-blue]$ module load python/3.8.1
[yourusername@login-00 HOOMD-blue]$ module load cmake/3.18.1 
[yourusername@login-00 HOOMD-blue]$ module list
  1) discovery/2021-10-06   2) python/3.8.1           3) cmake/3.18.1
```
Now create your virual environment
```bash
[yourusername@login-00 HOOMD-blue]$ mkdir VirtEnv
[yourusername@login-00 HOOMD-blue]$ python3 -m venv VirtEnv/ --system-site-packages
```
Download and unzip HOOMD-blue 2.9.7
```bash
[yourusername@login-00 HOOMD-blue]$ curl -O https://glotzerlab.engin.umich.edu/Downloads/hoomd/hoomd-v2.9.7.tar.gz 
[yourusername@login-00 HOOMD-blue]$ tar -xf hoomd-v2.9.7.tar.gz
```
Then enter the virtual environment and make sure you are using the correct version of Python. It should be the version located at your virtual environment NOT the version on Discovery's shared drive (you can compare with the location of cmake)
```bash
[yourusername@login-00 HOOMD-blue]$ source VirtEnv/bin/activate
(VirtEnv) [yourusername@login-00 HOOMD-blue]$ which python
/work/props/yourusername/HOOMD-blue/VirtEnv/bin/python
(VirtEnv) [yourusername@login-00 HOOMD-blue]$ which cmake
/shared/centos7/cmake/3.18.1/bin/cmake
```
Finally, move to the hoomd-v2.9.7 folder and create (and move to) the build folder, configure HOOMD-blue (ignoring the GPU options), and then compile and install HOOMD-blue
```bash
(VirtEnv) [yourusername@login-00 HOOMD-blue]$ cd hoomd-v2.9.7
(VirtEnv) [yourusername@login-00 hoomd-v2.9.7]$ mkdir build && cd build
(VirtEnv) [yourusername@login-00 build]$ cmake ../ -DCMAKE_INSTALL_PREFIX=`python3 -c "import site; print(site.getsitepackages()[0])"` 
(VirtEnv) [yourusername@login-00 build]$ make -j4
(VirtEnv) [yourusername@login-00 HOOMD-blue]$ make install 
```
***NOTE: These last 2 steps can take several hours***

Once you have installed the base version of HOOMD-blue you will want to modify it with the files described in [Modifying HOOMD-blue](/06-Modifying-HOOMDblue.md). Copy those files into your new installation of HOOMD-blue and then recompile and reinstall the software to make sure you are running the correct version (this should be faster than the first installation).

It is recommended that you always have a version of the base HOOMD-blue AND the modified HOOMD-blue installed on your computer for debugging. It is up to you if you want to have both installed on Discovery as well.

## Scheduling a Job with Slurm

It is best practice to use a bash file (i.e. `exec.bash`) to submitting a job on Discovery. This file will use the [Slurm Workload Manager](https://slurm.schedmd.com/documentation.html) to manage the job.
