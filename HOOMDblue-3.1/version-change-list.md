# Version change list

HOOMD-blue provides detailed information on migrating from 2.9 to 3.0, including a number of classes that have been renamed or removed to match the new API. A full list of changes is [available here](https://hoomd-blue.readthedocs.io/en/latest/migrating.html). This file aims to be a cheat-sheet for interpreting old code with the PRoPS group, highlighting the class changes that most directly affected Nabi's colloid simulation formatting.

# List of key changes relevant to gelation simulations
- [hoomd.dump](https://hoomd-blue.readthedocs.io/en/v2.9.7/module-hoomd-dump.html) --> [hoomd.write](https://hoomd-blue.readthedocs.io/en/v3.0.0/module-hoomd-write.html)
- [hoomd.context.initialize](https://hoomd-blue.readthedocs.io/en/v2.9.3/module-hoomd-context.html) --> [hoomd.device.CPU](https://hoomd-blue.readthedocs.io/en/v3.0.0/module-hoomd-device.html) or hoomd.device.GPU 
- [hoomd.data](https://hoomd-blue.readthedocs.io/en/v3.0.0/module-hoomd-data.html) --> [hoomd.State](https://hoomd-blue.readthedocs.io/en/v3.0.0/package-hoomd.html)
- [hoomd.group](https://hoomd-blue.readthedocs.io/en/v2.9.7/module-hoomd-group.html) --> [hoomd.filter](https://hoomd-blue.readthedocs.io/en/v3.0.0/module-hoomd-filter.html)
- [hoomd.init](https://hoomd-blue.readthedocs.io/en/v2.9.7/module-hoomd-init.html) --> [hoomd.Simulation](https://hoomd-blue.readthedocs.io/en/v3.0.0/package-hoomd.html) create_state_from_ factory methods
- [hoomd.md.integrate.mode_standard](https://hoomd-blue.readthedocs.io/en/v2.9.7/module-md-integrate.html) --> [hoomd.md.Integrator](https://hoomd-blue.readthedocs.io/en/v3.0.0/package-md.html)
- [deprecated.analyze.msd](https://hoomd-blue.readthedocs.io/en/v2.9.7/module-deprecated-analyze.html) --> Offline analysis (they recommend their other package, [Freud](https://freud.readthedocs.io/en/latest/))
- [deprecated.init.create_random](https://hoomd-blue.readthedocs.io/en/v2.9.7/module-deprecated-init.html) --> recommend replacing with mBuild, packmol, or your own script

