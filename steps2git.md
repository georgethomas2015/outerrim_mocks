# Using git and GitHub

If you need to: create an account in github and learn the basics with the [basic github resources](https://help.github.com/articles/git-and-github-learning-resources/), [tryGit](https://try.github.io/levels/1/challenges/1) and [a cheat sheet](https://zeroturnaround.com/rebellabs/git-commands-and-best-practices-cheat-sheet/).

Github provides free account upgrades to students and anyone working at a educational/research institute, which allow you to have your own private repositories. To get this upgrade, once you have a personal account, go to this page and fill in the form: https://education.github.com/discount_requests/new

The recommended steps to contribute to Firefly are:

1. Fork and clone: Get a copy of Firefly from the GitHub repository 
1. Update your personal copy
1. Track upstream: keeping your copy up-to-date with the main one
1. Steps to follow when working on a new (big) feature: Branch, Contribute, Commit, (Merge) and Push.
1. Submit a Pull Request to the main Firefly code.

## Fork and clone: Get a copy of Firefly from the GitHub repository 

Once you have your GitHub account and are familiar with the basic git vocabulary, create your own Firefly copy:

1. Go to https://github.com/FireflySpectra/firefly_doc or https://github.com/FireflySpectra/firefly_dev

2. Click 'Fork' there (right upper corner).
 
The next step is to get your copy of Firefly into your machine (e.g Sciama):

1. Go to your home directory in your machine.

2. Clone there your repository. From your OWN local repository (firefly_[doc/dev] at your Sciama home):

```   
>  git clone https://[username]@github.com/[username]/firefly_[doc/dev]
```

You'll be prompt for your GitHub username and password.

## Updating your Firefly copy.

Ensure that the remote is the correct one: 
```
> git remote -v
```

If you need to reset the remote link:
```
> git remote set-url origin https://[git username]@github.com/[git username]/firefly_[doc/dev]
```
   
Update your personal copy:

```
> git push origin master
```

## Track upstream: keeping your copy up-to-date with the main one

This instructions follow the recommendations on [syncing a fork from GitHub](ttps://help.github.com/articles/syncing-a-fork/). To make sure that your version remains up to date with
the master version, set the upstream tracking:

```
> git remote add --track master upstream https://[username]@github.com/FireflySpectra/firefly_doc
```

Now, every time you need to apply the changes that have been made to the master version to yours, navigate to your Firefly directory and run:

```
> git fetch upstream
> git merge upstream/master
```

## Working on a new (big) feature

### Branch, contribute and Commit

To start working on new feature, create a separate feature branch:

    git checkout -b feature

You can check the branches you have by:

    git branch

And switch between them with:

    git checkout master
    git checkout feature

Once some changes have been made in the branch, stage them
and commit:

    git add .
    git commit -m "Add a comment here"

### (Merge and) Push

You can push changes with:

    git push origin feature

Alternatively, you can merge the changes with the master
branch first, and then push:

    git checkout master
    git merge feature
    git push origin master

## Submit a Pull Request

When you are ready to update the main Firefly code, go to your GitHub Firefly page, click "New pull request" to create a Pull Request from your
latest commit. It will be applied by someone with
administrator master version  rights after review.

# Steps to create a new release under firefly_release

Following the instructions given [here](http://ctarda.com/2015/11/private-development-public-release/):

    git clone https://[username]@github.com/[username]/firefly_[doc/dev]
    cd [firefly_dev]
    git checkout -b release/release
    git push origin release/release
    git checkout -b release/github-master
    git push origin release/github-master
    git merge --squash release/release
    git tag 0.0.1 -m "Firefly first release"
    git remote add github https://github.com/FireflySpectra/firefly_release.git
    git push github HEAD:master

# Steps to create a new shared repository in Sciama

On server (/mnt/lustre/firefly):
> git init --bare --shared [new].git


On client (a directory on your home):
> mkdir [new]
> cd [new]
> echo "# README" >> README.md
> git init
> git add .
> git commit -m "Initial commit"
> git remote add origin /mnt/lustre/firefly/[new].git
> git push origin master

