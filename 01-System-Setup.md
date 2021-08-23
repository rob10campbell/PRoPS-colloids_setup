# MacOS System Setup Recommendations and Tips

This is a guide to setting up a new MacOS computer before installing and using [HOOMD-blue] for colloids simulations in the [PRoPS Group]. If you are new to MacOS, or new to programming on MacOS, then this guide can help you get started.

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

The first thing you need to do before using the Terminal is install Xcode. Xcode includes several essential packages and pieces of software for programming in MacOS.

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
This script (from the Homebrew [website](https://brew.sh/)) explains what it will do and then pauses before it does it.

Some simple Homebrew commands are
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

You will want to get comfortable with a command line text editor for quickly creating and editing files. MacOS includes [nano](https://www.nano-editor.org/) and [vim](https://www.vim.org/). You can update these or install other text editors with Homebrew.
<br>
<br>
## Cmake

HOOMD-blue requires [cmake](https://cmake.org/), which you can go ahead and install or update now with Homebrew
```bash
$ brew install cmake
```
<br>
<br>
## Python 3



