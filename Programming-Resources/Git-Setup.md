# Git and Github Setup Recommendations and Tips

This is a guide to setting up command-line Git on a MacOS computer for backing up code implementing version management in command line programming.

[Last Update: December 2021]

This guide was complied by Rob Campbell.


## Git

Git is a version management tool, especially useful for collaborating with others on shared code. You can use Git locally, on your computer, via the command line (or Terminal, on MacOS) to work with files stored remotely on Github. By using Git to synch the local and remote copies of your files you automatically keep a record of all the changes you make (making it easy to revert to previous versions), and you can easily share the remote copy with a collaborator. If two or more people are working on the same file (or set of files) in a remote Github repository, Git helps keep track of who makes which changes. It also helps you merge changes from multiple contributors into the same final file. Many people use Github for open-source software development, but in principle it can be used for any project that needs versions management (whether they are public OR private). You can access Github repositories through a variety of means, with or without contributing to them. This guide is specifically for setting up Git on the command-line for use contributing to personal or collaborative projects (such as this start-up guide).

*NOTE: Github has limited storage, and therefore it is NOT a suitable place to store data files. You can store your project code or documentation on Github, but you will need to store data separately (on your own computer, on Discovery, etc.)*

## Getting a Github account and your first repository

Before using Git on the command-line you will need a Github account (so you can have a place to host the remote copies of your repositories). If you don't already have a Github account you can make one for free on [https://github.com/](https://github.com/).

Once you have an account, you should [create a new repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/creating-a-new-repository) on Github using the Github website (note the options during set-up for public vs. private, etc.). This repository can be for anything. In these instructions we assume it is a repository for a PRoPS project, but it could also be for a personal project or just a test repository. You will need at least one repository on Github in order to set up Git on the command-line.
<br>
<br>
## Install Git on the command line

If you need more information about working on the command line, I recommend the first few lectures from ["The Missing Semester of Your CS Education"](https://missing.csail.mit.edu/). You can also look at our [MacOS System Setup Recommendations and Tips](/System-Setup/01-MacOS-Setup.md) and the early steps of the [HOOMD-blue Installation Guide](/01-HOOMDblue-Install-Guide.md) for a quick review.

Open Terminal to the home directory and use the command line to create a new directory where you want to store your Github repositories. This directory can also store non-Github files, for example it could be the "src" or "repositories" directory in your home directory, or you could create a new a "Github" specific directory. The directory does not need to be in the home directory (you could put it in another subfolder, or as a subfolfer in "repositories" etc.) but putting it in the home directory typically makes it easiest to access).

Move to the directory you chose/created and initialize Git with the command
```bash
% git init
```
This will create several files in this directory needed to use Git.

Next, you need to configure Git with your Github credentials. You can do this globally with the `--global` attribute. Set your username with
```bash
% git config --global user.name "your_Github_username"
```
and set your email (use an email address that you have verified on Github)
```bash
% git config --global user.email "the_email_you_use_with_Github"
```
*Note: Your username and email will be recorded as part of the commit history of any repository you contribute to. If you would like your email to be kept private, you can use the Github-generated `users.noreply.github.com` email instead. To access this* [manage your email settings on Github](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-user-account/managing-email-preferences/setting-your-commit-email-address)
<br>
<br>
## Linking to your account and copying your Github repository to your computer

The next steps are well documented on Github. Each step below is linked to the corresponding Github manual page.

The next step is to [set up SSH authentication for connecting to Github](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/about-ssh) (this will allow you to contribute to files and repositories on Github from the command line).

Once you have set up SSH authentication you should [clone your Github repository to your computer with SSH](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) (be sure to use the SSH link, not the HTTPS link).
<br>
<br>
## Using command-line Git

You now have a local copy of your Github repository on your computer! You can now make changes here and then push them to the main branch on Github via the command line. To practice this, use Terminal to make or edit your repository's README.md file, and then push these changes to Github with the following steps:

Stage your changes to the README.md file to Git with the command
```bash
% git add .
```

Check the status of files in your repository with
```bash
% git status
```
This will show you that a file is being tracked, but the changes have not been committed to the branch yet.

Commit the changes to your branch with
```bash
% git commit
```
This will open a new window where you should enter a comment describing the changes you made <br>
***ALWAYS add a comment explaining your commit***

You can also do this in one line with
```bash
% git commit -m "comment description"
```

You can check the status again with `git status` to see that the changes have been committed to the branch.

Push the committed changes to the `main` branch on Github with
```bash
% git push
```

You're now up to date! You can go to the repository on Github and view the changes. 

See the [Programming Resources](../Programming-Resources) folder and the [Git Cheet Sheet](../Programming-Resources/git-cheat-sheet_USletter.pdf) for more help with Git commands.
<br>
<br>
## *Optional Git Settings*: Signature Verification

It is recommended that you set up [signature verification](https://docs.github.com/en/github/authenticating-to-github/managing-commit-signature-verification/about-commit-signature-verification) with vigilant mode and a GPG key (this step verifies your identity when you make a commit, making it harder for someone else to contribute to a project in your name without your permission).

Turn on [vigilant mode](https://docs.github.com/en/github/authenticating-to-github/managing-commit-signature-verification/displaying-verification-statuses-for-all-of-your-commits) in your Github profile's Settings on the website.

Install [GNU Privacy Guard (GPG)](https://gnupg.org/) on your computer with
```bash
% brew install gnupg gnupg2
```
and make sure you have the passphrase entry management tool `pinentry` installed
```bash
% brew install pinentry
```

[Follow the steps for creating a GPG key listed here](https://docs.github.com/en/github/authenticating-to-github/managing-commit-signature-verification/checking-for-existing-gpg-keys) and then add it to your Github profile

To configure Git to sign all commits by default, run
```bash
% git config --global commit.gpgsign true
```

This allows you to commit as normal, with identity verification, but it will require you to enter your GPG passphrase to authenticate a commit. If you would like the passphrase to be automatically entered from the MacOS keychain you can install [GPG Suite](https://gpgtools.org/) (recommended by Github), or configure `gpg-agent` to save your GPG passphrase automatically.

To configure `gpg-agent` to retrieve your passphrase, use the following steps:

Install `pinentry-mac`
```bash
% brew install gnupg pinentry-mac
```
Create a `gpg-agent.config` file
```bash
% vim ~/.gnupg/gpg-agent.conf
```
Enter insert mode (by pressing "i") and copy the following text into that file (including the "#" comments)
```vim
# Connects gpg-agent to the OSX keychain via the brew-installed
# pinentry program from GPGtools. This allows the gpg key's passphrase
# to be stored in the login keychain, enabling automatic key signing.
pinentry-program /usr/local/bin/pinentry-mac
```
(save and exit the file with `:wq`)

Sign a test message so pinentry-mac can store your password in the keychain
```bash
% echo "test" | gpg --clearsign
```
A new MacOS window should pop-up prompting you to enter your passphrase. Make sure you check "Save in Keychain" and you should be all set. 

If you get a differnet pop-up (more like part of the Terminal window) without the "Save in Keychain" option then you can still enter your passphrase but it will not automatically enter it in the future. To fix this, quit all gpg-agent processes
```bash
% killall gpg-agent
```
and resrart gpg-agent in "daemon mode" (as a background process)
```bash
% gpg-agent --daemon
```
then try again:
```bash
% echo "test" | gpg --clearsign
```
You should now be set up for verified commits.
<br>
<br>
## *Optional Git Next Steps*: Contribute to the PRoPS-colloids_setup repository

You can learn more about using Git from [the Programming Resources collected in this repository](/Programming-Resources#git)

The best way to learn Git is to practice! Start using it for your own projects, and contribute to open-source projects you like (even just catching typos in Documentation can be a huge help for developers).

You can help us keep these guides accurate and up-to-date (and get more familiar with Git commands and the [Github workflow](https://guides.github.com/introduction/flow/)) by proposing changes to this repository that fix typos, formatting inconsistencies, and out-dated information: 
* [Fork this repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo) to your account
* [Create a branch](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository) for the changes you intend to make
* Make your changes to your fork
* [Send a pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) from your fork's branch to the `main` branch

