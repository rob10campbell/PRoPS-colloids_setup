# Simulating waterDPD

This is a guide for running a simple particle simulation with [HOOMD-blue] for research in the [PRoPS Group].

This guide is optimized for MacOS. See the [HOOMD-blue Installation Guide](https://github.com/rob10campbell/PRoPS-colloids_setup/blob/main/02-HOOMDblue-Install-Guide.md) for prerequisites.

[Last Update: August 2021]

The standard implementation of HOOMD-blue was adapted for our colloids simulations by Mohammad (Nabi) Nabizadeh. Nabi also created the [waterDPD.py](https://github.com/rob10campbell/PRoPS-colloids_setup/blob/main/waterDPD.py) file. This guide was compiled by Rob Campbell.

[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/
[PRoPS Group]: https://web.northeastern.edu/complexfluids/
<br>

## Getting the waterDPD.py File

A good way to start working with colloids simulations in HOOMD-blue is to run a dissipative particle dynamics (DPD) simulation of a random distribution of water particles. You will need the `waterDPD.py` file provided in this repository to run this simulation.

If you haven't already, clone this repository (or a fork of this repository) to your "repositories" directory.<br>
*Note: For help setting up command line git with Github, see the MacOS Setup guide.*
```bash
$ cd repositories/
$ git clone https://github.com/rob10campbell/PRoPS-colloids_setup.git
```
Move to the simulations directory in your "HOOMDblue" repository and make a directory for the water simulation
```bash
$ cd ~/repostiories/HOOMDblue/sims/
$ mkdir water
```
Move to the "water" directory and copy waterDPD.py into that directory from the cloned copy of this repository
```bash
$ cd water
$ cp ~/repositories/PRoPS-colloids_setup/waterDPD.py waterDPD.py
$ ls
waterDPD.py
```
<br>

## About waterDPD.py

After downloading `waterDPD.py` you can exam it with an integrated development environment (IDE) such as [Eclipse](https://www.eclipse.org/downloads/) or [Pycharm](https://www.jetbrains.com/pycharm/), or with a built-in text editor such as [Vim](https://www.vim.org/)
```bash
$ vim waterDPD.py
```
*Note: If you are viewing or editing* `waterDPD.py` *in an IDE you should already have line numbering enabled by default. If you are using Vim you will need to turn on line numbers with the command* `:set number` *or* `:set nu`

You will see that the `waterDPD.py` Python script is divided into 4 sections:
1. Importing a list of packages
2. Defining a set of Inputs
3. Calculating additional values based on the Inputs
4. Initializing HOOMD-blue and running the simulation, including any outputs

This is our standard framework for writing colloids simulation scripts. 
<br>
<br>
If you look more closely at the 4th section ("Total INITIALIZE") you will see that the code:<br>
* Initializes HOOMD-blue
```python
29 #################        Total INITIALIZATION        ##############
30 hoomd.context.initialize("");
```
* Creates a random distribtion (scroll right in the box below to see the full code)
```python
31 hoomd.deprecated.init.create_random(N=N_Solvents, box=hoomd.data.boxdim(Lx=L_X, Ly=L_Y, Lz=L_Z), name='A', min_dist=0., seed=randomint(1, 101), dimensions=3)
32
33 nl = hoomd.md.nlist.tree();
34 groupA = hoomd.group.type(name='groupA', type='A');
35
```
* Sets up the dissipative particle dynamics (DPD) interactions (where A, gamma, and T are the only required variables)
```python
36 dpd = hoomd.md.pair.dpd(r_cut= 1 * r_c, nlist=nl, kT=KT, seed=simulation_seed);
37 dpd.pair_coeff.set('A', 'A', r_cut= 1.0 * r_c, A=25, gamma=4.5);
38
```
* Uses a standard integration mode to integrate across all the particles over time
```python
39 hoomd.md.integrate.mode_standard(dt=dt_Integration);
40 all = hoomd.group.all();
41 hoomd.md.integrate.nve(group = all);
42
43
```
* And then produces two output files, "Equilibrium.gsd" and "Pressure_xy.log"
```python
44 hoomd.dump.gsd(filename="Equilibrium.gsd", overwrite=True, period=1, group=all, dynamic=['attribute', 'momentum', 'topology'])
45 hoomd.analyze.log(filename='Pressure_xy.log', overwrite=True ,
46                   quantities=['pressure_xy','temperature'],period=1)
47 hoomd.run(N_time_steps);
```

Now that you have examined the `waterDPD.py` script, close the file (in Vim, `esc` `:q`) and try running the simulation.
<br>
<br>
## Running a Simulation

Go back to the "HOOMDblue" directory and activate the virtual environment
```bash
$ cd ..
$ cd ..
$ pwd
/Users/your_username/repositories/HOOMDblue
$ source VirtEnv/bin/activate
(VirtEnv) $
```
You can now move back to the directory for the water simulation and run `waterDPD.py`.<br>
*Note:* `waterDPD.py` *intentionally imports several packages when it is run. You will likely be prompted to install some of these packages before you can run the file (e.g. to install gsd, use* `pip install gsd`*). After you have installed any missing packages, try running the file again.*
```bash
(VirtEnv) $ cd sims/water/
(VirtEnv) $ python3 waterDPD.py
```
This should launch HOOMD-blue, display the file, and then run the file.

Successfully running the file will add two new output files to the directory: `Equilibrium.gsd` and `Pressure_xy.log`<br>
You can check that this worked by viewing the files currently in this folder with the command `ls`
```bash
(VirtEnv) $ ls
Equilibrium.gsd	Pressure_xy.log	waterDPD.py
```
You can open `Pressure_xy.log` with Vim or another text editor to see the recorded temperature and pressure at each timestep. 
```bash
(VirtEnv) $ vim Pressure_xy.log
```
For example, the first 4 lines should look something like this (although the numbers will be different)
```vim
timestep	pressure_xy	temperature
0	0.1109824717	0
1	0.1085123802	0.02589183378
2	0.1036177395	0.09799321669
```
<br>

In contrast, if you open the GSD file it will look like gibberish. The GSD file generates a visualization of the simulation, which we will view later with the [Visual Molecular Dynamics (VMD)](https://www.ks.uiuc.edu/Research/vmd/) software.
<br>
<br>
## Modifying waterDPD.py

Now that you have successfully run the simulation, you can try making changes to the inputs and then check the `Pressure_xy.log` file to see how the simulation changes.

For reproducibility when testing and debugging these simulations you should replace the `simulation_seed` with a fixed value (e.g. 123) in the "Total INITIALIZATION" section on lines `31` and `36` (scroll right on the box below to see the changes to line `31`)
```python
29 #################        Total INITIALIZATION        ##############
30 hoomd.context.initialize("");
31 hoomd.deprecated.init.create_random(N=N_Solvents, box=hoomd.data.boxdim(Lx=L_X, Ly=L_Y, Lz=L_Z), name='A', min_dist=0., seed=123, dimensions=3)
32
33 nl = hoomd.md.nlist.tree();
34 groupA = hoomd.group.type(name='groupA',type='A');
35
36 dpd = hoomd.md.pair.dpd(r_cut= 1 * r_c, nlist=nl, kT=KT, seed=123);
37 dpd.pair_coeff.set('A', 'A', r_cut= 1.0 * r_c, A=25, gamma=4.5);
```
Once you have made these changes you can go back up to the "INPUTS" section and try changing the timestep dt (line `22`), KT (line `23`), etc. to see how changes affect the behavior of the system during the simulation (i.e. what changes happen to the pressures and temperatures recorded in the `Pressure_xy.log` file).
```python
20 ################           INPUTS             ##############
21 N_time_steps = 1000;L_X = 10; L_Y = 10; L_Z = 10;
22 dt_Integration = 0.01; m_S = 1; R_S = 0.5;
23 r_c = 1; rho = 3; KT = .1;
```
<br>

## Other Examples

Now that you are familiar with using HOOMD-blue to run the `waterDPD.py` example you can get more comfortable with HOOMD-blue's capabilities by working through the examples in "[Introducing HOOMD-blue](https://github.com/glotzerlab/hoomd-examples/tree/master/00-Introducing-HOOMD-blue)."
<br>
<br>
For next steps, see the [VMD Installation Guide](https://github.com/rob10campbell/PRoPS-colloids_setup/blob/main/04-VMD-Install-Guide.md). 