# MacOS System Setup Recommendations and Tips

This is a guide to setting up a new MacOS computer for command line programming, specifically what to do before installing and using [HOOMD-blue] for colloids simulations in the [PRoPS Group]. If you are new to MacOS, or new to programming on MacOS, then this guide can help you get started.

[Last Update: December 2021]

This guide was complied by Rob Campbell.

[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/
[PRoPS Group]: https://web.northeastern.edu/complexfluids/
<br>

## Contents
1. [Terminal for Command Line Programming in MacOS](/System-Setup/01-MacOS-Setup.md#terminal-for-command-line-programming-in-macos)
2. [Xcode](/System-Setup/01-MacOS-Setup.md#xcode)
3. [Package Managers](/System-Setup/01-MacOS-Setup.md#package-managers)
4. [Text Editors](/System-Setup/01-MacOS-Setup.md#text-editors)
5. [Cmake](/System-Setup/01-MacOS-Setup.md#cmake)
6. [Python 3](/System-Setup/01-MacOS-Setup.md#python-3)
7. [IDEs](/System-Setup/01-MacOS-Setup.md#ides)
8. [Git and Github](/System-Setup/01-MacOS-Setup.md#git-and-github)
<br>

## Terminal for Command Line Programming in MacOS

MacOS uses the Terminal application for command line programming. The Terminal app is located in the Utilities folder, and can be accessed by opening Finder and selecting Applications from the Favorites sidebar

>Applications/Utilities/Terminal

or via Launchpad in the Other folder

>Launchpad/Other/Terminal

Once you have opened the Terminal application you can create a shortcut to it that stays in the Dock at the bottom of your screen. 

After you open Terminal, right click the Terminal icon in the Dock at the bottom of your screen, scroll up to "Options," and select "Keep in Dock."

By default, Terminal opens in your home directory (where "your_username" is the name of your account on your computer)
```bash
/Users/your_username
```
This is where you will want to install most packages and create most files and folders/directories/repositories.

In older versions of MacOS the default Terminal window uses the bash shell (the same as Linux and most HPC clusters); however, more recent versions of MacOS use the zsh shell (seemingly due to licensing). Both bash and zsh exist on MacOS, but Apple strongly recommends switching to zsh. Many online resources for command line programming on MacOS still reference bash, so keep in mind which shell you are using when troubleshooting.

Using zsh is very similar to using bash. The main difference you will notice at first is the symbol at the end of the prompt

Bash uses $
```bash
$
```
and zsh uses %
```bash
%
```

Another important difference is which file you use to modify the prompt. If you want to make any changes to settings in the Terminal prompt you will need to modify the `~/.bash_profile` in bash and the `~/.zshrc` file in zsh.
<br>
<br>
## Xcode

Now that you are familiar with the Terminal, the first thing you need to do is install Xcode. Xcode includes several essential pieces of software for programming in MacOS.

Open a Terminal window and enter
```bash
% xcode-select --install 
```
<br>

## Package Managers

You will also need to install a package manager, such as [Homebrew](https://brew.sh/). You can install Homebrew with
```bash
% /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
This script (from the Homebrew [website](https://brew.sh/)) explains what it will do and then pauses before installing.

Some simple Homebrew commands are:

Update Homebrew
```bash
% brew update
```
Install software/packages
```bash
% brew install package-name
```
And update installed software
```bash
% brew upgrade package-name
```
<br>

## Text Editors

You will want to get comfortable with a command line text editor for quickly creating and editing files. MacOS includes [Nano](https://www.nano-editor.org/) and [Vim](https://www.vim.org/). You can update these or install other text editors with Homebrew.

For Vim, open an existing file (or create a new one) with
```bash
% vim filename
```

*Note about using Vim:*<br>
Vim is powerful, but difficult to get used to because of its unintuitive default interface and its many functions and shortcuts. The basics of Vim are: 
* Opening a file with `vim` does not allow you to immediately edit it. You must first enter "Instert" mode, by pressing `i`
* To stop editing a file, press `esc` to return to the default mode
* Back in the default "Normal" mode, you can search for something in your file using "/" (for example, so search for instances of the word "something" type "/something")
* The command `:q` will quit a file that has not been edited
* The command `:q!` will quit a file that has been edited WITHOUT saving changes
* The command `:wq` will save (write) and quit a file that has been edited

For more on using Vim, see the lectures in ["The Missing Semester of Your CS Education"](https://missing.csail.mit.edu/) and our other [Vim Programming Resources](/Programming-Resources#vim)
<br>

## Cmake

HOOMD-blue requires [cmake](https://cmake.org/), which you can go ahead and install or update now with Homebrew
```bash
% brew install cmake
```
<br>

## Python 3

MacOS comes with Python 2 pre-installed, but you **DO NOT** want to use this Python. Not only do we want to use Python 3, rather than Python 2, but the pre-installed version of Python 2 is used by your computer internally, and so it's best not to mess with it. 

One way to manage multiple versions of Python is by using virtual environments. If you plan on working with several different versions of Python across multiple projects, then you may want to install [pyenv](https://github.com/pyenv/pyenv) and/or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html) for easier version and virtual environment management. This is not required to use HOOMD-blue. We will use virtual environemnts when working with HOOMD-blue, but you do not need pyenv or virtualenvwrapper for that, you can instead use the built-in venv option. There is more on venv in the [HOOMD-blue Installation Guide](../01-HOOMDblue-Install-Guide.md). If you are using pyenv, see the [pyenv website](https://github.com/pyenv/pyenv) for more details on how it works before installing it with Homebrew.

Another popular option is to use the package and environment manager [conda](https://docs.conda.io/en/latest/) via Miniconda (the basic installation) or Anaconda (a larger installation with 7500+ packages included). Conda is also not required for using HOOMD-blue. If you are using conda, see the [conda website for installation steps](https://docs.conda.io/en/latest/).

If you decide not to use pyenv or conda, then you can still install Python 3 with
```bash
% brew install python
```
This will also install pip, the Python package manager, which you can use to install NumPy and other required Python packages once we set up our virtual environments during the HOOMD-blue installation steps.

Whichever installation method you choose, you will be able to check your current version of Python with 
```bash
% python --version
```
You will can run the current (default) version of Python with 
```bash
% python
```
And you can specify running Python 3 with
```bash
% python3
```
<br>

## IDEs

While you can write and edit scripts with a text editor, you will likely want to install an integrated development environment (IDE) for developing and debugging your code.

It is recommended that you download [Eclipse](https://www.eclipse.org/downloads/) for C++ programming.

You can also use Eclipse for developing Python code, but you may be better off with a dedicated Python IDE. For working on MacOS, people frequently recommend [PyCharm](https://www.jetbrains.com/pycharm/), although members of our lab currently prefer [Spyder](https://www.spyder-ide.org/). (For help setting up Spyder, chat to Soohee or Milad)
<br>
<br>
## Git and Github

Git is a version management tool, especially useful for collaborating with others on shared code. If you're interested in using Github and need help setting up command-line Git, you can check out the separate [guide to setting up Git](/Programming-Resources/Git-Setup.md) in the Programming Resources directory.

