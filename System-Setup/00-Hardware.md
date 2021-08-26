# Hardware Requirements and System Recommendations

This is a guide to choosing a computer for research simulating colloids with [HOOMD-blue] in the [PRoPS Group].

[Last Update: August 2021]

This guide was compiled by Rob Campbell.

[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/
[PRoPS Group]: https://web.northeastern.edu/complexfluids/
<br>

## Operating System

HOOMD-blue currently requires MacOS or Linux. MacOS is recommended because it is what current group members use, and what you can get the most help troubleshooting. That said, if you are familiar with Linux and prefer it over MacOS you can definitely choose to use a Linux machine.
<br>
<br>
## Laptop vs. Desktop

A laptop is sufficient for this work. Most simulations are run on Northeastern's Discovery research cluster, so you will mainly be using your computer for writing scripts, debugging, and interfacing with the cluster. Most members of the group have chosen 13" laptops because they're more portable, but if you prefer a larger screen for programming absolutely go for it.
<br>
<br>
## Memory

Memory is the **most important** feature for our work. In our experience 8GB is not enough to do this work without the computer getting hot/slow quite often, so opt for at least 16GB. It's unlikely you'll need more than 16GB unless you plan to use other software that requries it.
<br>
<br>
## Storage

For storage, we recommend 500GB. Most data will be stored externally on the cluster or other devices, so you shouldn't need more locally unless a particular project requires it.
<br>
<br>
## GPU

Our implementation of HOOMD-blue is currently CPU only (without parallelization) so you will not need a high performance GPU unless you intend to redevelop the code. HOOMD-blue has existing GPU options, but we found them difficult to set up in the past and chose not to use them at this time.
<br>
<br>
## Processor

Any reasonably current processor should be good enough for this work. Our group members currently use the 2018 Intel i7, 2020 Intel i7, and 2020 Intel i5 without issue.

Most Mac computers will soon switch over from Intel to Apple silicon (starting with the M1 chip). We expect Apple silicon to be a great choice in the future. For 2021, pandemic-related chip-shortages have made it easier to get a hold of Intel Macs, so that is what we recommend this year.
<br>
<br>
## Current Hardware Used by Group Members (Fall 2021)

13-inch MacBook Pro 2018
* Processor: 2.7 GHz Quad-Core Intel Core i7
* Memory: 16GB 2133 MHz LPDDR3
* Storage: 500GB
<br>

13-inch MacBook Pro 2020
* Processor: 2 GHz Quad-Core Intel Core i5
* Memory: 16GB 3733 MHz LPDDR4X
* Storage: 512GB SSD
<br>

13-inch MacBook Pro 2020
* Processor: 2 GHz Quad-Core Intel Core i7
* Memory: 16GB 3733 MHz LPDDR4X
* Storage: 512GB SSD
<br>

