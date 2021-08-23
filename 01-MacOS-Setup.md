# MacOS System Setup Recommendations and Tips

This is a guide to setting up a new MacOS computer for command line programming before installing and using [HOOMD-blue] for colloids simulations in the [PRoPS Group]. If you are new to MacOS, or new to programming on MacOS, then this guide can help you get started.

This guide was complied by Rob Campbell, and was last updated in August 2021.

[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/
[PRoPS Group]: https://web.northeastern.edu/complexfluids/
<br>

## Terminal for Command Line Programming in MacOS

MacOS uses the Terminal application for command line programming. The Terminal app is located in the Utilities folder, and can be accessed by opening Finder and selecting Applications from the Favorites sidebar

>Applications/Utilities/Terminal

or via Launchpad in the Other folder

>Launchpad/Other/Terminal

Once you have opened the Terminal application you can create a shortcut to it that stays in the Dock at the bottom of your screen. 

After you open Terminal, right click the Terminal icon in the Dock at the bottom of your screen, scroll up to "Options," and select "Keep in Dock."

By default, Terminal opens in your home directory (where "you_username" is the username you use on for you profile on your computer)
```bash
/Users/your_username
```
This is where you will want to install most packages and create most files and folders/directories/repositories.

In older versions of MacOS the default Terminal window uses the bash shell (similar to Linux and HPC clusters); however, more recent versions of MacOS use the zsh shell (seemingly due to licensing). Both bash and zsh exist on MacOS, but Apple strongly recommends switching to zsh. Many online resources for command line programming on MacOS still reference bash, so keep in mind which shell you are using when troubleshooting.

Using zsh is very similar to using bash. The main difference you will notice at first is the symbol at the end of the prompt

Bash uses $
```bash
$
```
and zsh uses %
```bash
%
```

Another important difference is which file you use to modify the prompt. If you want to make any changes to settings in the Terminal prompt you will need to modify the ~/.bash_profile in bash and the ~/.zshrc file in zsh.
<br>
<br>
## Xcode

The first thing you need to do before using the Terminal is install Xcode. Xcode includes several essential pieces of software for programming in MacOS.

Open a Terminal window and enter
```bash
$ xcode-select --install 
```
<br>

## Package Manager

You will also need to install a package manager, like [Homebrew](https://brew.sh/)
```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
This script (copied from the Homebrew [website](https://brew.sh/)) explains what it will do and then pauses before installing.

Some simple Homebrew commands are<br>
Update Homebrew
```bash
$ brew update
```
Install software/packages
```bash
$ brew install package-name
```
and update installed software
```bash
$ brew upgrade package-name
```
<br>

## Text Editors

You will want to get comfortable with a command line text editor for quickly creating and editing files. MacOS includes [Nano](https://www.nano-editor.org/) and [Vim](https://www.vim.org/). You can update these or install other text editors with Homebrew.

Open and existing file (or create a new one) with
```bash
$ vim filename
```

*Note on Vim*<br>
Vim is powerful, but difficult to get used to because of its unintuitive default interface and its many functions and shortcuts. The basics of Vim are: 
* Opening a file with "vim" does not allow you to immediately edit it. You must first enter "Instert" mode, by pressing "i"
* To stop editing a file, press "esc" to return to the default mode
* The command ":q" will quit a file that has not been edited
* The command ":q!" will quit a file that has been edited WITHOUT saving changes
* The command ":wq" will save and quite a file that has been edited
<br>

## Cmake

HOOMD-blue requires [cmake](https://cmake.org/), which you can go ahead and install or update now with Homebrew
```bash
$ brew install cmake
```
<br>

## Python 3

MacOS comes with Python 2 pre-installed, but you DO NOT want to use this Python. Not only do we want to use Python 3, rather than Python 2, but the pre-installed version of Python 2 is used by your computer internally, and so it's best not to mess with it. 

One way to manage multiple versions of Python is by using virtual environments. If you plan on working with several different versions of Python across multiple projects, then you probably want to install [pyenv](https://github.com/pyenv/pyenv) for easier version and virtual environment management. This is not required to use HOOMD-blue. We will use virtual environemnts when working with HOOMD-blue, but you do not need pyenv for that and can instead use the built-in venv option. More on that in the HOOMD-blue Installation Guide.

If you are using pyenv, see the [pyenv site](https://github.com/pyenv/pyenv) for more details on how it works before installing it with Homebrew.

If you decide not to use pyenv, then you can still install Python 3 with
```bash
$ brew install python
```
This will also install pip, the Python package manager, which you can use to install NumPy and other required packages. 
```bash
$ pip install NumPy
```

Whichever installation method you choose, you will be able to check you version of Python with 
```bash
$ python --version
```
You will be able to run the default version of Python with 
```bash
$ python
```
And you can specify Python 3 with
```bash
$ python3
```


