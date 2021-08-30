# MacOS System Setup Recommendations and Tips

This is a guide to setting up a new MacOS computer for command line programming, specifically what to do before installing and using [HOOMD-blue] for colloids simulations in the [PRoPS Group]. If you are new to MacOS, or new to programming on MacOS, then this guide can help you get started.

[Last Update: August 2021]

This guide was complied by Rob Campbell.

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
$ xcode-select --install 
```
<br>

## Package Manager

You will also need to install a package manager, such as [Homebrew](https://brew.sh/). You can install Homebrew with
```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
This script (from the Homebrew [website](https://brew.sh/)) explains what it will do and then pauses before installing.

Some simple Homebrew commands are:

Update Homebrew
```bash
$ brew update
```
Install software/packages
```bash
$ brew install package-name
```
And update installed software
```bash
$ brew upgrade package-name
```
<br>

## Text Editors

You will want to get comfortable with a command line text editor for quickly creating and editing files. MacOS includes [Nano](https://www.nano-editor.org/) and [Vim](https://www.vim.org/). You can update these or install other text editors with Homebrew.

For Vim, open an existing file (or create a new one) with
```bash
$ vim filename
```

*Note about using Vim:*<br>
Vim is powerful, but difficult to get used to because of its unintuitive default interface and its many functions and shortcuts. The basics of Vim are: 
* Opening a file with `vim` does not allow you to immediately edit it. You must first enter "Instert" mode, by pressing `i`
* To stop editing a file, press `esc` to return to the default mode
* The command `:q` will quit a file that has not been edited
* The command `:q!` will quit a file that has been edited WITHOUT saving changes
* The command `:wq` will save (write) and quit a file that has been edited
<br>

## Cmake

HOOMD-blue requires [cmake](https://cmake.org/), which you can go ahead and install or update now with Homebrew
```bash
$ brew install cmake
```
<br>

## Python 3

MacOS comes with Python 2 pre-installed, but you **DO NOT** want to use this Python. Not only do we want to use Python 3, rather than Python 2, but the pre-installed version of Python 2 is used by your computer internally, and so it's best not to mess with it. 

One way to manage multiple versions of Python is by using virtual environments. If you plan on working with several different versions of Python across multiple projects, then you may want to install [pyenv](https://github.com/pyenv/pyenv) for easier version and virtual environment management. This is not required to use HOOMD-blue. We will use virtual environemnts when working with HOOMD-blue, but you do not need pyenv for that and can instead use the built-in venv option. More on that in the [HOOMD-blue Installation Guide](../01-HOOMDblue-Install-Guide.md).

If you are using pyenv, see the [pyenv website](https://github.com/pyenv/pyenv) for more details on how it works before installing it with Homebrew.

Another popular option is to use the package and environment manager [conda](https://docs.conda.io/en/latest/) via Miniconda (the basic installation) or Anaconda (a larger installation with 7500+ packages included). Conda is also not required for using HOOMD-blue. If you are using conda, see the [conda website for installation steps](https://docs.conda.io/en/latest/).

If you decide not to use pyenv or conda, then you can still install Python 3 with
```bash
$ brew install python
```
This will also install pip, the Python package manager, which you can use to install NumPy and other required Python packages. 
```bash
$ pip install NumPy
```

Whichever installation method you choose, you will be able to check your current version of Python with 
```bash
$ python --version
```
You will can run the current (default) version of Python with 
```bash
$ python
```
And you can specify running Python 3 with
```bash
$ python3
```
<br>

# IDEs

While you can write and edit scripts with a text editor, you will likely want to install an integrated development environment (IDE) for developing and debugging your code.

It is recommended that you download [Eclipse](https://www.eclipse.org/downloads/) for C++ programming.

You can also use Eclipse for developing Python code, but some people prefer a dedicated Python IDE. For working on MacOS, the recommended IDE for Python is [PyCharm](https://www.jetbrains.com/pycharm/).
<br>
<br>
# Git

Git is a version management tool, especially useful for collaborating with others on shared code. If you don't already have a Github account you can make one for free on [https://github.com/](https://github.com/).

Once you have an account you should
* [Create a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/creating-a-new-repository) on Github
* [Set up Git on the command line](https://docs.github.com/en/get-started/quickstart/set-up-git#setting-up-git) and [clone your repository with SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/about-ssh) (This will allow you to contribute to files and repositories on Github from the command line)<br>
*Note: Your user.email will be recorded as part of the commit history of a repository you contribute to. If you would like your email to be kept private, you can* [manage your email settings on GitHub](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-user-account/managing-email-preferences/setting-your-commit-email-address)*. Be sure to also use your Github generated users.noreply.github.com email as your gitconfig user.email in Git.*
* [Recommended] Set up [signature verification](https://docs.github.com/en/github/authenticating-to-github/managing-commit-signature-verification/about-commit-signature-verification) with [vigilant mode](https://docs.github.com/en/github/authenticating-to-github/managing-commit-signature-verification/about-commit-signature-verification) and a GPG key. This will publically verify that changes you make to a project on GitHub are actually made by you, and not someone else disguised as your username.<br>
*Note: To do this on MacOS you will need to first* `brew install gnupg gnupg2` *to install* [GNU Privacy Guard (GPG)](https://en.wikipedia.org/wiki/GNU_Privacy_Guard) *

Optional: Help us keep these guides accurate and up-to-date (and get more familiar with Git commands and the Github workflow) by proposing changes to this repository that fix typos, formatting inconsistencies, and out-dated information: 
* [Fork this repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo) to your account
* [Create a branch](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository) for the changes you intend to make
* Make your changes to your fork
* [Send a pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) from your fork's branch to the `main` branch


