# Getting Setup with the Discovery Cluster

This is a guide to getting setup to use the Discovery Cluster at Northeastern University for research in the [PRoPS Group].

This guide is optimized for MacOS.

[Last Update: August 2021]

This guide was compiled by Rob Campbell.

[PRoPS Group]: https://web.northeastern.edu/complexfluids/
<br>

## Getting Access

To request access to the Discovery cluster, complete the [ServiceNow Research Computing Access Request form](https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0ae24596db535fc075892f17d496199c). We do not need the software Gaussian.

More details on getting access and using Discovery are available in [the Discovery documentation](https://rc-docs.northeastern.edu/en/latest/get_started/get_access.html).
<br>
<br>
## Connecting to Discovery

Once you have been granted access to Discovery you should have both a home folder (`your_username`) and a `scratch` folder (`/scratch/your_username`) that you can access on the cluster.

You can login to your Discovery home folder from your Terminal shell with the command
```bash
$ ssh -Y campbell.r@login.discovery.neu.edu
```
And by entering your MyNortheastern username and password.

You can then move to the `scratch` folder with
```bash
$ cd /scratch/your_username
```

To learn more about connecting to Discovery, including setting up passwordless SSH, see [Connecting to Discovery](https://rc-docs.northeastern.edu/en/latest/get_started/connect.html#mac) on the Discovery docs.
<br>
<br>
## Learning How to Use Discovery

To get started understanding the Discover cluster you should watch the introductory training video on [Northeastern's LinkedIn Learning page](https://www.linkedin.com/checkpoint/enterprise/login/74653650?pathWildcard=74653650&application=learning&redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Flearning%2Fcontent%2F1139340%3Fu%3D74653650).

You can also sign up for [training sessions](https://rc.northeastern.edu/support/training/) on introductory and advanced topics.

And you can schedule an "office hours" style meeting for 1-on-1 help from a Research Computing staff member at the RC [Consulting page](https://rc.northeastern.edu/support/consulting/).
<br>
<br>
## Getting Access to the `work` Directory

As a member of the PRoPS Group you should have access to the `props` directory on `work`. This is where you will store most of your data.

After connecting to Discovery, you can check this with
```bash
$ cd /work/props
```

If you do not have permission to access this directory contact RC Help.

After you get access to `/work/props` you can create your own folder for your projects
```bash
$ cd /work/props
$ mkdir your_name
```
<br>

## Requesting Access to Additonal Partitions

You automatically have access to the essential partitions for running small jobs on Discovery; however, you will likely need access to additional partitions, such as `long` or `large`, during the course of your research.

To request access to one of these partitions use the [Partition Access Request Form](https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0c34d402db0b0010a37cd206ca9619b7).
<br>
<br>
## Copying files to Discovery

There are several ways that you can copy files to and from Discovery:

The method used in most Discovery Trainings is the web-based interface [Discovery Open on Demand (OOD)](https://ood.discovery.neu.edu/pun/sys/dashboard).

You can also transfer small files from your computer to Discovery on the terminal with the `scp` command and Discovery's dedicated transfer node (`xfer`). You cannot transfer data from the `login` node or any other node except `xfer`.

For example, to transfer files to your `/scratch` space, use the command:
```bash
$ scp filename yourusername@xfer.discovery.neu.edu:/scratch/yourusername
```
The Discovery documentation includes more details about [transfering files](https://rc-docs.northeastern.edu/en/latest/using-discovery/transferringdata.html), including options for SSHFS.

The *recommended* method for transfering files (especially large data files) is with Globus. You can learn more about how to set up a Globus account and enable Globus' command line tools on the [Using Globus](https://rc-docs.northeastern.edu/en/latest/using-discovery/globus.html#using-globus) page in the Discovery documentation.
<br>
<br>
## Advice for Running Simulations on Discovery

[to be added]
